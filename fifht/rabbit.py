import argparse
from pyats import aetest


class SmokeTest(aetest.Testcase):

    @aetest.setup
    def setup(self):
        parser = argparse.ArgumentParser(description='Rabbit Test')
        parser.add_argument('--word', type=str, help='Word to be passed to the job')
        args = parser.parse_args()

        self.word = args.word
        print("Setting up the test")
        print(f"Word provided: {self.word}")

    @aetest.test
    def test_1(self):
        if self.word is None:
            self.failed("Don't provide word")
        print(f'Test #1: {self.word}')

    @aetest.cleanup
    def cleanup(self):
        print("Cleaning up the test")


if __name__ == '__main__':
    aetest.main()
