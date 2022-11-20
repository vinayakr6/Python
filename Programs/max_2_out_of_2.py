n1 = int(input("Enter the 1st CIE marks: "))
n2 = int(input("Enter the 2nd CIE marks: "))
n3 = int(input("Enter the 3rd CIE marks: "))

def cie(n1, n2, n3):
    if n1 > n2:
        if n2 > n3:
            total = n1 + n2
            print(n1, 'and', n2, 'maximum')
        else:
            total = n1 + n3
            print(n1, 'and', n3, 'maximum')
    elif n1 > n3:
        total = n1 + n2
        print(n1, 'and', n2, 'maximum')
    else:
        total = n2 + n3
        print(n2, 'and', n3, 'maximum')

    avg = total/2
    print("Averge of Maximum two marks is: ", avg)
    
cie(n1, n2, n3)