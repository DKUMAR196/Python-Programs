"""
   @ Author - Deepak Kumar
   @ Date - 10-NOV-2021
   @ Time - 20:56
   @ Title  : a. Desc -> Given N distinct Coupon Numbers, how many random numbers do you
             need to generate distinct coupon number? This program simulates this random
             process.
"""

import math
import random

class CoupenNumber:
    @staticmethod
    def randomCoupon():
        i=0
        flag = True
        couponList = []
        noOfCoupon = int(input("How Many Coupons You want to generate...?"))
        while noOfCoupon>=(i+1):
            randomNumber = random.randrange(1,100)
            if (not (couponList.__contains__(randomNumber))):
                couponList.append(randomNumber)
                i += 1
            elif noOfCoupon:
                flag = False
            else:
                print("No contain")
            print(couponList)

coupenNumber = CoupenNumber()
coupenNumber.randomCoupon()
