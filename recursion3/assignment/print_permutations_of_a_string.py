# Print Permutations of a String

# Given a string, find and print all the possible permutations of the input string.
# Note : The order of permutations are not important. Just print them in different lines.
# Sample Input :
# abc
# Sample Output :
# abc
# acb
# bac
# bca
# cab
# cba

# ---------------------------------------------------------------------

# solution

def printPermutations(string,res):
    #Implement Your Code Here
    if len(string) == 0:
        print(res)
        return
    for i in range(len(string)):
        out = res+string[i]
        printPermutations(string[:i]+string[i+1:],out)
    
    
# main
string = input()
printPermutations(string,"")