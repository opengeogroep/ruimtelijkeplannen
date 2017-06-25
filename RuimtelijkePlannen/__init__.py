# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RuimtelijkePlannen
                                 A QGIS plugin
 Plugin for using Dutch online zoning plans from www.ruimtelijkeplannen.nl
                             -------------------
        begin                : 2017-06-25
        copyright            : (C) 2017 by OpenGeoGroep
        email                : info@opengeogroep.nl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load RuimtelijkePlannen class from file RuimtelijkePlannen.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ruimtelijke_plannen import RuimtelijkePlannen
    return RuimtelijkePlannen(iface)
