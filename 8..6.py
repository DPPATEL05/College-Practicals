def bank():
    ln = eval(input("Enter loan amount: "))
    n = eval(input("Enter number of months: "))
    ir = eval(input("Enter annual interest rate: "))
    r= ir/12
    EMI = ln * (r/100) * (((1 + (r/100))**n)/(((1 + (r/100))**n - 1)))
    print(EMI)
    TP = ln*(1+(r/100))**n
    print(TP)
bank()