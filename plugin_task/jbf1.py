from pyats import easypy
from pyats.topology.loader import load

def main(runtime):
    easypy.run(testscript='tr_test.py', runtime=runtime)