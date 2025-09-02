import numpy as np

class Test:
    def __init__(self, data):
        self.data = np.array(data)

    def mean(self):
        return np.mean(self.data)

    def median(self):
        return np.median(self.data)

    def std_dev(self):
        return np.std(self.data)