harfler=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
metin="Thequick BROWN foX jumps over the lazydog"
def panagram(veri):
    veri=veri.lower()
    m=0
    for i in range(len(harfler)):
        if  harfler[i] in veri:
            m=m+1
    return m==26

print(panagram(metin))
