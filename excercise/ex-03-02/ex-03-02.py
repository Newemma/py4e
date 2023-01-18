xh = input('enter hours: ')
#not a numberic input
try:
    xh = float(xh)
except:
    print('Error, please enter numberic input')
    quit()
xr = input('enter rates: ')
try:
    xr = float(xr)
except:
    print('Error, please enter numberic input')
    quit()
#numberic input
xh = float(xh)
xr = float(xr)
if xh >= 40:xp = 40*xr+1.5*(xh-40)*xr
else:
    xp = xh*xr
print('pay:',xp)
