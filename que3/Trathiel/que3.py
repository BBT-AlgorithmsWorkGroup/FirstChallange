number=input("Enter number:")

numbers=list(map(int,number))
count=0
while len(numbers)>1:
    new=1
    for i in numbers:
        new=str(int(new)*int(i))
    numbers=list(map(int,new))
    count+=1
print(count)