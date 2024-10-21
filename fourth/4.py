from turtledemo.clock import setup

from pyats import aetest
import argparse


mapping = {
    'a': (1, 3, 4, 5, 6, 7, 8),
    'b': (0, 2, 3, 4),
    'c': (7, 9, 0, 6, 5, 4, 3, 1),
}


def get_numbers():
    letter = args.letter
    if letter in mapping:
        for number in mapping[letter]:
            yield number


class Test(aetest.Testcase):

    @aetest.setup
    def setup(self):
        self.letter = args.letter
        if self.letter not in mapping:
            self.failed("the test failed")


    @aetest.loop(get_numbers)
    @aetest.test
    def check(self):
        print(f'number: ')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Key letter')
    parser.add_argument('--letter', type=str, help='Character for starting the test')
    args = parser.parse_args()
    aetest.main()