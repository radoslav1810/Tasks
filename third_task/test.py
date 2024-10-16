import os
from pyats import aetest
from pyats.topology import loader
from pyats.aetest import Testcase
from pyats.utils.fileutils import FileUtils


class TransferFile(Testcase):

    @aetest.setup
    def setup(self):
        tb = loader.load('testbed.yml')
        self.vm = tb.devices['radi']
        self.vm.connect()
        self.fileutil = FileUtils(testbed=tb)


    @aetest.test
    def file_from_local_to_vm(self):
        local_file = '/Users/radoslav/Desktop/Test/test.txt'
        remote_file = '/home/radi2/transfer'
        self.fileutil.copyfile(source=local_file,destination=remote_file,device=self.vm)
        output = self.device.execute(f'ls {remote_file}')
        if "No such file" in output:
            self.failed(f"File {local_file} was not copied to {remote_file}.")
        else:
            self.passed(f"File {local_file} successfully copied to {remote_file}.")

    @aetest.cleanup
    def cleanup(self):
        """
        Cleanup function to disconnect from the VM
        """
        self.vm.disconnect()


if __name__ == '__main__':

    aetest.main()







