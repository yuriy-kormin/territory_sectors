CREATE database IF NOT EXISTS sectors;
CREATE user IF NOT EXISTS sectors with password 'sectors';
ALTER database sectors owner to sectors;
CREATE EXTENSION postgis;
ALTER ROLE sectors SUPERUSER;