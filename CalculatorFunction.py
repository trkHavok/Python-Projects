def addition(num_1, num_2):
    answer = num_1 + num_2
    return answer

def subtract(num_1, num_2):
     answer = num_1 - num_2
     return answer

def divide(num_1, num_2):
     answer = num_1 / num_2
     return answer

def multiply(num_1, num_2):
     answer = num_1 * num_2
     return answer

value_1 = int(input("First number: "))
value_2 = int(input("Second number: "))


print(value_1,"+",value_2, "is equal to:", addition(value_1,value_2))
print(value_1,"-",value_2, "is equal to:", subtract(value_1,value_2))
print(value_1,"/",value_2, "is equal to:", divide(value_1,value_2))
print(value_1,"*",value_2, "is equal to:", multiply(value_1,value_2))

