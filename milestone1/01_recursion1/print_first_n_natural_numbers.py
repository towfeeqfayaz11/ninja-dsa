# print first n natural numbers from 1 to n
def print_1_to_n(n: int) -> None:
	if n == 0:
		return 
	print_1_to_n(n-1)                        # induction hypotheses step
	print(n,end=' ')                         # here induction step comes after hypotheses



# print first n natural numbers from n to 1
def print_n_to_1(n: int) -> None:
	if n == 0:
		return
	print(n,end=' ')                         # here induction step comes before hypotheses
	print_n_to_1(n-1)                        # induction hypotheses step


if __name__ == "__main__":
	n = int(input())
	print_1_to_n(n)
	print("################################################")
	print_n_to_1(n)
