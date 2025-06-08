
print("Welcome to simple calculator\n")
print("\n")
choice = input("do you want to add, subract, multiply or divide? :")


try:
    if choice.lower() == "add":
        while True:
            
                x = input("enter you first number:")
                y = input("enter your second number:")

                if x.isdigit() and y.isdigit():
                     print(int(x)+int(y))
                     break
                
                else:
                     print(f"{x} or {y} is not a valid integer")
    elif choice.lower() == "subtract":
         while True:
            
                x = input("enter you first number:")
                y = input("enter your second number:")

                if x.isdigit() and y.isdigit():
                     print(int(x)-int(y))
                     break
                
                else:
                     print(f"{x} is not a valid integer")
    elif choice.lower() == "multiply":
         while True:
            
                x = input("enter you first number:")
                y = input("enter your second number:")

                if x.isdigit()  and y.isdigit():
                     print(int(x)*(y))
                     break
                
                else:
                     print(f"{x} is not a valid integer")
    elif choice.lower() == "divide":
         while True:
              
              x = input("enter your first number: ")
              y = input("enter you second number: ")

              if x.isdigit() and y.isdigit():
                   print(int(x)/int(y))
                   break
              else:
                   print("not a valid integer")
         
                


            


except Exception as e:
    print (e)

