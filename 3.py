# Problem no 3 : Reverse a number using recursive function
def reverse_number(num,r):
    if (num == 0):
        return r
    else:
        r = r * 10 + (num % 10)
        num = num // 10
        return reverse_number(num,r)

num = int(input("Enter a number:"))
result = reverse_number(num,r=0)
print("Reverse number:",result)