#For any function call at a given stage: T(N, beg,aux,end), we have to make three sub calls

# 1> T(N-1, beg, end, aux)       --> move top N-1 disks from beg to aux peg
# 2> T(1, beg, aux, end)         --> move disk 1 from beg to end peg
# 3> T(N-1, aux, beg, end)       --> move N-1 disks from aux to end peg


# solution 1
def towerofhanoi(n, source, aux, dest):
    # Please add your code here
    if n == 1:
        print(source,dest)
        return
    towerofhanoi(n-1, source, dest, aux)          # move n-1 from source to auxillary
    print(source,dest)                            # move 1 from source to destination
    towerofhanoi(n-1, aux, source, dest)          # move n-1 from auxillary to destination

n=int(input())
towerofhanoi(n, 'a', 'b', 'c')

# ------------------------------------------------------------------------------------------

# solution 2
def towerofhanoi(n, source, aux, dest):
    # Please add your code here
    if n == 1:
        print(source,dest)
        return
    towerofhanoi(n-1, source, dest, aux)          # move n-1 from source to auxillary
    towerofhanoi(1, source, aux, dest)            # move 1 from source to destination
    towerofhanoi(n-1, aux, source, dest)          # move n-1 from auxillary to destination

n=int(input())
towerofhanoi(n, 'a', 'b', 'c')

# ------------------------------------------------------------------------------------------

# solution 3
def towerofhanoi(n, source, aux, dest):
    # Please add your code here
    if n <= 0:                                     # covers all the base cases
        return
    towerofhanoi(n-1, source, dest, aux)           # move n-1 from source to auxillary
    print(source, dest)                            # move 1 from source to destination
    towerofhanoi(n-1, aux, source, dest)           # move n-1 from auxillary to destination

n=int(input())
towerofhanoi(n, 'a', 'b', 'c')


# ------------------------------------------------------------------------------------------

# solution 4:
def towerofhanoi(n, source, aux, dest):
    # Please add your code here
    if n == 0:
        return
    towerofhanoi(n-1, source,dest,aux)
    print(source,dest)
    towerofhanoi(n-1, aux,source,dest)
    

n=int(input())
towerofhanoi(n, 'a', 'b', 'c')