rf2db
=====

SNOMED CT RF2 Database Loader and wrapper classes.  This only runs with Python 2.x series and has been tested with
Python 2.6.6

Dependencies:

Cherrypy        3.2.4
MySQL-python    1.2.4
PyXB            1.2.3
Routes          2.0
SQLAlchemy      0.8.4
configparser    3.3.0r2
lxml            3.2.4

When combined with rf2server, you will also need:
py4j            0.8

There are three executables in the bin directory
* generateschema - this compiles rf2db/static/xsd/rf2.xsd into the rf2db/schema directory
* newdb - this can be used to maintain the database configuration variables as well as create the database itself.
          (Note: there is currently a bug in this module such that the "-h" option does not show all of the available
           options.  Use "-?" returns a list of the options.)
* loaddb - database load scripts.
