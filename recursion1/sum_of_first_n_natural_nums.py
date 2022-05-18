def find_sum(n: int) -> int:
	if n == 1:                          # natual numbers start from 1
		return 1
	smallOutput = find_sum(n-1)
	output = n + smallOutput
	return output


if __name__ == "__main__":
	n = int(input())
	res = find_sum(n)
	print(res)