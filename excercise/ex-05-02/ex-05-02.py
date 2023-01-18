largest = None
smallest = None
#count = 0
while True:
    x = input('Enter a number: ')
    if x == 'done':
        break
    try:
        x = int(x)
    except:
        print('Invalid input')
        continue
    #print('Enter a number: ', x)
    #count = count + 1
    if largest is None:
        largest = x
    if x > largest:
        largest = x
    if smallest is None:
        smallest = x
    if x < smallest:
        smallest = x
    #print(smallest)

print('Maximum is',largest)
print('Minimum is',smallest)


#continue and break only in loop
