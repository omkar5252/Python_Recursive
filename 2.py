# Problem no 2 : armstrong number using recursive function

def armstrong(num,power):
    if (num == 0):
        return 0
    else:
        return (num % 10)**power + armstrong(num//10,power)

num = int(input("Enter a number:"))
power = len(str(num))
if (num == armstrong(num,power)):
    print(num,"is a armstrong number.")
else:
    print(num,"is not a armstrong number.")