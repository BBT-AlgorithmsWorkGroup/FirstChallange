f=1
def persistence(sayi):
        global f
        gsayi=1
        for i in range (len(sayi)):
            gsayi=gsayi*int(sayi[i])
        if(gsayi>10):
            f=f+1
            persistence(str(gsayi))
        else:
                print(f)
                f=0            
persistence("19")
