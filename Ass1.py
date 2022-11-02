la = eval(input("Enter loan amount: "))
mir = eval(input("Enter  monthly interest\
 rate: "))
noy = eval(input("Enter number of years: "))
mp = la * mir/(1-(1/(1+mir)**(noy*2)))
tp = mp*noy*12
print(mp)
print(tp)