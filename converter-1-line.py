from tabulate import tabulate
import itertools as it


def genConverter(angka, pembilang):
    result = []
    hasilAngka = ""
    loop = True
    while loop:
        if angka >= pembilang:
            result.append(angka)
            sisa = angka % pembilang
            angka = angka // pembilang
            if sisa > 9:
                huruf = libChar(sisa)
                hasilAngka += huruf
                sisa = "{0} = {1}".format(sisa, huruf)
            else:
                hasilAngka += str(sisa)
            divid = "{0}------  {1}".format(pembilang, sisa)
            result.append(divid)
        else:
            if angka > 9:
                angka = libChar(angka)
            hasilAngka += str(angka)
            result.append(angka)
            loop = False
            break
        result.append("")

    hasilAngka = "".join(reversed(hasilAngka))  # reversed

    return (result, hasilAngka)


def libChar(angka):
    if angka == 10:
        return "A"
    elif angka == 11:
        return "B"
    elif angka == 12:
        return "C"
    elif angka == 13:
        return "D"
    elif angka == 14:
        return "E"
    elif angka == 15:
        return "F"
    elif angka == 16:
        return "G"
print('===========================================================================')
angka = int(input("Masukkan bilangan Desimal untuk dikonversi menjadi Biner, Oktal, dan Hexa : "))

biner, hasilBiner = genConverter(angka, 2)
octal, hasilOctal = genConverter(angka, 8)
hexa, hasilHexa = genConverter(angka, 16)

combine = list(it.zip_longest(biner, octal, hexa))

header = ("Binner", "Octal", "Hexadecimal")

print(tabulate(combine, header, tablefmt="plain"))
print("")
print('=================================')
print("Binner : ", hasilBiner)                                                      
print("Octal  : ", hasilOctal)                                                      
print("Hexa   : ", hasilHexa)                                                       
print('=================================')

