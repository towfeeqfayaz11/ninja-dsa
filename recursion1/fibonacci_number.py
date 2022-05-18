# find nth fibonacci number
# fibonacci series: 0 1 1 2 3 5 8 13 ...


def nth_fibonacci(n: int) -> int:
	if n == 1 or n == 2:                       # some questions can have multiple base cases
		return 1

	fib_n_1 = nth_fibonacci(n-1)               # here we have two induction hypotheses
	fib_n_2 = nth_fibonacci(n-2)
	
	output = fib_n_1 + fib_n_2
	return output


