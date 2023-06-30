#elif
#used when we have to check multiple conditions.

age=int(input('enter your age'))
if 0<age<=10:
    print('tickets are free')
elif 10<age<=15:
    print('ticket cost is 150 rupees')
elif 15<age<=60:
    print('ticket cost is 400 rupees')
else :
    print('ticket cost is 50 rupees')
