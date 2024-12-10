def luaspersegipanjang (panjang, lebar):
    return panjang * lebar
def keliling (panjang,lebar):
    return 2* (panjang + lebar)
a = float(input("masukkan panjang: "))
b = float(input("masukkan lebar: "))
hasil_luas = luaspersegipanjang (a,b)
hasil_lebar = lebar (a,b)
print ("hasil luas adalah:",hasil_luas)
print ("hasil lebar adalah:",hasil_lebar)

def fungsi (x):
    return (2x^2+3x)-10
a = float(input("masukkan variabel"))
hasil_fx =fungsi(a)
print("hasil dari funfsi f(x) = (2^x2+3x)-10 adalah: ",hasil_fx)
