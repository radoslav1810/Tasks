

from pyats import aetest

class MultiplicationTest(aetest.Testcase):

    @aetest.setup
    def setup(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @aetest.test
    def multiplication_test(self):
        result = self.num1 * self.num2
        if result < 0:
            self.failed(f"Multiplication test failed,because result is less than 0 - {result}")
        else:
            self.passed("Multiplication test passed")


if __name__ == '__main__':
    aetest.main()