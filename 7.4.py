temperature = {
    "Monday": 45,
    "Tuesday": 34,
    "Wednesday": 46,
    "Thursday": 34,
    "Friday": 54,
    "Saturday": 32,
    "Sunday": 39
}
for i in temperature:
    if temperature[i]>40 and temperature[i]<50:
        print(i)