from pyats import aetest
import argparse


mapping = {
    'a': (1, 3, 4, 5, 6, 7, 8),
    'b': (0, 2, 3, 4),
    'c': (7, 9, 0, 6, 5, 4, 3, 1),
}

class Test(aetest.Testcase):

    @aetest.setup
    def setup(self):
        parser = argparse.ArgumentParser(description='Key letter')
        parser.add_argument('--letter', type=str, help='Character for starting the test')
        args = parser.parse_args()

        if args.letter not in mapping:
            self.failed(f'Letter {args.letter} not found in mapping')

        self.letter = args.letter
        aetest.loop.mark(self.check, number=mapping[args.letter])

    @aetest.test
    def check(self, number):
        print(f'number: {number}')

if __name__ == '__main__':
    aetest.main()