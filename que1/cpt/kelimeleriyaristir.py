import sys

harfler=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def karsilastir(veri):
    v=veri.split(" ")
    v2=[]
    for veri1 in v:
        t=0
        for a in (veri1) :
            t=t+int(harfler.index(a)+1)
        v2.append(t)
    return (v[v2.index(max(v2))])

print(karsilastir("abcdf ghjkl qwerytyu"))
