
from pyats.easypy.tasks import run

def main():
    testbed = 'testbed1.yaml'
    run(testscript='test_script.py', testbed=testbed)
    run(testscript='save1.py')

if __name__ == "__main__":

    main()  # Pass runtime as required by your setup
