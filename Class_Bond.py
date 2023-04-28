import numpy as np
from typing import Any
from scipy import optimize


class Coupon_Bonds():
    def get_price(self, coupon: float, face_value: float, int_rate: float, years: int, freq: int = 2) -> float:
        total_coupons_pv = self.get_coupons_pv(coupon, int_rate, years, freq)
        face_value_pv = self.get_face_value_pv(face_value, int_rate, years)
        result = total_coupons_pv + face_value_pv
        return result

    @staticmethod
    def get_face_value_pv(face_value: float, int_rate: float, years: int) -> float:
        face_value_pv = face_value / (1 + int_rate) ** years
        return face_value_pv

    def get_coupons_pv(self, coupon: float, int_rate: float, years: int, freq: int = 2) -> float:
        pv = 0
        for period in range(years * freq):
            pv += self.get_coupon_pv(coupon, int_rate, period + 1, freq)
        return pv

    @staticmethod
    def get_coupon_pv(coupon: float, int_rate: float, period: int, freq: int) -> float:
        pv = coupon / (1 + int_rate / freq) ** period
        return pv

    def get_ytm(self, bond_price: Any, face_value: float, coupon: float,
                years: int, freq: int = 2, estimate: float = 0.05) -> float:
        """
        Function to calculate YTM of a bond
        Arguments:
        bond_price (int) - Price of the bond
        face_value (float) - Face Value of the bond
        coupon (float) - Coupon Rate of the Bond
        years (int) - Maturity Date in Years
        freq (int) - Number of Coupon Payments per Year (default = 2)
        Returns:
        get_YTM (float) - Yield to Maturity of the Bond
        """
        get_yield = lambda int_rate: self.get_price(coupon, face_value, int_rate, years, freq) - bond_price
        return optimize.newton(get_yield, estimate)

    def duration_calc(self):
        pass


my_bond = Coupon_Bonds()
ytm = my_bond.get_ytm(bond_price=95.05, face_value=100.0, coupon=5.75, years=2, freq=1)
print(ytm)
