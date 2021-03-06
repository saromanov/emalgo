import numpy as np
import logging

class EM:
    def __init__(self, X1, X2):
        self.X1 = X1
        self.X2 = X2

    def fit(self, samples=5, n=10, eps=0.005):
        theta1 = 0.5
        theta2 = 0.6
        err = eps+1
        while (err < eps):
            for i in range(samples):
                sample1 = np.random.binomial(self.X1[i], theta1, n)
                sample2 = np.random.binomial(self.X2[i], theta2, n)
                H1, T1 = self._ML(sample1, n)
                H2, T2 = self._ML(sample2, n)
                value1 = theta1 * H1
                value2 = theta1 * T1
                value3 = theta2 * H2
                value4 = theta2 * T2

                theta1_new = value1/(value1 + value2)
                theta2_new = value3/(value3 + value4)
                err = np.abs(theta1_new - theta1)/theta1
                err2 = np.abs(theta2_new - theta2)/theta2
                logging.info("Error: {0}".format(err))
                theta1, theta2 = theta1_new, theta2_new

    def _ML(self, item, size):
        H = np.where(item == 1)
        return len(H), size - len(H)


