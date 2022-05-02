# sum of series of factorial
def fact(num):
    if (num == 0):
        return 1
    else:
        return(num * fact(num-1))

def sum_of_fact(sum):
    sum = 0
    for i in range(1,num+1):
        sum = sum + fact(i)
    return sum       

num = int(input("Enter a number:"))
result = sum_of_fact(sum)
print("sum of serie of factorial:",result)

