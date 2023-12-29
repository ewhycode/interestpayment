# collect necessary inputs: principal, apr, years
# calculate monthly payment
# show to the user

def main(): 
    print("Monthly Payment Loan Calculator")
    print("")

    principal = float(input("Enter the loan amount: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Enter total number of years of loan: "))

    monthlyInterestRate = apr / 1200
    totalMonths = years * 12
    monthlyPayment = principal * monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** (-totalMonths))

    print(" The monthly payment for this loan is: %.2f " % monthlyPayment)

main()