#var = input("What's your favorite number?")
#a_var = input("What's another number?")
#print(int(var) + int(a_var))
import random
testlst = []
for i in range(1,100): 
    testlst.append(random.sample(range(10000), 2))
def calculator(num1, num2):
    print("Add: ", num1 + num2) 
    print("Subtract: ", num1 - num2) 
    print("Multiply: ", num1 * num2) 
    print("Division: ", num1 / num2) 
for val in testlst: 
    calculator(val[0], val[1])
