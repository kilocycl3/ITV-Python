s = input("Enter the email: ")

for i in s:
    
    if i == '@':
        break
    elif(i.isalpha()):
        print(i,end='')
