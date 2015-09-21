

def pass_hash(s):
    temp = 0x1505

    for c in s:
        temp = 33 * temp + ord(c)
    return temp

def pass_unhash(t):
    p = ""

    while (t / 33) > 0x1505 + ord('z'):
        t = t - ord('a')
        t = t / 33
        p += "a"

    print p
    print hex(t)


temp = 0x1505
s = " " * 0x200
for c in s:
    temp = (33 * temp + ord(c)) & 0xffffffff
    if (temp > 0xD0000000 and temp < 0xF0000000):
        print hex(temp)
        if (temp == 0xD386D209):
            print "Winner: " + hex(temp)





