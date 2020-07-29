income = int(input())
tax_percentage = 0
if 0 <= income <= 15527:
    tax_percentage = 0
    calculated_tax = income * tax_percentage / 100
    print("The tax for {0} is {1}%. That is {2} dollars!".format(income, tax_percentage, "%.0f" % calculated_tax))

else:
    if 15528 <= income <= 42707:
        tax_percentage = 15
    elif 42708 <= income <= 132406:
        tax_percentage = 25
    elif 132407 <= income:
        tax_percentage = 28

    calculated_tax = income * tax_percentage / 100
    print("The tax for {0} is {1}%. That is {2} dollars!".format(income, tax_percentage, "%.0f" % calculated_tax))
