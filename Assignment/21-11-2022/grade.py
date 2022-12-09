n = int(input("Enter a number: "))

if (n>=75 and n<=100):
    print("Grade A")
elif (n>=60 and n<75):
    print("Grade B")
elif (n>=35 and n<60):
    print("Grade C")
elif (n>=0 and n<35):
    print("Fail")
else:
    print("Invalid Output")
