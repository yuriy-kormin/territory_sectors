[![linter-run](https://github.com/yuriy-kormin/territory_sectors/actions/workflows/linter-run.yml/badge.svg)](https://github.com/yuriy-kormin/territory_sectors/actions/workflows/linter-run.yml)
[![test](https://github.com/yuriy-kormin/territory_sectors/actions/workflows/django-test.yml/badge.svg)](https://github.com/yuriy-kormin/territory_sectors/actions/workflows/django-test.yml)

# Territory sector manager

### Project is under construction


This app helps you make marks on the map using markers.

## Logic 

There are apartments, houses, sectors. Each apartment belongs to a house, the houses are grouped into sectors. 

The sector is drawn on the map in the form of a polygon of any shape.

Each house has a gps-tagged address and description. The belonging of the house to some sector is determined by the intersection of the gps-mark and the polygon defining the boundaries of the sector.  


The function INTERSECTS in the special extension for POSTGRESQL is used for this purpose.


<img width="1000" src="https://user-images.githubusercontent.com/96548294/218972719-42fd95db-46b0-494e-9b7a-bc357d3752e2.png">

Digit inside marker show flat count on this house

## Usability

Adding apartments to houses can be done on the page of the house using the button "add flat"

( Here using javascript a line is added to the table, which is then converted into json when sending the form)


<img width="1000" src="https://user-images.githubusercontent.com/96548294/218972835-e83c3b09-fdda-4b1d-a772-4070243269e5.png">


<img width="1000" src="https://user-images.githubusercontent.com/96548294/218980792-8a48d31b-ca6b-466b-8e87-bcec940f16e1.png">


