import os
from pyats import aetest
from pyats.topology import loader
from pyats.aetest import Testcase

class FileTransferTest(Testcase):

    @aetest.setup
    def setup(self):
        tb = loader.load('testbed.yml')
        device = tb.devices['radi']
        device.connect()

    @aetest.test
    def test_copy_file_to_vm(self):

        local_file = '/Users/radoslav/Desktop/Test/test.txt'
        remote_file = '/home/radi2/transfer'  #


        if not os.path.exists(local_file):
            self.failed(f"Local file {local_file} does not exist.")


        result = self.device.execute(
            f'scp {local_file} {self.device.credentials.default.username}@{self.device.connections.cli.ip}:{remote_file}')

        if 'No such file' in result:
            self.failed(f"Failed to copy the file to VM: {result}")
        else:
            self.passed(f"File {local_file} successfully copied to {remote_file} on VM.")

    @aetest.cleanup
    def cleanup(self):
        self.device.disconnect()


# Main to trigger the test
if __name__ == '__main__':
    # Load the testbed and execute the test script
    aetest.main()
