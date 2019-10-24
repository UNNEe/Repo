def sub_2for(string):
    lenp = len(string)
    for n in range(lenp):
        for p in range(n,lenp+1):
            if string[n:p] != "":
                print(string[n:p])


def sub_1for(string):
    lenp = len(string)
    n = 0
    p = 0
    while n < lenp +1:
        if p == lenp:
            n+= 1
            p = n
        p+= 1
        if string[n:p] != "": print(string[n:p])


def sub_rec(string,lenp,n=0,p=0):
    if n > lenp:
        return None
    if p > lenp:
        sub_rec(string,lenp,n+1,n)
        return None

    if string[n:p] != "" :print(string[n:p])
    sub_rec(string,lenp,n,p+1)


s = "Paula"
# sub_1for(s)
# sub_2for(s)
sub_rec(s,len(s))