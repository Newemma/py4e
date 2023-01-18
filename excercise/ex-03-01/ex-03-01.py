xh = input('enter hours: ')
xr = input('enter rates: ')
xh = float(xh)
xr = float(xr)
if xh > 40:
    xp = 40*xr+1.5*(xh-40)*xr
else:
    xp = xh*xr
print('pay:',xp)
