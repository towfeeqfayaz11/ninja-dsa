# Return Permutations of a String

# Given a string, find and return all the possible permutations of the input string.
# Note : The order of permutations are not important.
# Sample Input :
# abc
# Sample Output :
# abc
# acb
# bac
# bca
# cab
# cba

# --------------------------------

# solution
def permutations(string):
    if len(string) == 0:
        return [""]
    output = []
    for i in range(len(string)):
        temp = permutations(string[:i]+string[i+1:])
        
        for j in range(len(temp)):
            output.append(string[i]+temp[j])
    return output
        
    
    


string = input()
ans = permutations(string)
for s in ans:
    print(s)