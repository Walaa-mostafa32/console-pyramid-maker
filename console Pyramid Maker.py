# console Pyramid Maker 

pyramid_type = input("Enter the pyramid type:")

n = int(input("Enter the number of layers:" ))

if pyramid_type == "right" :

    for i in range (n) :
        print( )
        
        for j in range (i+1) :
            print("* ", end="")

elif  pyramid_type == "isosceles" :
    for i in range(n):

        for j in range(n - i - 1):
            print(" ", end="")

        for j in range(2 * i + 1):
            print("*", end="")

        print()
        
else :
    print("Exit")
