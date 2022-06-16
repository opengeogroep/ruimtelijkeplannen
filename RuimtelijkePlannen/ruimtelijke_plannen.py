# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RuimtelijkePlannen
                                 A QGIS plugin
 Plugin for using Dutch online zoning plans from www.ruimtelijkeplannen.nl
                              -------------------
        begin                : 2017-06-25
        git sha              : $Format:%H$
        copyright            : (C) 2019 by OpenGeoGroep
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
                        QgsGeometry, QgsPoint, QgsPointXY, QgsMessageLog, \
                        QgsActionManager, QgsAction, Qgis, \
                        QgsCoordinateReferenceSystem, QgsCoordinateTransform
from qgis.PyQt import QtCore
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, \
                             QSortFilterProxyModel, QUrl, QSize

from qgis.PyQt.QtWidgets import QAction, QLineEdit, QAbstractItemView, \
                                QCompleter, QMessageBox, QHeaderView, QApplication
from qgis.PyQt.QtGui import QIcon, QStandardItemModel, QStandardItem, QPixmap, \
                            QCursor, QDesktopServices

# Initialize Qt resources from file resources.py
from . import resources

# Import the code for the dialog
from .ruimtelijke_plannen_dialog import RuimtelijkePlannenDialog
from .ruimtelijke_plannen_settings_dialog import RuimtelijkePlannenSettingsDialog


import json
import os.path
import urllib

from .network import networkaccessmanager

layer_action = '''
from qgis.core import QgsMessageLog, Qgis
from qgis.PyQt.QtGui import QDesktopServices
from qgis.PyQt.QtCore import QUrl

urls = ""
if "[%verwijzingNaarTekst%]":
    urls = "[%verwijzingNaarTekst%]"
elif "[%verwijzingNaarObjectgerichteTekst%]":
    urls = "[%verwijzingNaarObjectgerichteTekst%]"

if urls:
    qgis.utils.iface.messageBar().pushMessage('Info', 
                    u"Opening text documents...",
                    level=Qgis.Info)
    for url in urls.split(','):
        QDesktopServices().openUrl(QUrl(url))
else:
    qgis.utils.iface.messageBar().pushMessage('Warning', 
                    u"No text documents found to open.",
                    level=Qgis.Warning)
'''

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
        svbp_plannen = ['bestemmingsplan',
                        'inpassingsplan',
                        'uitwerkingsplan',
                        'wijzigingsplan']
        prpcp_plannen = ['gemeentelijk plan; bestemmingsplan artikel 10',
                         'gemeentelijk plan; uitwerkingsplan artikel 11',
                         'gemeentelijk plan; voorbereidingsbesluit',
                         'gemeentelijk plan; wijzigingsplan artikel 11',
                         'gemeentelijke visie; overig']
        
        if self.plantype in svbp_plannen:
            return [ \
                {'name': 'app:Bestemmingsplangebied', 
                 'qml': 'bestemmingsplangebied_imro_qgis.qml', 
                 'text_action': True},
                {'name': 'app:Figuur', 
                 'qml': 'figuur.qml', 
                 'text_action': False},
                {'name': 'app:Lettertekenaanduiding', 
                 'qml': 'lettertekenaanduiding.qml', 
                 'text_action': False},
                {'name': 'app:Functieaanduiding', 
                 'qml': 'functieaanduiding_digitaal.qml', 
                 'text_action': False},
                {'name': 'app:Maatvoering', 
                 'qml': 'maatvoering_digitaal.qml', 
                 'text_action': False},
                {'name': 'app:Bouwaanduiding',
                 'qml': 'bouwaanduiding_imro_qgis.qml', 
                 'text_action': False},
                {'name': 'app:Bouwvlak', 
                 'qml': 'bouwvlak_digitaal.qml', 
                 'text_action': False},
                {'name': 'app:Gebiedsaanduiding', 
                 'qml': 'gebiedsaanduiding_imro_qgis.qml', 
                 'text_action': False},
                {'name': 'app:Dubbelbestemming',
                 'qml': 'dubbelbestemming_digitaal.qml', 
                 'text_action': True},
                {'name': 'app:Enkelbestemming',
                 'qml': 'enkelbestemming_imro_qgis.qml', 
                 'text_action': True}]
        elif self.plantype in prpcp_plannen:
            return [ {'name': 'app:Plangebied_PCP', 
                      'qml': 'plangebied.qml', 
                      'text_action': True} ]
        else:
            # We should make this explicit. At least:
            # voorbereidingsbesluit, beheersverordening, omgevingsvergunning,
            # gerechtelijke uitspraak, reactieve aanwijzing
            return [ {'name': 'app:Besluitgebied_X', 
                      'qml': 'plangebied.qml', 
                      'text_action': True},
                     {'name': 'app:Besluitsubvlak_X', 
                      'qml': 'besluitvlak.qml', 
                      'text_action': True},
                     {'name': 'app:Besluitvlak_X', 
                      'qml': 'besluitvlak.qml', 
                      'text_action': True}]


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
        if not QSettings().value('locale/userLocale'):
            locale = QSettings().value('locale/globalLocale')[0:2]
        else:
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
        
        # initialize styles folder
        self.settings = QSettings()
        self.available_styles_folder = os.path.join(self.plugin_dir,'styles')
        self.map_style = self.settings.value("RuimtelijkePlannen/map_style",
            "print")
        self.map_style_folder = os.path.join(self.available_styles_folder,
            self.map_style)
        if not os.path.isdir(self.map_style_folder):
            self.map_style = "print"
            self.map_style_folder = os.path.join(self.available_styles_folder,
                self.map_style)

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
        self.settings_dlg = RuimtelijkePlannenSettingsDialog()
                
        self.add_action(
            dialog = None,
            icon_path = ':/plugins/RuimtelijkePlannen/help.png',
            text=self.tr(u'Help'),
            callback=self.open_help,
            parent=self.iface.mainWindow(),
            add_to_toolbar=False)
            
        self.add_action(
            dialog = None,
            icon_path = ':/plugins/RuimtelijkePlannen/settings.png',
            text=self.tr(u'Settings'),
            callback=self.run_settings,
            parent=self.iface.mainWindow(),
            add_to_toolbar=False)

        # add a button to click in map and find bestemmingsplannen
        self.action = self.add_action(
            dialog = None,
            icon_path = ':/plugins/RuimtelijkePlannen/icon.png',
            text=self.tr(u'Click map query RuimtelijkePlannen'),
            callback=self.activate_tool,
            add_to_menu=True,
            status_tip=self.tr(u'Click map query RuimtelijkePlannen'),
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
        self.dlg.treeView_results.setSortingEnabled(True)
        self.dlg.treeView_results.doubleClicked.connect(self.loadRPplan)

        # have an info icon at hand for keuzehulp
        self.infoIcon = QIcon(':/plugins/RuimtelijkePlannen/info.png')
                
        # have the right crs at hand
        self.rp_crs = QgsCoordinateReferenceSystem(28992)
        
        ## urls to RuimtelijkePlannen
        ## this one is the traditional one
        # self.rp_search_url = "https://www.ruimtelijkeplannen.nl/web-roo/rest/search"
        # self.rp_search_id_resource = "/plan/id/"
        # self.rp_search_xy_resource = "/plannen/xy/"
        ## this one is new and has more metadata with the "keuzehulp"!
        #self.rp_search_url = "https://www.ruimtelijkeplannen.nl/plannenservice"
        self.rp_search_url = "https://afnemers.ruimtelijkeplannen.nl/plannenservice"
        self.rp_search_headers = {"Referer": "https://plugins.qgis.org/plugins/RuimtelijkePlannen/"}
        self.rp_search_id_resource = "/plannen/identificatie/"
        self.rp_search_xy_resource = "/plannen/xy/"
        
        self.rp_wfs_url = "https://afnemers.ruimtelijkeplannen.nl/afnemers2012/services"
        
        # the following lists of plantypes comes from: 
        # https://www.ruimtelijkeplannen.nl/viewer/planoverzicht
        self.rp_supported_planTypes = [\
            'aanwijzingsbesluit',
            'beheersverordening',
            'bestemmingsplan',
            'exploitatieplan',
            'gemeentelijk plan; bestemmingsplan artikel 10', 
            'gemeentelijk plan; uitwerkingsplan artikel 11',
            'gemeentelijk plan; voorbereidingsbesluit',
            'gemeentelijk plan; wijzigingsplan artikel 11',
            'gemeentelijke visie; overig',
            'gerechtelijke uitspraak', 
            'inpassingsplan',
            'omgevingsvergunning',
            'projectbesluit',
            'reactieve aanwijzing',
            'tijdelijke ontheffing buitenplans',
            'uitwerkingsplan',
            'voorbereidingsbesluit',
            'wijzigingsplan'
            ]
        self.rp_not_supported_plantypes = [\
            # these are the plan types which can have multiple maps
            'amvb',
            'provinciale verordening',
            'regeling',
            'structuurvisie'
            ]

        # There seem te be more plan types. The following list comes from
        # Kadaster internal documenation
        # This list should be merged with the above
        #* Mother plan: no; dedicated procedure (dossier): yes

              #"bestemmingsplan"
              #"Chw bestemmingsplan"
              #"gemeentelijk plan; bestemmingsplan artikel 10"
              #"rijksbestemmingsplan"
              #"inpassingsplan"
              #"beheersverordening"
              #"aanwijzingsbesluit"
              #"reactieve aanwijzing"
              #"exploitatieplan"

        #* Mother plan: yes; dedicated procedure (dossier): yes

              #"wijzigingsplan"
              #"gemeentelijk plan; wijzigingsplan artikel 11"
              #"uitwerkingsplan"
              #"gemeentelijk plan; uitwerkingsplan artikel 11"
              #"omgevingsvergunning"
              #"projectbesluit"
              #"tijdelijke ontheffing buitenplans"

        #* Mother plan: yes; dedicated procedure: no (potentially in dossier mother plan)

              #"voorbereidingsbesluit"
              #"gemeentelijk plan; voorbereidingsbesluit"
              #"gerechtelijke uitspraak"


        # layer action on RuimtelijkePlannen layers to show links to text
        self.rp_layer_action = QgsAction(QgsAction.GenericPython, 
                                    'Open text link(s) in browser ', 
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
        
        
    def open_help(self):
        '''
        Method to open the help pages
        '''
        
        QDesktopServices().openUrl(QUrl.fromLocalFile(os.path.join("file://",
            self.plugin_dir, 'help/build/html','index.html')))
        
    def run_settings(self):
        '''
        method showing the settings dialog and act on the results
        '''

        # we do this on opening this setting, so the user can easily add 
        # new styles wthout reloading the plugin.
        available_styles = next(os.walk(self.available_styles_folder))[1]
        self.settings_dlg.styleComboBox.clear()
        self.settings_dlg.styleComboBox.addItems(available_styles)
        
        index = self.settings_dlg.styleComboBox.findText(self.map_style)
        self.settings_dlg.styleComboBox.setCurrentIndex(index)

        self.settings_dlg.show()        
        result = self.settings_dlg.exec_()
        if result:
            map_style_folder = os.path.join(self.available_styles_folder,
                self.settings_dlg.styleComboBox.currentText())
            if os.path.isdir(map_style_folder):
                self.map_style = self.settings_dlg.styleComboBox.currentText()
                self.map_style_folder = os.path.join(self.available_styles_folder,
                    self.map_style)
                self.settings.setValue("RuimtelijkePlannen/map_style", 
                    self.map_style)
            else:
                self.iface.messageBar().pushMessage('Warning', 
                    self.tr(u"Selected style folder not found. See message log for details."),
                    level=Qgis.Warning)
                QgsMessageLog.logMessage(u'Style folder not found: ' + \
                    os.path.join(self.available_styles_folder, self.map_style), 
                    'RuimtelijkePlannen')
            
    def activate_tool(self):
        self.mapcanvas.setMapTool(self.xytool)

    def addRPplanFromToolbar(self):
        '''slot for toolbarSearch'''
        self.addFromIdn(self.toolbarSearch.text())

    def addFromIdn(self, search_string):
        '''adds plan from idn'''
        self.toolbarSearch.clear()
        url = self.rp_search_url + self.rp_search_id_resource + search_string
        QgsMessageLog.logMessage(u'Query: ' + str(url), 'RuimtelijkePlannen')
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        (response, content) = self.nam.request(url, headers = self.rp_search_headers)
        self.rp = json.loads(content.decode("utf-8"))
        
        QApplication.restoreOverrideCursor()
        if "ErrorType" in self.rp \
        or ('aantal' in self.rp and self.rp['aantal'] == 0):
            self.iface.messageBar().pushMessage("Error",
                self.tr(u'Plan not found.'), 
                level = Qgis.Critical)
            return
        if 'resultaat' in self.rp:
            # we are using the keuzeHulp
            self.rp = self.rp['plannen'][0]        
        if not self.rp["typePlan"] in self.rp_supported_planTypes:
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

    def addRPplan_WFS(self, plangebied, plantype):
        '''adds a plan as a WFS layer'''
        
        QgsMessageLog.logMessage(u'Adding plan with IDN "%s" and plantype "%s"'\
            % (plangebied,plantype), 'RuimtelijkePlannen')
        
        # add a layergroup to insert the layers in
        bpGroup = QgsProject.instance().layerTreeRoot().insertGroup(0, plangebied)
        
        service = self.rp_wfs_url
        wfs_filter = '"plangebied"=\'' + plangebied + '\''
        plan = rp_plan(plantype)
        for layer in plan.layers:
            vlayer = self.getWfsLayer(service, layer['name'], wfs_filter)
            if vlayer.isValid():
                if 'qml' in layer:
                    layerQml = os.path.join(self.map_style_folder, layer['qml'])
                    if os.path.exists(layerQml):
                        vlayer.loadNamedStyle(layerQml)
                    else:
                        self.iface.messageBar().pushMessage('Warning', 
                            self.tr(u"Style not found. See message log for details."),
                            level=Qgis.Warning)
                        QgsMessageLog.logMessage(u'Style file not found: ' + \
                            str(layerQml), 'RuimtelijkePlannen')
                if layer['text_action']:
                    vlayer.actions().addAction(self.rp_layer_action)
                self.project.addMapLayer(vlayer, False)
                bpGroup.insertChildNode(-1, QgsLayerTreeLayer(vlayer))
            else:
                self.iface.messageBar().pushMessage('Warning', 
                    self.tr(u"Invalid layer: ") + layer['name'],
                    level=Qgis.Warning)
                
        vlayer.selectAll()
        canvas = self.iface.mapCanvas()
        canvas.zoomToSelected(vlayer)
        vlayer.removeSelection()

    def loadRPplan(self, index):
        '''slot for row in search results widget'''
        self.dlg.hide()
        self.addRPplan_WFS( plangebied = index.sibling(index.row(),1).data(), 
                            plantype = index.sibling(index.row(),3).data())

    def addSourceRow(self, nr, plan, keuze_hulp = None):
        '''adds plan to search results widget'''
        if plan["typePlan"] in self.rp_supported_planTypes:
            nr = QStandardItem(str(nr + 1))
            planId = QStandardItem(plan["identificatie"])
            if keuze_hulp:
                planStatus = QStandardItem(self.infoIcon, plan["planStatus"])
                f = planStatus.font()
                f.setUnderline(True)
                planStatus.setFont(f)
                planStatus.setToolTip('%s: %s' % (
                                        keuze_hulp["positieTekst"],
                                        keuze_hulp["keuzeHulpTekst"])
                                     )
            else:
              planStatus = QStandardItem(plan["planStatus"])
            planNaam = QStandardItem(plan["naam"])
            planType = QStandardItem(plan["typePlan"])
            #planGebiedType = QStandardItem(plan["planGebiedType"])
            # not yet(?) in use by this plugin
            self.sourceModel.appendRow( [ nr, planId, planStatus, planType, planNaam] )
            
    def addSourceRowFromKeuzeHulp(self, nr, plan_en_keuze):
        '''adds plan to search results widget'''
        keuze_hulp = plan_en_keuze['keuzeHulp']
        plan = plan_en_keuze['planDto']

        self.addSourceRow(nr, plan, keuze_hulp)
            
    def getRPplannenByPoint(self, event):
        '''Queries ruimtelijkeplannen by point and shows results on widget.'''
        
        xform = QgsCoordinateTransform(
                self.mapcanvas.mapSettings().destinationCrs(),
                self.rp_crs, 
                QgsProject.instance())
        xy = xform.transform(QgsPointXY(
                    self.mapcanvas.getCoordinateTransform().toMapCoordinates(
                        event.pos().x(), 
                        event.pos().y())))

        self.sourceModel.clear()
        url = self.rp_search_url + self.rp_search_xy_resource + str(xy.x()) + "/" + str(xy.y())
        QgsMessageLog.logMessage(u'Query: ' + str(url), 'RuimtelijkePlannen')

        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor) 
        (response, content) = self.nam.request(url, headers = self.rp_search_headers)
        self.rp = json.loads(content.decode("utf-8"))

        if "ErrorType" in self.rp:
            self.iface.messageBar().pushMessage("Error",
                self.tr(u'No Plans found.') + self.rp["ErrorDescription"], 
                level = Qgis.Critical)
            QApplication.restoreOverrideCursor()
            return

        if 'plannen' in self.rp:
            for nr, plan in enumerate(self.rp["plannen"]):
                self.addSourceRow(nr, plan)
        else:
            for nr, plan_en_keuze in enumerate(self.rp["keuzeHulpPlannen"]):
                self.addSourceRowFromKeuzeHulp(nr, plan_en_keuze)

        if not self.sourceModel.rowCount():
            QApplication.restoreOverrideCursor()
            return 

        self.sourceModel.setHeaderData(0, QtCore.Qt.Horizontal, "Nr")
        self.sourceModel.setHeaderData(1, QtCore.Qt.Horizontal, "Identification")
        self.sourceModel.horizontalHeaderItem(1).setTextAlignment(QtCore.Qt.AlignLeft)
        self.sourceModel.setHeaderData(2, QtCore.Qt.Horizontal, "Status")
        self.sourceModel.setHeaderData(3, QtCore.Qt.Horizontal, "Type")
        self.sourceModel.setHeaderData(4, QtCore.Qt.Horizontal, "Name")
        self.dlg.treeView_results.setColumnHidden(0, True)
        self.dlg.treeView_results.resizeColumnsToContents()
        self.dlg.treeView_results.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.dlg.treeView_results.setSelectionMode(1)
        self.dlg.treeView_results.selectRow(0)
        # sort on order of the keuzehulp, instead of status.
        #self.dlg.treeView_results.sortByColumn(2, QtCore.Qt.AscendingOrder)
        self.dlg.treeView_results.sortByColumn(0, QtCore.Qt.AscendingOrder)
        QApplication.restoreOverrideCursor()
        self.dlg.show()
