x = input('Enter Score: ')
try:
    x=float(x)
except:
    print('Error, please enter numberic input between 0.0-1.1')
    quit()

if 0.0 <= x <= 1.0:
    if x>=0.9:
        print('A')
    elif x>=0.8:
        print('B')
    elif x>=0.7:
        print('C')
    elif x>=0.6:
        print('D')
    elif x<0.6:
        print('F')
else:
    print('Error')
