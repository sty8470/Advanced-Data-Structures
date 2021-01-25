from math import pow, sqrt
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

def first_repository():
    dict = {}
    #lookup = [-1] * 1000
    for i in range(10):
        for j in range(10):
            for k in range(10):
                index = str(i) + str(j) + str(k)
                dict[index] = i+j+k
    return dict
                
first_lookup = first_repository()
#print(lookup)

def second_repository():
    dict = {}
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    index = str(i) + str(j) + str(k) + str(l)
                    dict[index] = i+j+k+l
    return dict

second_lookup = second_repository()

def third_repository():
    dict = {}
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        index = str(a) + str(b) + str(c) + str(d) + str(e)
                        dict[index] = a+b+c+d+e
    return dict

third_lookup = third_repository()

#By using indexing of the string, it calculates the whether the sum of consecutive three numbers is a prime number or not
def is_three_digits_sum_prime(n):
    for j in range (len(n)-2):
        seg = n[j:j+3]
        if is_prime(first_lookup[seg]) == False:
            return False
    return True

print(is_three_digits_sum_prime('283002'))
print(is_three_digits_sum_prime('902005'))
print(is_three_digits_sum_prime('101101'))

def is_four_digits_sum_prime(n):
    for j in range(len(n)-3):
        seg = n[j:j+4]
        if is_prime(second_lookup[seg]) == False:
            return False
    return True
print(is_four_digits_sum_prime('283002'))
print(is_four_digits_sum_prime('902005'))
print(is_four_digits_sum_prime('101101'))

def is_five_digits_sum_prime(n):
    for j in range(len(n)-4):
        seg = n[j:j+5]
        if is_prime(third_lookup[seg]) == False:
            return False
    return True
print(is_five_digits_sum_prime('283002'))
print(is_five_digits_sum_prime('902005'))
print(is_five_digits_sum_prime('101101'))


#Given the input n refering to the number of digits, this function loops through all the possible numbers and check whether they all satisfy above Chole's conditions
def final_digits(n):
    if n<5:
        return False
    lst = []
    #for i in range(int(pow(10,4)), int(pow(10,n)-1)
    for i in range(int(pow(10,n-1)), int(pow(10,n))):
        i = str(i)
        x = is_three_digits_sum_prime(i)
        y = is_four_digits_sum_prime(i)
        z = is_five_digits_sum_prime(i)
        if x and y and z == True:
            lst.append(i)
    return len(lst)

def main():
    #q is a     
    q = int(input("Enter the number of queries: "))
    for i in range(0,q):
        n = int(input("Enter the number of digits: "))
        print(final_digits(n))

main()
    
            


