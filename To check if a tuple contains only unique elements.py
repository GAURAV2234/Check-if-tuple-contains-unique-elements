## check if a tuple contains only unique elements

def check_unique_elements(data):
    unique_elements = set(data)
    if len(unique_elements) == len(data):
        return True
    else:
        return False

a=[]
b=int(input("Enter the No. of elements you want to put in list:"))
for i in range(b):
    b=int(input("Enter element"))
    a.append(b)

print("List you entered:",a)
t=tuple(a)


print(t, check_unique_elements(t))

