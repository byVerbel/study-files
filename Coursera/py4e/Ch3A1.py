# Rewrite your pay computation to give the employee 1.5 times the hourly rate
# for hours worked above 40 hours.

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = (hrs*rate)
if hrs > 40:
    ehrs = hrs-40
    erate = rate*1.5
    pay = (40*rate)+(ehrs*erate)
print(pay)
