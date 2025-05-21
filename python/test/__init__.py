from decades import  calculate_age

#age = int(input("Age : "))

#calculate_age(age)

[print(x) for x in range(0, 10) if x % 2== 0]


for x in filter(lambda x: x % 2 == 0, range(0, 10)) :
    print(x)