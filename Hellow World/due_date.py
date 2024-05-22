print("""Hi User, When is this assignement due?
Please enter all in integer format""")
day, month, year, minn, hours = str(input('What is the day? ')), str(input('What is the month? ')),\
                                str(input('What is the year? ')), str(input('What is time in minutes? ')),\
                                str(input('What is the time in hours? '))
print(f"Module 1 Assignment is due on {month}/{day}/{year} at {hours}:{minn} EST")
