[![linter-run](https://github.com/yuriy-kormin/territory_sectors/actions/workflows/linter-run.yml/badge.svg)](https://github.com/yuriy-kormin/territory_sectors/actions/workflows/linter-run.yml)
[![test](https://github.com/yuriy-kormin/territory_sectors/actions/workflows/django-test.yml/badge.svg)](https://github.com/yuriy-kormin/territory_sectors/actions/workflows/django-test.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/9c7062dd68f9f445a56e/maintainability)](https://codeclimate.com/github/yuriy-kormin/territory_sectors/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9c7062dd68f9f445a56e/test_coverage)](https://codeclimate.com/github/yuriy-kormin/territory_sectors/test_coverage)

# Territory sector manager

### Project is under construction


This app helps you make marks on the map using markers.

## Logic 

There are apartments, houses, sectors. Each apartment belongs to a house, the houses are grouped into sectors. 

The sector is drawn on the map in the form of a polygon of any shape.

Each house has a gps-tagged address and description. The belonging of the house to some sector is determined by the intersection of the gps-mark and the polygon defining the boundaries of the sector.  


The function INTERSECTS in the special extension for POSTGRESQL is used for this purpose.
