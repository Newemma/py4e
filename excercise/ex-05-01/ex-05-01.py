total = 0
count = 0
while True:
    x = input('Enter a number: ')
    if x == 'done':
        break
    try:
        x = float(x)
    except:
        print('Error, Invalid input')
        continue
    #print('Enter a number: ', x)
    count = count + 1
    total = total + x
    #print(count, total)

print('total:',total, 'count:',count, 'average:',total/count)


#continue and break only in loop
