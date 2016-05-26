# Problem 2-1: Paying the Minimum
# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
# Answer should not specify the values for the variables balance, annualInterestRate, or monthlyPaymentRate - our test code will define those values before testing your submission

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
term = 12 # set term to 1 year -> 12 months
ub = balance  # at beginning remaingbal = intial monthly balance
totalp = 0
for month in range(term):
    payment = monthlyPaymentRate * balance
    totalp += payment
    ub = balance - payment
    balance = ub + (annualInterestRate / 12.00) * ub
    print 'Month: ' + str(month + 1)
    print 'Minimum monthly payment: ' + str(round(payment,2))
    print 'Remaining Balance is '+ str(round(balance,2))
print 'Total paid: ' + str(round(totalp,2))
print 'Remaining Balance is '+ str(round(balance,2))

# Problem 2-2: Paying Debt Off in a Year
# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
# Answer should not specify the values for the variables balance or annualInterestRate - our test code will define those values before testing your submission.

term = 12
initbal = balance #save initial balance
ub = balance  # at beginning remaining bal = intial monthly balance
payment = 0.00
n = 1
for n in range(1,balance):
    payment = n * 10
    balance = initbal
    for month in range(term):
        ub = balance - payment
        balance = ub + (annualInterestRate / 12.00) * ub
    if balance <= 0:
        break
print 'Lowest Payment: '+str(payment)

# Problem 2-3: Using Bisection Search to Make the Program Faster
# Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year.
# Answer should not specify the values for the variables balance or annualInterestRate - our test code will define those values before testing your submission.

def findbal(payment, balance, r, term):
    for month in range(term):
        ub = balance - payment
        balance = ub + (r / 12.00) * ub
    return balance

term = 12
initbal = balance #save initial balance
ub = balance  # at beginning remaining bal = intial monthly balance
upper = findbal(0, balance, annualInterestRate, term)
lower = initbal / 12
payment = 0.00
while (True):
    balance = initbal  #reset
    payment = (upper + lower) / 2.0   
    balance = findbal(payment, balance, annualInterestRate, term)
    if (round(balance,2) > 0.01):
        lower = payment
    elif (round(balance,2) < -0.01):
        upper = payment
    else:
        break
print 'Lowest Payment: '+str(round(payment,2))
