#!/usr/bin/env python

"""
Author: John Stein
Description: Template python script
"""
from __future__ import print_function
from __future__ import print_function
import sys, argparse
#import triplesMap as tm
import conf



PREFIXES = [
    "@prefix rml: <http://semweb.mmlab.be/ns/rml#> .",
    "@prefix rr: <http://www.w3.org/ns/r2rml#> .",
    "@prefix ql: <http://semweb.mmlab.be/ns/ql#> .",
    "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .",
    "@prefix cc: <http://www.ontologyrepository.com/CommonCoreOntologies/> .",
    "@base <http://example.com/ns#>."
]




def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def AddCounter(func):
    def Decorate():
        func()
    Decorate.counter = 0
    return Decorate

@AddCounter
def VulnMap():
    tripleMapName = "<#Vuln " + f"{VulnMap.counter}" + ">"
    



# def main(arguments):

rml = ""

# Parse Arguments
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-m', '--mini', help="Use mini data", default=False, action='store_true')
#parser.add_argument('-o', '--output', help="Output File", default=sys.stdout, type=argparse.FileType('w'))
# args = parser.parse_args(arguments)
args = parser.parse_args(sys.argv[1:])

for i in PREFIXES: rml = rml + i + "\n"

# Gather data sources
dat_srcs = [v for v in dir(conf) if v.startswith('DAT_') and not v.endswith('_MINI')]


for s in dat_srcs:
    s = s + args.mini * '_MINI'
    if s.split('_')[1] == 'CVE':
        eprint('CVE', s, getattr(conf, s))
        # generate all triple maps for CVE documents
    elif s.split('_')[1] == 'CWE':
        eprint('CWE', s, getattr(conf, s))
        # generate all triple maps for CWE document

print(rml)
    # return(rml)



# if __name__ == "__main__":
#     res = main(sys.argv[1:])
#     # sys.exit(main(sys.argv[1:]))