import datetime
date=input("Enter date in DD/MM/YYYY format: ")
format = '%d/%m/%Y'
for i in date:
    # convert from string format to datetime format
    # and get the date
    print(datetime.datetime.strptime(i, format).date())