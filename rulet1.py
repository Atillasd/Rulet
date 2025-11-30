import random


hesap_bakiyesi = 200


# --- HESAP İŞLEMLERİ FONKSİYONLARI ---

def bakiye():
    global hesap_bakiyesi
    print(f"\nBakiye: {hesap_bakiyesi}")


def para_yatır():
    global hesap_bakiyesi

    try:
        miktar = int(input("\nYatırılacak Miktar:"))
        if miktar <= 0:
            print("Geçersiz miktar.")
            return
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return

    hesap_bakiyesi = hesap_bakiyesi + miktar
    bakiye()


def para_cek():
    global hesap_bakiyesi
    try:
        miktar = int(input("\nÇekilecek Miktar:"))
        if miktar <= 0:
            print("Geçersiz miktar.")
            return
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return

    if hesap_bakiyesi < miktar:
        print("Yetersiz Bakiye")
    else:
        hesap_bakiyesi = hesap_bakiyesi - miktar
    bakiye()


def hesap():
    print("\nİŞLEM SEÇENEKLERİ:")
    print("  1) Bakiye Sorgula ")
    print("  2) Para Yatır ")
    print("  3) Para Çek ")
    print("  4) Bahis Menüsüne Dön ")

    try:
        x = int(input())
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return

    if x == 1:
        bakiye()
        hesap()
    elif x == 2:
        para_yatır()
        hesap()
    elif x == 3:
        para_cek()
        hesap()
    elif x == 4:
        return


# --- BAHİS FONKSİYONLARI ---

def Sayı(bahis):
    global hesap_bakiyesi
    try:
        secilen_sayı = int(input("Bir Sayi Seciniz (0-36):"))
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return

    if secilen_sayı < 0 or secilen_sayı > 36:
        print("Yanlış Değer Girdiniz")
        return

    print("-" * 30)
    print("Rulet Dönüyor...\n\n")
    a = random.randint(0, 36)
    print(f"Kazanan sayı : {a}")
    if secilen_sayı == a:

        kazanc = bahis * 36
        hesap_bakiyesi = hesap_bakiyesi + kazanc
        print(f"TEBRİKLER {kazanc} TL KAZANDINIZ (Kâr: {bahis * 35} TL)")
    else:

        print("KAYBETTİNİZ")


def Renk(bahis):
    global hesap_bakiyesi
    secilen_renk = input("Bir Renk Secin (kırmızı/siyah/yeşil):").lower()

    if secilen_renk not in ["kırmızı", "siyah", "yeşil"]:
        print("Geçersiz renk")
        return

    print("-" * 30)


    a = random.randint(0, 36)

    if a == 0:
        kazanan_renk = "yeşil"
    elif a % 2 != 0:
        kazanan_renk = "kırmızı"
    else:
        kazanan_renk = "siyah"

    print(f"Kazanan Sayı : {a}")
    print(f"Kazanan Renk : {kazanan_renk.upper()}")

    if kazanan_renk == "yeşil" and secilen_renk == "yeşil":

        kazanc = bahis * 15
        hesap_bakiyesi = hesap_bakiyesi + kazanc
        print(f"TEBRİKLER {kazanc} TL KAZANDINIZ (Kâr: {bahis * 14} TL)")
    elif kazanan_renk == secilen_renk:

        kazanc = bahis * 2
        hesap_bakiyesi = hesap_bakiyesi + kazanc
        print(f"TEBRİLER {kazanc} TL KAZANDINIZ (Kâr: {bahis} TL)")
    else:
        print("KAYBETTİNİZ")


def Tek_Cift(bahis):
    global hesap_bakiyesi
    TekCift = input("Tek / Cift :").lower()
    if TekCift not in ["tek", "cift"]:
        print("Hatalı Giris")
        return

    print("-" * 30)
    print("Rulet Dönüyor...\n\n")
    a = random.randint(0, 36)
    print(f"Kazanan Sayı : {a}")

    if a == 0:
        print("SAYI SIFIR. KAYBETTİNİZ")
    elif (a % 2 == 0 and TekCift == "cift") or (a % 2 != 0 and TekCift == "tek"):

        kazanc = bahis * 2
        hesap_bakiyesi = hesap_bakiyesi + kazanc
        print(f"TEBRİKLER {kazanc} TL KAZANDINIZ (Kâr: {bahis} TL)")
    else:
        print("KAYBETTİNİZ")


def Alt_Ust(bahis):
    global hesap_bakiyesi
    AltUst = input("Alt (1-18) / Üst (19-36) :").lower()


    if AltUst not in ["alt", "ust"]:
        print("Hatalı Giris")
        return

    print("-" * 30)
    print("Rulet Dönüyor...\n\n")
    a = random.randint(0, 36)
    print(f"Kazanan Sayı : {a}")

    if a == 0:
        print("SAYI SIFIR. KAYBETTİNİZ")
    elif (AltUst == "alt" and 1 <= a <= 18) or (AltUst == "ust" and 19 <= a <= 36):

        kazanc = bahis * 2
        hesap_bakiyesi = hesap_bakiyesi + kazanc
        print(f"TEBRİKLER {kazanc} TL KAZANDINIZ (Kâr: {bahis} TL)")
    else:
        print("KAYBETTİNİZ")


def Duzine(bahis):
    global hesap_bakiyesi
    print("-" * 30)

    try:
        secilen_duzine = int(input("Aralık Seçin (1: 1-12 / 2: 13-24 / 3: 25-36) :"))
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return

    if secilen_duzine not in [1, 2, 3]:
        print("Hatalı Secim")
        return

    print("Rulet Dönüyor...\n\n")
    a = random.randint(0, 36)
    print(f"Kazanan Sayi : {a}")

    kazandi = False


    if secilen_duzine == 1 and 1 <= a <= 12:
        kazandi = True
    elif secilen_duzine == 2 and 13 <= a <= 24:
        kazandi = True
    elif secilen_duzine == 3 and 25 <= a <= 36:
        kazandi = True

    if kazandi:

        kazanc = bahis * 3
        hesap_bakiyesi = hesap_bakiyesi + bahis * 2
        print(f"TEBRİKLER {kazanc} TL KAZANDINIZ (Kâr: {bahis * 2} TL)")
    else:
        print("KAYBETTİNİZ")




def print_bet_menu():
    global hesap_bakiyesi
    print("-" * 30)
    print(f"\n\nBAHİS SEÇENEKLERİ:                                    Bakiye: {hesap_bakiyesi}")
    print("  1) Sayı (0-36) ")
    print("  2) Kırmızı / Siyah / Yeşil ")
    print("  3) Tek / Çift ")
    print("  4) Alt (1-18) / Üst (19-36) ")
    print("  5) Düzine (1-12, 13-24, 25-36) ")
    print("  6) Hesaba Git ")
    print("  7) Çıkış / Oyunu Bitir\n")

    try:
        secim = int(input("Seçiminiz: "))
    except ValueError:
        print("Lütfen menüden geçerli bir sayı seçin.")
        return

    if secim not in [1, 2, 3, 4, 5, 6, 7]:
        print("Yanlıs Deger Girdiniz")
        return

    if secim == 7:
        print("\nOyun sonlandırılıyor. Güle güle!")
        return 7

    if secim == 6:
        hesap()
        return


    try:
        bahis = int(input("Bahis Miktarı Giriniz:"))
        if bahis <= 0:
            print("Bahis miktarı pozitif olmalıdır.")
            return
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return


    if hesap_bakiyesi < bahis:
        print("Yetersiz Bakiye. Lütfen önce bakiye yükleyin.")
        x = input("Hesabınıza Bakiye Yüklemek İstermisiniz ? (E / H)").upper()
        if x == "E":
            para_yatır()

        return
    else:

        hesap_bakiyesi = hesap_bakiyesi - bahis

        if secim == 1:
            Sayı(bahis)
        elif secim == 2:
            Renk(bahis)
        elif secim == 3:
            Tek_Cift(bahis)
        elif secim == 4:
            Alt_Ust(bahis)
        elif secim == 5:
            Duzine(bahis)


def main():
    while True:
        result = print_bet_menu()
        if result == 7:

            break


# Programı başlat
if __name__ == "__main__":
    main()