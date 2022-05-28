# Return Subsequences

# Given a string (let's say of length n), return all the subsequences of the given string.
# Subsequences contain all the strings of length varying from 0 to n. But the order of characters should remain the same as in the input string.
# Note: The order of subsequences are not important.
# Sample Input:
# abc
# Sample Output:
# "" (the double quotes just signifies an empty string, don't worry about the quotes)
# c 
# b 
# bc 
# a 
# ac 
# ab 
# abc 


# ------------------------------------------------------------------------------
# solution 1:

def getSubsequences(string,ans):
    if len(string) == 0:
        ans.append(string)
        return
    getSubsequences(string[1:],ans)
    temp = ans.copy()           # if using = operator here, it wont create a copy (no new object) but only new reference to same objecct
    for i in range(len(temp)):
        temp[i] = string[0]+temp[i]
    ans.extend(temp)

def subsequences(string):
    #Implement Your Code Here
    ans = []
    getSubsequences(string,ans)
    return ans

string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)

# -----------------------------------------------------------------------------------

# solution 2:

def subs(s):
    if len(s)==0:
        output=[]
        output.append("")
        return output
    smallerString=s[1:]
    smallerOutput=subs(smallerString)
    
    output=[]
    for sub in smallerOutput:
        output.append(sub)
        
    for sub in smallerOutput:
        subs_with_zeroth_char=s[0]+sub
        output.append(subs_with_zeroth_char)
        
    return output


s = input()
ans = subs(string)
for ele in ans:
    print(ele)