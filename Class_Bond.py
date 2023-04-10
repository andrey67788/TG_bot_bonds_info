import numpy as np


class Coupon_Bonds():

    def YTM(self):
        pass

    def duration_count(self, c, y, m, n):
        macaulay_duration = ((1 + y) / (m * y)) - ((1 + y + n * (c - y)) / ((m * c * ((1 + y) ** n - 1)) + m * y))
        modified_duration = macaulay_duration / (1 + y)

        return macaulay_duration, modified_duration


my_bond = Coupon_Bonds()
duration = my_bond.duration_count(c=0.035, y=.04, m=2, n=6)
print(duration)
