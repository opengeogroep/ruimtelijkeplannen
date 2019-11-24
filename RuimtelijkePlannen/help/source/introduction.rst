Introduction
************

About
=====

This plug-in is was first developed by Jos Rijborz - Provincie Zeeland (for QGIS2) and Raymond Nijssen - OpenGeoGroep (for QGSI2). The current version was completely rebuild for QGIS3 by Marco Duiker - OpenGeoGroep.

First development and first version for QGIS3 was sponsored by `Provincie Zeeland <https://www.zeeland.nl>`_. Support for more plantypes and multiple styles was funded by `LBP|SIGHT <https://lbpsight.nl>`_. This help and general maintenance is sponsored by `LandGoed <https://landgoed.it>`_.


You will find the plugin in the web menu of QGIS. Furthermore you'll find a RP icon next to a text field on a toolbar.

The plug-in provides a simple way to add a spatial zoning plan (RuimtelijkPlan) to your QGIS project.

Usage
=====

First zoom the map to your area of interest. Then click the RP icon in the RuimtelijkePlannen toolbar, followed by a click in the map. A list of (the supported) spatial zoning plans in that location is shown. Double click one of the plans to add it to the map.

Alternatively you can add a plan with a known IMRO-IDN by typing the IMRO-IDN in the textbox next to the RP icon.

The plan is added from the RuimtelijkePlannen WFS services, so all data is available to you.

Open associated texts
'''''''''''''''''''''

Some object in the map have associated texts. These can be opened by using the action button (this button should be next to the identify button). First choose the action "Open text link(s) in browser" and then click an object in the map which has associated texts. These texts will be opened in a web browser.

**Warning**: This can sometimes open many documents.


Limitations
===========

The following plan types as used by the RuimtelijkePlannen services are supported by this plugin:

 - 'aanwijzingsbesluit',
 - 'beheersverordening',
 - 'bestemmingsplan',
 - 'exploitatieplan',
 - 'gemeentelijk plan; bestemmingsplan artikel 10', 
 - 'gemeentelijk plan; uitwerkingsplan artikel 11',
 - 'gemeentelijk plan; voorbereidingsbesluit',
 - 'gemeentelijk plan; wijzigingsplan artikel 11',
 - 'gemeentelijke visie; overig',
 - 'gerechtelijke uitspraak', 
 - 'inpassingsplan',
 - 'omgevingsvergunning',
 - 'projectbesluit',
 - 'reactieve aanwijzing',
 - 'tijdelijke ontheffing buitenplans',
 - 'uitwerkingsplan',
 - 'voorbereidingsbesluit',
 - 'wijzigingsplan'

The following plan types as used by the RuimtelijkePlannen services are NOT supported by this plugin:

 - 'amvb',
 - 'provinciale verordening',
 - 'regeling',
 - 'structuurvisie'


Settings
========

The settings dialog allows you to select a default style which is applied to the spatial zoning plan when adding it to the project.


Adding styles
'''''''''''''

In the plugin folder you will find a folder named `styles`. Each sub folder in  the folder styles contains a style which can be chosen in the settings dialog. 

To create your own style, copy one of these folders and adapt the style files to your wishes.