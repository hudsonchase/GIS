 import math
gather the parameters from the user
balance = float(input("Enter the initial balance: "))
intrate = float(input("enter the annual interest rate: "))/100
yr = int(input("Enter the number of years for deposit: "))

compute the balance over the specified time period
for i in range(1,yr+1):
    balance= balance * intrate + balance      #balance accumulator
    print("After {0:d} years the balance will be {1:10.2f}".format(i, balance)) //

def interest (balance, intrate, yr):
    for i in range(1,yr+1):
        balanced = balance * intrate + balance      #balance accumulator
        print("After {0:d} years the balance will be {1:10.2f}".format(i, balanced))

interest(1000, 2.5, 10)

