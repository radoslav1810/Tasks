import os
import logging
from pyats import aetest
from pyats.topology import loader

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def load_testbed_config(testbed_file):
    return loader.load(testbed_file)

class Smoke(aetest.Testcase):
    @aetest.setup
    def create(self):
        testbed_config = load_testbed_config('testbed.yaml')
        if not testbed_config:
            self.failed("Failed to load testbed configuration")

        self.directory = testbed_config.custom['directory']
        self.report_directory = testbed_config.custom['report-directory']
        os.makedirs(self.directory, exist_ok=True)
        os.makedirs(self.report_directory, exist_ok=True)
        logger.info(f"Created directories: {self.directory}, {self.report_directory}")

    @aetest.test
    def create_test_file(self):
        file_path = os.path.join(self.directory, 'test_file.txt')
        with open(file_path, 'w') as f:
            f.write('This is a test file for plugin task.\n')
        logger.info(f'Created test file: {file_path}')

if __name__ == '__main__':
    aetest.main()