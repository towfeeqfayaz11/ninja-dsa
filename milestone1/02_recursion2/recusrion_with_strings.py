# given a string , replace all occurance of 'a' with 'b'. Since string is immutable datatype, so we will be creating a new string in each iteration call

def replace_a_with_b(s: str) -> str:
    if len(s) == 0:
        return ""
    smallOutput = replace_a_with_b(s[1:])
    if s[0] == 'a':
        return 'b'+smallOutput
    else:
        return s[0]+smallOutput

if __name__ == "__main__":
    s = input()
    ans = replace_a_with_b(s)
    print(ans)

# **************************************************************************

# given a string , replace all occurance of c1 with c2. Since string is immutable datatype, so we will be creating a new string in eahc iteration call

def replace_a_with_b(s: str, c1: str, c2: str) -> str:       # replace all occurances of c1 with c2
    if len(s) == 0:
        return ""
    smallOutput = replace_a_with_b(s[1:],c1,c2)
    if s[0] == c1:
        return c2+smallOutput
    else:
        return s[0]+smallOutput

if __name__ == "__main__":
    s = input()
    ans = replace_a_with_b(s,'c','x')
    print(ans)