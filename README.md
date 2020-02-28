# RuimtelijkePlannen #

QGIS plugin for Dutch spatial or zoning plans.

## Gebruik ##

Na installatie verschijnt de plugin in een werkbalk en in het web-menu van QGIS.

De kaartlagen worden toegevoegd vanuit de Web Feature Service (WFS) van het koppelvlak van [ruimtelijkeplannen.nl](https://ruimtelijkeplannen.nl). Dit betekent dat u de beschikking heeft over alle data die u verder zelf kunt opmaken of gebruiken voor analyses.

### Plan toevoegen middels klikken in de kaart ###
Door eerst het `RP` icoontje aan te klikken en daarna in de kaart te klikken verschijnt een lijst met plannen. Dit zijn alle plannen die NIET behoren tot een van de volgende typen:

  - amvb
  - provinciale verordening
  - regeling
  - structuurvisie

De plannen worden getoond op volgorde van belangrijkheid zoals bij de keuzehulp van [ruimtelijkeplannen.nl](https://ruimtelijkeplannen.nl). Aan de status kolom van de lijst is een *tooltip* toegevoegd, waarin de uitleg van de keuzehulp is opgenomen.

Middels dubbelklikken op een van de regels in de lijst wordt het plan vervolgens toegevoegd aan het QGIS project.

### Plan toevoegen middels IMRO-idn ###

Indien het IMRO-idn van een plan bekend is kan dit ook direct worden ingevuld in de werkbalk van de plugin (rechts naast het `RP` icoontje).

Indien het plan inderdaad bestaat en wordt ondersteund, dan wordt het vervolgens toegevoegd aan het project.

### Doorklikken naar teksten ###

Aan elke laag is door de plugin ook een zogenaamde 'actie' gekoppeld. Door eerst bij het QGIS action-knopje (rechts naast het identify-knopje) de actie 'Open text link(s) in browser' te kiezen en daarna een object in een toegevoegd plan aan te klikken worden alle gekoppelde documenten in de velden 'verwijzingNaarText' of 'verwijzingNaarObjectgerichteText' geopend in uw webbrowser. 
**Let op:** dit kunnen er soms veel zijn!

## OpenSource en Doorontwikkeling ##

Dit project is een OpenSource project, waarbij verschillende partijen hebben bijgedragen aan de ontwikkeling:

  - [Provincie Zeeland](https://www.zeeland.nl) zorgde voor de eerste versie in QGIS2 en QGIS3.
  - [LBP|SIGHT](https://www.lbpsight.nl/) financierde de uitbreiding van de plantypen, het gebruik van meerdere stijlen en de integratie van de keuzehulp.
  - [LandGoed](https://landgoed.it/) sponsort de help functionaleit en het fixen van bugs.
  - [OpenGeoGroep](https://opengeogroep.nl/) zorgt voor het beheer van de plugin in de QGIS plugins repository.



Verdere doorontwikkelingen zijn welkom. Enkele suggesties:

Nu de mogelijkheid bestaat om uit meerdere stijlen te kiezen (een voor print en een voor scherm) zou het mooi zijn om ook andere stijlen toe te voegen. In de help staat uitgelegd  hoe.

De niet ondersteunde plantypes 'amvb', 'provinciale verordening', 'regeling', 'structuurvisie' zijn niet eenvoudig te verbeelden vanuit de data. Hiervoor zou het zinnig kunnen zijn om de services uit het koppelvlak van ruimtelijkeplannen die de plannen correct verbeelden in deze plugin te betrekken.

Voor alle doorintwikkeling geldt dat pull requests zeer welkom zijn. Daarnaast zijn [LandGoed](https://landgoed.it/) en [OpenGeoGroep](https://opengeogroep.nl/) bereid vragen te beantwoorden en mee te denken.
