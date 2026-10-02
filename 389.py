def findTheDifference( s: str, t: str) -> str:   
    res=0
    for x in s+t:
        res^=ord(x)
    return chr(res)

'''s = "abcd"
t = "abcde"
print(findTheDifference(s, t))'''