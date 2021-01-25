from math import pow, sqrt

#Discerning whether given number is a prime or not
def is_prime(n):
    n = int(n)
    if n == 0:
        return False
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

#By using indexing of the string, it calculates the whether the sum of consecutive three numbers is a prime number or not
def is_three_digits_sum_prime(n):
    for i in range (len(n)-2):
        seg = int(n[i]) + int(n[i+1]) + int(n[i+2])
        if is_prime(seg) == False:
            return False
    return True

#By using indexing of the string, it calculates the whether the sum of consecutive four numbers is a prime number or not
def is_four_digits_sum_prime(n):
    for i in range(len(n)-3):
        seg = int(n[i]) + int(n[i+1]) + int(n[i+2]) + int(n[i+3])
        if is_prime(seg) == False:
            return False
    return True

#By using indexing of the string, it calculates the whether the sum of five consecutive numbers is a prime number or not
def is_five_digits_sum_prime(n):
    for i in range(len(n)-4):
        seg = int(n[i]) + int(n[i+1]) + int(n[i+2]) + int(n[i+3]) + int(n[i+4])
        if is_prime(seg) == False:
            return False
    return True

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
    return lst

def main():
    #q is a     
    q = int(input("Enter the number of queries: "))
    for i in range(0,q):
        n = int(input("Enter the number of digits: "))
        print(final_digits(n))

main()
    
            
