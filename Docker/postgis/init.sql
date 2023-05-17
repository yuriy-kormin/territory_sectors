CREATE database sectors;
CREATE user sectors with password 'sectors';
ALTER database sectors owner to sectors;
CREATE EXTENSION postgis;
ALTER ROLE sectors SUPERUSER;