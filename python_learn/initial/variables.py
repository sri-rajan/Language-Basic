# strings
name="sri rajan"

# integers
age = 25

#float
price = 10.99

# boolean
is_correct = True
is_wrong = False

#list
data = [1,2,"a","b"]

#dictionary
obj = {
    "one":1,
    "two":2
}

print(name,type(name))
print(age,type(age))
print(price,type(price))
print(is_correct,type(is_correct))
print(is_wrong,type(is_wrong))
print(data,type(data))
print(obj,type(obj))
print(f"this is price ${price} ")

# typecasting  str() , int(), float(), bool()

print(int(price),"price float to int")
print(str(age),"age int to str")

# string concatanation
print("this is "+"concat")