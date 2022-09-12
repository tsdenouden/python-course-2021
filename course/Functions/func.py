
"""
General structure of a function:

def FunctionName(Input):
    Action
    return Output
More code

^Not indented = outside of function

"""

def addOne(Number):
    Output = Number + 1
    return Output
#return gives back the value
#can't use Output without return because it's a local var

Var = 0
print(Var)

Var2 = addOne(Var)
Var3 = addOne(Var2)

#hardcoded the number
#calculates the sum first before it calls the function
Var4 = addOne(2.1+3.4)

print(Var2)
print(Var3)
print(Var4)

#A function with 2 inputs
def addOneAddTwo(Number1,Number2):
    Output = Number1 + 1
    #Output = Output + Number2 + 2
    Output += Number2 + 2
    return Output

Sum = addOneAddTwo(Var2,Var3)
print(Sum)
