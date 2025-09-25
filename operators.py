def calculator(a,b,operator):
    if  operator == "+" :
        print(a+b)
    elif operator == "-" :
        print(a-b)
    elif operator == "*" :
        print(a*b)
    elif operator == "/" :
        print(a/b)
    else:
        print("invalid operator")
while True:
     a=int(input("enter the first num a:"))
     b=int(input("enter the second num b:"))
     operator=input("enter operator(+,-,*,/):")
     
     print("result:",calculator(a,b,operator))

     again = input(" you calculate again? (yes/no): ").lower()
     if again != "yes":
        print("Exiting calculator.")
        break
     