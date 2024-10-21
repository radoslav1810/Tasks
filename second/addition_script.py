from pyats import aetest

class AdditionTest(aetest.Testcase):

    @aetest.setup
    def setup(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @aetest.test
    def addition(self):
        result = self.num1 + self.num2
        if 0 > result:
            self.failed(f"Addition test failed: result ,because result  is less than 0 : {result}")
        else:
            self.passed(f"Addition test passed ")

if __name__ == '__main__':
    aetest.main()
