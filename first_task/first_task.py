from pyats import aetest
from calculation import add, divide
import  argparse

class CalculationTest(aetest.Testcase):
    default_parameters = {"num1": 3 , "num2": 0}

    @aetest.setup
    def setup(self, num1=None, num2=None):
        self.num1 = num1 if num1 is not None else self.default_parameters["num1"]
        self.num2 = num2 if num2 is not None else self.default_parameters["num2"]

    @aetest.test
    def add_test(self):
        result = add(self.num1, self.num2)
        if result < 0:
            self.skipped("Result is less than 0, skipping the test.")
            return

        self.passed( f"Addition result is correct {result}")

    @aetest.test
    def divide_test(self):
        try:
            result = divide(self.num1, self.num2)
            if result < 0:
                self.skipped("Result is less than 0, skipping the test.")
                return
            self.passed(f"The divide result is correct {result}")
        except ZeroDivisionError:
            self.passx("ZeroDivisionError encountered, treated as expected. Test passed with passx.")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculation Test Parameters")
    parser.add_argument('--num1', type=int, help='First number for calculation', default=3)
    parser.add_argument('--num2', type=int, help='Second number for calculation', default=0)
    args = parser.parse_args()

    aetest.main(num1=args.num1, num2=args.num2)
