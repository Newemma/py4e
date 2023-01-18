def computepay(h, r):
#print('computepay', h, r )
    if h <= 40:
        xp = h * r
    else:
        xp = 40*r+1.5*(h-40)*r
#print('return', xp)
    return(xp)

def num (a):
    try:
        a = float(a)
    except:
        print('Error, please enter numberic input')
        quit()
    return(a)

xh = input("Enter Hours: ")
xh = num (xh)
xr = input("Enter Rates: ")
xr = num (xr)
#print('number', xh, xr)

p = computepay(xh, xr)
print("Pay", p)
#‘#’：lock checking flag，运行正常之后标#；both of checking and mention；
#ps：print 用于function return之前
