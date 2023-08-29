total=0
numbers=[1,2,3,4,5,6,7,8]
numbers.sort(reverse=True)
for x in range(7):
    if (numbers[x]%2)==1:
        print(numbers[x])
        total=total+numbers[x]
print(numbers)


