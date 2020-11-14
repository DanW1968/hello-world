count = 0
sum = 0
print('Before', count, sum)
for  value in [9, 41, 12, 3, 74, 15] :
    count = count+1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)

print('Before')
for  value in [9, 41, 12, 3, 74, 15] :
    if value > 20 :
        print('Large Number', value)
print('After')

found = False
print('Before', found)
for  value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
    print(found, value)
print('After', found)
