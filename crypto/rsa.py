
def tobinary(a):
    d = []
    c = a
    while(c!=0):
        b = c % 2
        c = int(c/2)
        d.append(b)
    return d

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def quickmi(m,e,n):
    f = tobinary(e)
    c = 0
    d = 1
    while(c!=e):
        c = 2*c
        d = (d*d)%n
        g = f.pop()
        if(g ==1):
            c=c+1
            d=(d*m)%n
    return d

def usePrivateKeyToEncrypt(p,q,e,c):
    d = modinv(e, (p - 1) * (q - 1))
    n = p * q
    m = pow(c, d, n)
    return m

def usePublicKeyToDecrypt(n,e,m):
    return quickmi(m,e,n)

def usePrivateKeyToDecrypt(p,q,e,c):
    d = modinv(e, (p - 1) * (q - 1))
    n = p * q
    m = pow(c, d, n)
    return m

def usePublicKeyToEncrypt(n,e,m):
    return quickmi(m,e,n)

p=11293231343323842475435038774986083604136666136515901710207183553485782239451048034576486430365838503866390616010931322669359717835450061373592539700165913

q=13254048923833821809946912408498586088236626098096401455889487063718583580508390254509299910664437919071018703504227782178234815786885518282957399445596959

e=65537

n = p * q



c=1651024298
m = usePrivateKeyToEncrypt(p,q,e,c)
c = usePublicKeyToDecrypt(n,e,m)
print(c)

m=1651024298
c = usePublicKeyToEncrypt(n,e,m)
m = usePrivateKeyToDecrypt(p,q,e,c)
print(m)
