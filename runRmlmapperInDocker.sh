#!/usr/bin/env bash

docker run --rm --user $(id -u):$(id -g) -v /home/john/Projects/CyberKGX:/data rmlmapper:4.9.0 -m mapping_cve_to_CC.ttl -o CyberKG_Triples.ttl
