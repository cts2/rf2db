python cleandb ../../rf2service/settings.conf -m 11000160102 -a
python cleandb ../../rf2service/settings.conf
python newmodule -n 1000160 -r 20150601 -c ../../rf2service/settings.conf -v -o CIMI --desc "CIMI Module" CIMIModule
python changeset ../../rf2service/settings.conf -cs CIMIModule -c
