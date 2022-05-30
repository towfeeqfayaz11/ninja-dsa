# bottom up approach is used for returning th eoutput
# top down approach is used for printing the output and also for returning the output

def printFact(n,ans):
	if n == 0:
		print(ans)
		return
	ans = ans * n
	printFact(n-1,ans)



n = int(input())
printFact(n,1)         # passing default value of ans as 1 which is base case value