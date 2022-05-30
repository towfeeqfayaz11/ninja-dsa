def fact(n: int) -> int:
	if n == 0:                      # base case
		return 1

	smallOutput = fact(n-1)         # inductionhypotheses
	output = n*smallOutput          # induction step

	return output

# NOTE: based on usecase and deemand of different questions, the order of hypotheses step and induction step can be reversed

if __name__ == "__main__":
	n = int(input())
	res = fact(n)
	print(res)