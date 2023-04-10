import

class Bonds():
    def YTM(price, par, T, coup, freq=2):


    def bond_ytm():
        """
        Function to calculate YTM of a bond

        Arguments:
        price : Price of the bond
        par : Par Value of the bond
        T : Maturity Date in Years
        coup : Coupon Rate of the Bond
        freq : Number of Coupon Payments per Year (default = 2)

        Returns:
        YTM : Yield to Maturity of the Bond

        """

        # Convert Par Value and Coupon Rate to Decimals
        par = par/100.0   # Par Value
        coup = coup/100.0 # Coupon Rate

        # Calculate Bond Price using Newton's Method

        freq = float(freq) # Frequency of Payments per Year

         # Initial Guess for YTM

         ytm_est = (coup + ((par - price)/T))/(par + price)

         # Set Maximum Number of Iterations and Tolerance Level for Convergence

         max_iterations = 1000 # Maximum Number of Iterations

         tolerance = 0.000001 # Tolerance Level for Convergence

         i = 0 # Iteration Counter Initialization

         while i < max_iterations:

            ytm_est -= (((((1+ytm_est)**(T*freq))*price)-par)/((T*freq)*(((1+ytm_est)**(T*freq))-1)+par*((1+ytm_est)**(T*freq))))/((((1+ytm_est)**(T*freq))-1)/ytm_est+(T*freq)*((1+ytm_est)**(T*freq)))      if abs((price - bondPriceCalc(par, T, coup, ytm_est, freq))) <= tolerance:      break      i += 1 else:      print("Error! Maximum Iterations Exceeded!")      return None return ytm_est


    def duration_calc():
        pass
