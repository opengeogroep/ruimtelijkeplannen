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
from qgis.core import QgsProject, QgsVectorLayer, QgsMapLayerRegistry, \
    QgsGeometry
from PyQt4.QtCore import Qt, QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon, QLineEdit, QSortFilterProxyModel, \
    QAbstractItemView, QStandardItemModel, QStandardItem, QCompleter, \
    QStringListModel, QMessageBox, QHeaderView
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from ruimtelijke_plannen_dialog import RuimtelijkePlannenDialog

import os.path
import urllib
import json
import pdokgeocoder


class RuimtelijkePlannen:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
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
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'RuimtelijkePlannen')
        self.toolbar.setObjectName(u'RuimtelijkePlannen')
        
        self.geolocator = pdokgeocoder.PDOKGeoLocator(self.iface)


    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('RuimtelijkePlannen', message)


    def add_action(
        self,
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

        # Create the dialog (after translation) and keep reference
        self.dlg = RuimtelijkePlannenDialog()

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

        icon_path = ':/plugins/RuimtelijkePlannen/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Ruimtelijke plannen'),
            callback=self.run,
            parent=self.iface.mainWindow())

        self.toolbarSearch = QLineEdit()
        self.toolbarSearch.setMaximumWidth(200)
        self.toolbarSearch.setAlignment(Qt.AlignLeft)
        self.toolbarSearch.setPlaceholderText("Bestemmingsplan code")
        self.toolbar.addWidget(self.toolbarSearch)
        self.toolbarSearch.returnPressed.connect(self.searchBestemmingsplanFromToolbar)

        # skip initial load for now
        #url = "http://www.ruimtelijkeplannen.nl/web-roo/rest/search/plannen/id/NL.IMRO.0687"
        #response = urllib.urlopen(url)
        #self.pdok = json.loads(response.read())

        self.proxyModel = QSortFilterProxyModel()
        self.sourceModel = QStandardItemModel()
        self.proxyModel.setSourceModel(self.sourceModel)
    
        self.dlg.treeView_results.setModel(self.proxyModel)
        self.dlg.treeView_results.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #for service in self.pdok["idns"]:
        #    itemLayername = QStandardItem( service )
        #    self.sourceModel.appendRow( itemLayername )

        self.dlg.lineEdit_id.setPlaceholderText("Bestemmingsplan code")
        self.dlg.lineEdit_address.setPlaceholderText("zoek op adres")
        #self.dlg.lineEdit_id.textChanged.connect(self.filterBestemmingsplannen)
        #self.dlg.lineEdit_address.textChanged.connect(self.filterAddresses)
        self.dlg.lineEdit_id.returnPressed.connect(self.filterBestemmingsplannen)
        self.dlg.lineEdit_address.returnPressed.connect(self.getBestemmingsplannenByAddress)
        self.dlg.treeView_results.doubleClicked.connect(self.loadBestemmingsplan)

        #self.sourceModel.setHeaderData(0, Qt.Horizontal, "Bestemmingsplan")
        #self.sourceModel.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        #self.sourceModel.setHeaderData(1, Qt.Horizontal, "Naam")
        #self.dlg.treeView_results.resizeColumnsToContents()
        #completer = QCompleter()
        #self.dlg.lineEdit_address.setCompleter(completer) 
        #self.stringModel = QStringListModel()
        #completer.setModel(self.stringModel)





    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginWebMenu(
                self.tr(u'&Ruimtelijke Plannen'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar


    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass
            

    def filterAddresses(self, search_string):
        if len(search_string) > 0:
            self.sourceModel.clear()
            url = "http://www.ruimtelijkeplannen.nl/web-roo/rest/search/geocodertokens/" + search_string
            response = urllib.urlopen(url)
            self.pdok = json.loads(response.read())

            self.stringList = [];
            
            for service in self.pdok:
                self.stringList.append(service["adres"])

            self.stringModel.setStringList(self.stringList)

    def getWfsLayer(self, service, typename, filter):
        params = {
            'typename': typename,
            'filter': filter,
            'srsname': 'EPSG:28992',
        }
        if not service[-1] == '?':
            service += '?'
        uri = service + urllib.unquote(urllib.urlencode(params))
        layername = typename
        vlayer = QgsVectorLayer(uri, layername, "WFS")
        return vlayer

    def searchBestemmingsplanFromToolbar(self):
        self.geocode(self.toolbarSearch.text())

    def geocode(self, search_string):
        self.toolbarSearch.clear()
        self.addBestemmingsplan(search_string)

    def addBestemmingsplan(self, plangebied):
        service = 'http://afnemers.ruimtelijkeplannen.nl/afnemers2012/services'
        
        filter = '"plangebied"=\'' + plangebied + '\''
        layers = [ \
        {u'name': u'app:Functieaanduiding', u'qml': 'functieaanduiding_digitaal.qml'}, \
        {u'name': u'app:Maatvoering', u'qml': 'maatvoering_digitaal.qml'}, \
        {u'name': u'app:Bouwaanduiding', u'qml': 'bouwaanduiding_imro_qgis.qml'}, \
        {u'name': u'app:Bouwvlak', u'qml': 'bouwvlak_digitaal.qml'}, \
        {u'name': u'app:Dubbelbestemming', u'qml': 'dubbelbestemming_digitaal.qml'}, \
        {u'name': u'app:Enkelbestemming', u'qml': 'enkelbestemming_imro_qgis.qml'}, \
        {u'name': u'app:Bestemmingsplangebied', u'qml': 'bestemmingsplangebied_imro_qgis.qml'}, \
        ]
        
        root = QgsProject.instance().layerTreeRoot()
        bpName = plangebied
        bpGroup = root.insertGroup(0, bpName)
    
        for layer in layers:
            vlayer = self.getWfsLayer(service, layer[u'name'], filter)
            if vlayer.isValid():
                plugin_dir = os.path.dirname(os.path.abspath(__file__)) + '/styles'
                layerQml = os.path.join(plugin_dir,layer[u'qml'])
                vlayer.loadNamedStyle(layerQml)
                QgsMapLayerRegistry.instance().addMapLayer(vlayer, False)
                node_vlayer = bpGroup.addLayer(vlayer)
            else:
                print 'invalid layer'
                
        vlayer.selectAll()
        canvas = self.iface.mapCanvas()
        canvas.zoomToSelected(vlayer)
        vlayer.removeSelection()

    def addSourceRow(self, serviceLayer):
        if serviceLayer["tabFilter"] == 'JURIDISCH':
            layerId = QStandardItem(serviceLayer["identificatie"])
            layernaam = QStandardItem(serviceLayer["naam"])
            
            self.sourceModel.appendRow( [ layerId, layernaam ] )

    def filterBestemmingsplannen(self):
        search_string = self.dlg.lineEdit_id.text();
        print(search_string)
        if len(search_string) > 0:
            self.dlg.treeView_results.selectRow(0)
            self.sourceModel.clear()

            url = "http://www.ruimtelijkeplannen.nl/web-roo/rest/search/plannen/id/" + search_string
            response = urllib.urlopen(url)
            self.pdok = json.loads(response.read())
                
            print len(self.pdok["idns"])
            for service in self.pdok["idns"]:
                itemLayername = QStandardItem(service)
                self.sourceModel.appendRow(itemLayername)

            self.sourceModel.setHeaderData(0, Qt.Horizontal, "Bestemmingsplan")
            self.sourceModel.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
            self.sourceModel.setHeaderData(1, Qt.Horizontal, "Naam")
            self.dlg.treeView_results.resizeColumnsToContents()
            self.dlg.treeView_results.selectRow(0)

    def loadBestemmingsplan(self, index):
        self.dlg.hide()
        self.addBestemmingsplan(index.data())
        self.dlg.lineEdit_id.clear()
        

    def getBestemmingsplannenByAddress(self):
        addresses = self.geolocator.search(self.dlg.lineEdit_address.text())
        if len(addresses) > 0:
            address = addresses[0];
            address_loc = address['centroide_rd']
            geom = QgsGeometry.fromWkt(address_loc)
            x = geom.asPoint().x()
            y = geom.asPoint().y()

            self.sourceModel.clear()
            url = "http://www.ruimtelijkeplannen.nl/web-roo/rest/search/plannen/xy/" + str(x) + "/" + str(y)
            response = urllib.urlopen(url)
            self.pdok = json.loads(response.read())

            for service in self.pdok["plannen"]:
                self.addSourceRow(service)

            self.sourceModel.setHeaderData(0, Qt.Horizontal, "Bestemmingsplan")
            self.sourceModel.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
            self.sourceModel.setHeaderData(1, Qt.Horizontal, "Naam")
            self.dlg.treeView_results.resizeColumnsToContents()
            self.dlg.treeView_results.horizontalHeader().setResizeMode(1, QHeaderView.Stretch)
            self.dlg.treeView_results.selectRow(0)
        else:
            QMessageBox.warning(self.iface.mainWindow(), "Bestemmingsplan", ( \
                "Niets gevonden. Probeer een andere spelling of alleen postcode/huisnummer."
                ), QMessageBox.Ok, QMessageBox.Ok)
