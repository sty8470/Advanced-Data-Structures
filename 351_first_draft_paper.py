from math import pow, sqrt
temp = []
#Discerning whether given number is a prime or not
def is_prime(num):
    num = int(num)
    if num == 0:
        return False
    if num == 1:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

#By using indexing of the string, it calculates the whether the sum of consecutive three numbers is a prime number or not
def is_three_digits_sum_prime(i):
    for j in range (len(n)-2):
        seg = int(n[j]) + int(n[j+1]) + int(n[j+2])
        temp.append(seg)
        if is_prime(seg) == False:
            return False
    return True
print(is_three_digits_sum_prime('283002'))
print(temp)
#By using indexing of the string, it calculates the whether the sum of consecutive four numbers is a prime number or not
def is_four_digits_sum_prime(i):
    for j in range(len(n)-3):
        temp[j] = temp[j] + int(n[j+3])
        if is_prime(temp[j]) == False:
            return False
    return True
print(is_four_digits_sum_prime('283002'))
print(temp)


#By using indexing of the string, it calculates the whether the sum of five consecutive numbers is a prime number or not
def is_five_digits_sum_prime(i):
    for i in range(len(i)-4):
        temp[j] = temp[j] + int(i[j+4])
        if is_prime(temp[i]) == False:
            return False
    return True
print(is_five_digits_sum_prime('283002'))
print(temp)s

#Given the input n refering to the number of digits, this function loops through all the possible numbers and check whether they all satisfy above Chole's conditions
def final_digits(n):
    lst = []
    #for i in range(int(pow(10,4)), int(pow(10,n)-1)
    for i in range(int(pow(10,n-1)), int(pow(10,n))):
        i = str(i)
        x = is_three_digits_sum_prime(i)
        y = is_four_digits_sum_prime(i)
        z = is_five_digits_sum_prime(i)
        if x and y and z == True:
            lst.append(i)
        temp[:] = []
    return lst

def main():
    #q is a     
    q = int(input("Enter the number of queries: "))
    for i in range(0,q):
        n = int(input("Enter the number of digits: "))
        print(final_digits(n))

main()
    
            
