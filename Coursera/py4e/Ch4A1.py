# Rewrite your pay computation with time-and-a-half for overtime and create a
# function called computepay which takes two parameters (hours and rate).

def computepay(hrs,rate):
    pay = hrs*rate
    if hrs > 40:
        ehrs = hrs-40
        erate = rate*1.5
        pay = (40*rate)+(ehrs*erate)
    return pay
hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
print('Pay',computepay(hrs,rate) )
