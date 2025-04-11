number=int(input("Enter the number:"))
last_first=0
last_second=1
print(f'{last_first}\n{last_second}')
# print(last_first , last_second)
for i in range(number-2):
    fibnacci=last_first+last_second
    print(fibnacci)
    last_first=last_second
    last_second=fibnacci