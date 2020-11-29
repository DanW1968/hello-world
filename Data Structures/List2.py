#2 ways to calculate an average
# one adds up total as it goes
#one uses a list

total = 0
count = 0
while True:
    inp = input('Enter a Number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print('Average : ', average)

numlist = list()
while True:
    inp = input('Enter a Number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)