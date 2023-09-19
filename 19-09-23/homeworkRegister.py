class boy:
    name : str = ""
    email : str = ""
    homework : bool = False

boys = []
detention = []

def getBoyDetails():
    b = boy()
    boy.name = input("Boy Name: ")
    boy.email = input("Email: ")
    if input("Has done homework") == "true" :
        boy.homework = True 
    else:
        boy.homework = False
    return b

done = False 
while (done == False):
    boys.append(getBoyDetails())
    if input("Are You Done?") == "true" :
        done = True 
    else:
        done = False

for b in boys:
    if b.homework == False:
        detention.append(b)

print(f'Done Homework: {len(boys)-len(detention)}')
print(f'Not Done Homework: {len(detention)}')

print(detention)




# len(list)
# list.len()
# list.lenth()
