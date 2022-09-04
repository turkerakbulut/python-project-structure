import pandas as pd


class SampleClass:
    param = str()

    def __init__(self, param) -> None:
        """
        Constructor
        """
        self.param = param

    def write(self):
        print(self.param)
        return self.param
