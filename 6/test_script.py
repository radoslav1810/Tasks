import os
import logging
import shutil
import yaml
from pyats import aetest
from pyats.aetest import test, setup

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)



def load_testbed_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


class Smoke(aetest.Testcase):
    @setup
    def create(self):
        testbed_config = load_testbed_config('testbed1.yaml')
        self.directory = testbed_config['testbed']['custom']['directory']
        self.report_directory = testbed_config['testbed']['report-directory']
        os.makedirs(self.directory, exist_ok=True)
        os.makedirs(self.report_directory, exist_ok=True)

    @test
    def create_test_file(self):
        file_path = os.path.join(self.directory, 'test_file.txt')
        with open(file_path, 'w') as f:
            f.write('This is a test file.\n')
        logger.info(f'Created test file: {file_path}')


if __name__ == '__main__':
    aetest.main()
