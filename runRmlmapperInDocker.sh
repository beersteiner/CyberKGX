#!/usr/bin/env bash

cat map_prefixes.ttl map_logicalSource_cve.ttl map_content_cve.ttl > map_all.ttl

docker run --rm --user $(id -u):$(id -g) -v /home/john/Projects/CyberKGX:/data rmlmapper:4.9.0 -m map_all.ttl -o CyberKG_Triples.ttl
