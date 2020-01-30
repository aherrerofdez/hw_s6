num = input("Enter a number: ")

i = -1
for n in num:
    if n != num[i]:
        print("The number provided is not a palindrome")
        break
    else:
        i -= 1
        if (i * (-1)) > (int(len(num) / 2)):
            print("The number provided is a palindrome")
            break
