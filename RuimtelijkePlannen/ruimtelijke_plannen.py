# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RuimtelijkePlannen
                                 A QGIS plugin
 Plugin for using Dutch online zoning plans from www.ruimtelijkeplannen.nl
                              -------------------
        begin                : 2017-06-25
        git sha              : $Format:%H$
        copyright            : (C) 2017 by OpenGeoGroep
        email                : info@opengeogroep.nl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from __future__ import print_function
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import str
from builtins import object

from qgis.gui import QgsMapTool
from qgis.core import   QgsProject, QgsVectorLayer, QgsLayerTreeLayer, \
                        QgsGeometry, QgsMessageLog, \
                        QgsActionManager, QgsAction
from qgis.PyQt import QtCore
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, \
                             QSortFilterProxyModel

from qgis.PyQt.QtWidgets import QAction, QLineEdit, QAbstractItemView, \
                                QCompleter, QMessageBox, QHeaderView, QApplication
from qgis.PyQt.QtGui import QIcon, QStandardItemModel, QStandardItem, QPixmap, QCursor

# Initialize Qt resources from file resources.py
from . import resources
# Import the code for the dialog
from .ruimtelijke_plannen_dialog import RuimtelijkePlannenDialog

import json
import os.path
import urllib

from .network import networkaccessmanager

class GetPointTool(QgsMapTool):

    def __init__(self, canvas, callback):
        QgsMapTool.__init__(self, canvas)
        self.callback = callback
        self.canvas = canvas
        self.cursor = QCursor(QPixmap(
            ["16 16 4 1", 
             "  c None", ". c #7198d7", "+ c #7198d7", "- c #7198d7",
                                    "                ",
                                    "                ",
                                    "      +++++     ",
                                    "     +++++++    ",
                                    "    +.     .+   ",
                                    "   +.   -   .+  ",
                                    "  +.   ---   .+ ",
                                    " ++.  -----  .++",
                                    " ++  -------  ++",
                                    " ++.  -----  .++",
                                    "  +.   ---   .+ ",
                                    "   +.   -   .+  ",
                                    "   ++.     .+   ",
                                    "    ++++++++    ",
                                    "      +++++     ",
                                    "                "]))

    def canvasPressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.pos = self.toMapCoordinates(e.pos())

    def canvasReleaseEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.callback(e)

    def activate(self):
        self.canvas.setCursor(self.cursor)

class rp_plan(object):
    '''
    A class for accessing layers and styles belonging to a plantype.
    '''
    
    def __init__(self, plantype):
        '''
        Constructor
        '''
        
        self.plantype = plantype
    
    @property    
    def layers(self):
        '''
        The layers and styles for the plantype.
        
        '''
        if self.plantype == 'bestemmingsplan':
            return [ \
                {'name': 'app:Figuur'},
                {'name': 'app:Lettertekenaanduiding'},
                {'name': 'app:Functieaanduiding', 'qml': 'functieaanduiding_digitaal.qml'},
                {'name': 'app:Maatvoering', 'qml': 'maatvoering_digitaal.qml'},
                {'name': 'app:Bouwaanduiding', 'qml': 'bouwaanduiding_imro_qgis.qml'},
                {'name': 'app:Bouwvlak', 'qml': 'bouwvlak_digitaal.qml'},
                {'name': 'app:Gebiedsaanduiding'},
                {'name': 'app:Dubbelbestemming', 'qml': 'dubbelbestemming_digitaal.qml'},
                {'name': 'app:Enkelbestemming', 'qml': 'enkelbestemming_imro_qgis.qml'},
                {'name': 'app:Bestemmingsplangebied', 'qml': 'bestemmingsplangebied_imro_qgis.qml'} ]
        elif self.plantype == 'gemeentelijk plan; bestemmingsplan artikel 10':
            return [ {'name': 'app:Plangebied_PCP', 'qml': 'plangebied.qml'} ]
        else:
            # ten minste:
            # voorbereidingsbesluit, beheersverordening, omgevingsvergunning,
            # gerechtelijke uitspraak, reactieve aanwijzing
            return [ {'name': 'app:Besluitsubvlak_X', 'qml': 'besluitvlak.qml'},
                     {'name': 'app:Besluitvlak_X', 'qml': 'besluitvlak.qml'},
                     {'name': 'app:Besluitgebied_X', 'qml': 'plangebied.qml'} ]

layer_action = '''
from qgis.core import QgsMessageLog
from qgis.PyQt.QtGui import QDesktopServices
from qgis.PyQt.QtCore import QUrl

urls = ""
if "[%verwijzingNaarTekst%]":
    urls = "[%verwijzingNaarTekst%]"
elif "[%verwijzingNaarObjectgerichteTekst%]":
    urls = "[%verwijzingNaarObjectgerichteTekst%]"

if not ',' in urls:
    urls = [urls]
else:
    urls = urls.split(',')

for url in urls:
    QDesktopServices().openUrl(QUrl(url))
'''



class RuimtelijkePlannen(object):
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface and the mapCanvas
        self.iface = iface
        self.mapcanvas = iface.mapCanvas()
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'RuimtelijkePlannen_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Ruimtelijke Plannen')
        self.toolbar = self.iface.addToolBar(u'RuimtelijkePlannen')
        self.toolbar.setObjectName(u'RuimtelijkePlannen')
        
        self.nam = networkaccessmanager.NetworkAccessManager()
        self.project = QgsProject.instance()

    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """

        return QCoreApplication.translate('RuimtelijkePlannen', message)


    def add_action(
        self,
        dialog,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        if dialog:
            self.dlg = dialog

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToWebMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        self.dlg = RuimtelijkePlannenDialog()

        # add a button to click in map and find bestemmingsplannen
        self.action = self.add_action(
            dialog = None,
            icon_path = ':/plugins/RuimtelijkePlannen/icon.png',
            text=self.tr(u'Click map to open query RuimtelijkePlannen'),
            callback=self.activate_tool,
            add_to_menu=False,
            status_tip=self.tr(u'Click map to open query RuimtelijkePlannen'),
            parent=self.iface.mainWindow())
        self.action.setCheckable(True)
        # add it to the same group as the pan/zoom tools
        self.iface.actionPan().actionGroup().addAction(self.action)
        self.xytool = GetPointTool(self.mapcanvas, self.getRPplannenByPoint)
            
        self.toolbarSearch = QLineEdit()
        self.toolbarSearch.setMaximumWidth(200)
        self.toolbarSearch.setAlignment(QtCore.Qt.AlignLeft)
        self.toolbarSearch.setPlaceholderText("NL.IMRO.")
        self.toolbar.addWidget(self.toolbarSearch)
        self.toolbarSearch.returnPressed.connect(self.addRPplanFromToolbar)

        self.proxyModel = QSortFilterProxyModel()
        self.sourceModel = QStandardItemModel()
        self.proxyModel.setSourceModel(self.sourceModel)
    
        self.dlg.treeView_results.setModel(self.proxyModel)
        self.dlg.treeView_results.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dlg.treeView_results.doubleClicked.connect(self.loadRPplan)
        
        # urls to RuimtelijkePlannen
        self.rp_search_url = "https://www.ruimtelijkeplannen.nl/viewer/web-roo/rest/search"
        self.rp_wfs_url = "https://afnemers.ruimtelijkeplannen.nl/afnemers2012/services"
        
        # supported tabs on RuimtelijkePlannen
        self.rp_supported_tabs = ["JURIDISCH"]
        
        # layer action on RuimtelijkePlannen layers to show links to text
        self.rp_layer_action = QgsAction(QgsAction.GenericPython, 
                                    'Toon verwijzing(en) naar tekst', 
                                    layer_action, "", False, "", 
                                    {'Feature', 'Canvas'})


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginWebMenu(
                self.tr(u'&Ruimtelijke Plannen'),
                action)
            self.iface.removeToolBarIcon(action)
        del self.toolbar
            
    def activate_tool(self):
        self.mapcanvas.setMapTool(self.xytool)

    def addRPplanFromToolbar(self):
        '''slot for toolbarSearch'''
        self.addFromIdn(self.toolbarSearch.text())

    def addFromIdn(self, search_string):
        '''adds plan from idn'''
        self.toolbarSearch.clear()
        url = self.rp_search_url + "/plan/id/" + search_string
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)       # wait cursor
        (response, content) = self.nam.request(url)
        self.rp = json.loads(content.decode("utf-8"))
        QApplication.restoreOverrideCursor()                    # restore cursor
        if "ErrorType" in self.rp:
            self.iface.messageBar().pushMessage("Error",
                self.tr(u'Plan not found.') + self.rp["ErrorDescription"], 
                level = Qgis.Critical)
        elif not self.rp["tabFilter"] in self.rp_supported_tabs:
            self.iface.messageBar().pushMessage("Error",
                self.tr(u'Plan type not supported.'), 
                level = Qgis.Critical)
        else:
            self.addRPplan_WFS(plangebied = search_string, 
                               plantype = self.rp["typePlan"])

    def getWfsLayer(self, service, typename, wfs_filter):
        params = {
            'service': 'WFS',
            'version': '1.1.0',
            'request': 'GetFeature',
            'typename': typename,
            'filter': wfs_filter,
            'srsname': 'EPSG:28992',
        }
        if not service[-1] == '?':
            service += '?'
        uri = service + urllib.parse.unquote(urllib.parse.urlencode(params))
        layername = typename
        vlayer = QgsVectorLayer(uri, layername, "WFS")
        return vlayer

    def addRPplan_WFS(self, plangebied, plantype = 'bestemmingsplan'):
        '''adds a plan as a WFS layer'''
        service = self.rp_wfs_url
        wfs_filter = '"plangebied"=\'' + plangebied + '\''
        
        plan = rp_plan(plantype)
        # add a layergroup to insert the layers in
        bpGroup = QgsProject.instance().layerTreeRoot().insertGroup(0, plangebied)
        for layer in plan.layers:
            vlayer = self.getWfsLayer(service, layer['name'], wfs_filter)
            if vlayer.isValid():
                if 'qml' in layer:
                    layerQml = os.path.join(self.plugin_dir, 
                                            'styles',  
                                            layer['qml'])
                    if os.path.exists(layerQml):
                        vlayer.loadNamedStyle(layerQml)
                vlayer.actions().addAction(self.rp_layer_action)
                self.project.addMapLayer(vlayer, False)
                bpGroup.insertChildNode(-1, QgsLayerTreeLayer(vlayer))
            else:
                self.iface.messageBar().pushMessage('Warning', 
                    self.tr(u"Invalid layer: ") + layer['name'],
                    level=Qgis.WARNING)
                
        vlayer.selectAll()
        canvas = self.iface.mapCanvas()
        canvas.zoomToSelected(vlayer)
        vlayer.removeSelection()

    def loadRPplan(self, index):
        '''slot for row in search results widget'''
        self.dlg.hide()
        self.addRPplan_WFS( plangebied = index.sibling(index.row(),0).data(), 
                            plantype = index.sibling(index.row(),1).data())

    def addSourceRow(self, plan):
        '''adds plan to search results widget'''
        if plan["tabFilter"] in self.rp_supported_tabs:
            planId = QStandardItem(plan["identificatie"])
            planNaam = QStandardItem(plan["naam"])
            planType = QStandardItem(plan["typePlan"])
            #planGebiedType = QStandardItem(plan["planGebiedType"])      # not yet(?) in use by this plugin
            #self.sourceModel.appendRow( [ planId, planType, planNaam, planGebiedType] )
            self.sourceModel.appendRow( [ planId, planType, planNaam] )
            
    def getRPplannenByPoint(self, event):
        '''Queries ruimtelijkeplannen by point and shows results on widget.'''
        
        x, y = self.mapcanvas.getCoordinateTransform().toMapCoordinates(
                    event.pos().x(), event.pos().y())
        # todo: what if not 28992?
        # actual_crs_id = self.mapcanvas.mapRenderer().destinationCrs().authid()
        
        self.sourceModel.clear()
        url = self.rp_search_url + "/plannen/xy/" + str(x) + "/" + str(y)

        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)       # wait cursor
        (response, content) = self.nam.request(url)
        self.rp = json.loads(content.decode("utf-8"))

        for plan in self.rp["plannen"]:
            self.addSourceRow(plan)

        self.sourceModel.setHeaderData(0, QtCore.Qt.Horizontal, "Identificatie")
        self.sourceModel.horizontalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignLeft)
        self.sourceModel.setHeaderData(1, QtCore.Qt.Horizontal, "Type")
        self.sourceModel.setHeaderData(2, QtCore.Qt.Horizontal, "Naam")
        self.dlg.treeView_results.resizeColumnsToContents()
        self.dlg.treeView_results.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.dlg.treeView_results.setSelectionMode(1)
        self.dlg.treeView_results.selectRow(0)
        QApplication.restoreOverrideCursor()                    # restore cursor
        self.dlg.show()
