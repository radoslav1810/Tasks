from pyats import aetest


class DivisionTest(aetest.Testcase):

    @aetest.setup
    def setup(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @aetest.test
    def division(self):
        if self.num2 == 0:
            self.failed("Division test failed: Division by zero")

        result = self.num1 / self.num2
        if 0 > result:
            self.failed(f"Division test failed: result ,because result is less than 0: {result}")
        else:
            self.passed("Division test passed ")


if __name__ == '__main__':
    aetest.main()
