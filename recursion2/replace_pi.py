# given a string replace all occurances of "pi" with "3.14"


# solution 1:
def replace_pi(s: str) -> str:
    if len(s) == 1 or len(s) == 0:
        return s
    smallOutput = replace_pi(s[1:])
    if s[0]+smallOutput[0] == "pi":
        return "3.14"+smallOutput[1:]
    return s[0]+smallOutput

if __name__ == "__main__":
    s = input()
    ans = replace_pi(s)
    print(ans)





# solution 2:
def replace_pi(s: str) -> str:
    if len(s) == 1 or len(s) == 0:
        return s
    if s[0:2] == "pi":
    	smallOutput = replace_pi(s[2:])
    	return "3.14"+smallOutput
    else:
    	smallOutput = replace_pi(s[1:])
    	return s[0]+smallOutput

if __name__ == "__main__":
    s = input()
    ans = replace_pi(s)
    print(ans)