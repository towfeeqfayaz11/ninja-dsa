# All prime numbers

# Given an integer N, print all the prime numbers that lie in the range 2 to N (both inclusive).
# Print the prime numbers in different lines.

# Input Format :
# Integer N

# Output Format :
# Prime numbers in different lines

# Constraints :
# 1 <= N <= 100

# Sample Input 1:
# 9
# Sample Output 1:
# 2
# 3
# 5
# 7

# Sample Input 2:
# 20
# Sample Output 2:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19

# ************************************************************************************

# solution 1: O(N^2)
def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return
    print(x)

n= int(input())

for i in range(2,n+1):
    isPrime(i)

# ************************************************************************************

# solution 2: O(N*(N)^1/2)
def isPrime(x: int) -> None:
    i = 2
    while i*i <= x:
        if x%i == 0:
            return
        i+=1
    print(x)
        

for i in range(2,int(input())+1):
    if i == 2:
        print(2)
    else:
        isPrime(i)

# ************************************************************************************

# solution 3: Sieve of Eratosthenes
n = int(input())
# Sieve of Eratosthenes
arr = [True]*(n+1)
arr[0],arr[1] = False,False


i = 2
# check only till sqrt(n)
while i*i<=n:
    if arr[i]:           # check if i is prime, if yes, then marking all other multiples of i as non prime
        j=i*2            # j is initialised with first multiple of i
        while j<=n:
            #making all multiples of i as false
            arr[j]=False
            j = j+i
    i+=1
for i,j in enumerate(arr):
    if j:
        print(i)
