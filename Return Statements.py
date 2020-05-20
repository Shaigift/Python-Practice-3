

def  cube(num):
    return num*num*num

result = cube(4)
print(result)



def  cube(num):
    return num*num*num

print(cube(4))


def  cube(num):  ##After return block code , python will stop runnning.
    return num*num*num
    print("code")
print(cube(4))




def add_numbers(num1, num2=99):
     return num1 + num2

sum = add_numbers(4, 3)
print(sum)


