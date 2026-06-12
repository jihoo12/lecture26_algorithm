# H = (\sum_{i=0}^{l-1} {a_i}{r^i}) mod M
# r= 31
# M = 1234567891

def H(a: str,l):
    arr = []
    for i in a:
        ai = ord(i)
        ri = ai-97
        rir = 31**ri
        air = ord(i)-96
        arr.append(air*rir)
    s = sum(arr)
    h = s % 1234567891
    return(h)

print(H("abcde",5))
