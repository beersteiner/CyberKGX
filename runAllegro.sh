#!/usr/bin/env bash

source ./conf.py

cd ${DIR_ALLEGRO}/bin
./agraph-control --config ../lib/agraph.cfg start
./agtool load --overwrite cyberkg ${DIR_CYBER_KG}/CyberKG_Triples.ttl

echo ""
echo "visit http://localhost:10035 and use user: super, password: super"
echo "press Enter to close server"

read __

./agraph-control --config ../lib/agraph.cfg stop
echo "Allegrograph Server stopped."


