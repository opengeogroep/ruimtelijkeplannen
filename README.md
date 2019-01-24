# RuimtelijkePlannen #

QGIS plugin for Dutch spatial or zoning plans.

## Gebruik ##

Na installatie verschijnt de plugin in een werkbalk en in het web-menu van QGIS.

De kaartlagen worden toegevoegd vanuit de Web Feature Service (WFS) van het koppelvlak van [ruimtelijkeplannen.nl](https://ruimtelijkeplannen.nl). Dit betekent dat u de beschikking heeft over alle data die u verder zelf kunt opmaken of gebruiken voor analyses.

### Plan toevoegen middels klikken in de kaart ###
Door eerst het `RP` icoontje aan te klikken en daarna in de kaart te klikken verschijnt een lijst met plannen. Dit zijn alle plannen die zijn opgenomen op het tabblad "JURIDISCH" van [ruimtelijkeplannen.nl](https://ruimtelijkeplannen.nl).

Middels dubbelklikken op een van de regels in de lijst wordt het plan toegevoegd aan het QGIS project.

### Plan toevoegen middels IMRO-idn ###

Indien het IMRO-idn van een plan bekend is kan dit ook direct worden ingevuld in de werkbalk van de plugin (rechts naast het `RP` icoontje).

Indien het plan inderdaad bestaat en opgenomen is op het tabblad "JURIDISCH' wordt het vervolgens toegevoegd aan het project.

### Doorklikken naar teksten ###

Aan elke laag is door de plugin ook een zogenaamde 'actie' gekoppeld. Door eerst bij het QGIS action-knopje (rechts naast het identify-knopje) de actie 'Open text link(s) in browser' te kiezen en daarna een object in een toegevoegd plan aan te klikken worden alle gekoppelde documenten in de velden 'verwijzingNaarText' of 'verwijzingNaarObjectgerichteText' geopend in uw webbrowser. 
**Let op:** dit kunnen er soms veel zijn!

## Doorontwikkeling ##

Doorontwikkelingen zijn welkom. Enkele suggesties:

De plugin werkt nu alleen voor plannen op het tabblad "JURIDISCH". Uitbreiding naar meer planvormen is zeer welkom. 

Vormvrije plannen als structuurvisies of verordeningen zijn niet eenvoudig te verbeelden vanuit de data. Hiervoor zou het zinnig kunnen zijn om de services uit het koppelvlak van ruimtelijkeplannen die de plannen correct verbeelden in deze plugin te betrekken.

Voor alle doorintwikkeling geldt dat pull requests zeer welkom zijn. Daarnaast is OpenGeoGroep bereid vragen te beantwoorden en mee te denken.
