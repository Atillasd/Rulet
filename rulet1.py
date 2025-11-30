import random


# BAKIYE MUTLAKA GLOBAL OLMALI
hesap_bakiyesi = 200


# --- HESAP İŞLEMLERİ FONKSİYONLARI ---

def bakiye():
    global hesap_bakiyesi
    print(f"\nBakiye: {hesap_bakiyesi}")


def para_yatır():
    global hesap_bakiyesi
    # input(print(...)) yerine sadece input(...) kullanıldı
    try:
        miktar = int(input("\nYatırılacak Miktar:"))
        if miktar <= 0:
            print("Geçersiz miktar.")
            return  # Fonksiyondan çık
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return  # Fonksiyondan çık

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
    print("  4) Bahis Menüsüne Dön ")  # Çıkış yerine menüye dönüş

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
        return  # Ana döngüye geri döner


# --- BAHİS FONKSİYONLARI ---

def Sayı(bahis):
    global hesap_bakiyesi  # SCOPE DÜZELTMESİ
    try:
        secilen_sayı = int(input("Bir Sayi Seciniz (0-36):"))
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return

    if secilen_sayı < 0 or secilen_sayı > 36:
        print("Yanlış Değer Girdiniz")
        return  # Menüye geri dönmek için

    print("-" * 30)
    print("Rulet Dönüyor...\n\n")
    a = random.randint(0, 36)
    print(f"Kazanan sayı : {a}")
    if secilen_sayı == a:
        # Bahis 1'e 35 öder (Yatırımınız + 35 katı kar = toplam 36 katı)
        kazanc = bahis * 36
        hesap_bakiyesi = hesap_bakiyesi + kazanc
        print(f"TEBRİKLER {kazanc} TL KAZANDINIZ (Kâr: {bahis * 35} TL)")
    else:
        # Bahis zaten başta çıkarıldığı için sadece kaybettiği bildirilir
        print("KAYBETTİNİZ")


def Renk(bahis):
    global hesap_bakiyesi  # SCOPE DÜZELTMESİ
    secilen_renk = input("Bir Renk Secin (kırmızı/siyah/yeşil):").lower()

    if secilen_renk not in ["kırmızı", "siyah", "yeşil"]:
        print("Geçersiz renk")
        return

    print("-" * 30)

    # 0 yeşil, 1-18 kırmızı/siyah, 19-36 kırmızı/siyah
    a = random.randint(0, 36)

    if a == 0:
        kazanan_renk = "yeşil"
    elif a % 2 != 0:  # Tek sayılar (1, 3, 5, ..., 35) genellikle Kırmızı kabul edilir
        kazanan_renk = "kırmızı"
    else:  # Çift sayılar (2, 4, 6, ..., 36) Siyah kabul edilir
        kazanan_renk = "siyah"

    print(f"Kazanan Sayı : {a}")
    print(f"Kazanan Renk : {kazanan_renk.upper()}")

    if kazanan_renk == "yeşil" and secilen_renk == "yeşil":
        # Yeşil 1'e 14 öder (Yatırımınız + 14 katı kar = toplam 15 katı)
        kazanc = bahis * 15
        hesap_bakiyesi = hesap_bakiyesi + kazanc
        print(f"TEBRİKLER {kazanc} TL KAZANDINIZ (Kâr: {bahis * 14} TL)")
    elif kazanan_renk == secilen_renk:
        # Kırmızı/Siyah 1'e 1 öder (Yatırımınız + 1 katı kar = toplam 2 katı)
        kazanc = bahis * 2
        hesap_bakiyesi = hesap_bakiyesi + kazanc
        print(f"TEBRİLER {kazanc} TL KAZANDINIZ (Kâr: {bahis} TL)")
    else:
        print("KAYBETTİNİZ")


def Tek_Cift(bahis):
    global hesap_bakiyesi  # SCOPE DÜZELTMESİ
    TekCift = input("Tek / Cift :").lower()
    if TekCift not in ["tek", "cift"]:  # Hatalı kontrol düzeltildi
        print("Hatalı Giris")
        return

    print("-" * 30)
    print("Rulet Dönüyor...\n\n")
    a = random.randint(0, 36)
    print(f"Kazanan Sayı : {a}")

    if a == 0:
        print("SAYI SIFIR. KAYBETTİNİZ")
    elif (a % 2 == 0 and TekCift == "cift") or (a % 2 != 0 and TekCift == "tek"):
        # Tek/Çift 1'e 1 öder
        kazanc = bahis * 2
        hesap_bakiyesi = hesap_bakiyesi + kazanc
        print(f"TEBRİKLER {kazanc} TL KAZANDINIZ (Kâr: {bahis} TL)")
    else:
        print("KAYBETTİNİZ")


def Alt_Ust(bahis):
    global hesap_bakiyesi  # SCOPE DÜZELTMESİ
    AltUst = input("Alt (1-18) / Üst (19-36) :").lower()

    # Giriş kontrolü düzeltildi
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
        # Alt/Üst 1'e 1 öder
        kazanc = bahis * 2
        hesap_bakiyesi = hesap_bakiyesi + kazanc
        print(f"TEBRİKLER {kazanc} TL KAZANDINIZ (Kâr: {bahis} TL)")
    else:
        print("KAYBETTİNİZ")


def Duzine(bahis):
    global hesap_bakiyesi  # SCOPE DÜZELTMESİ
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

    # Mantık Düzeltildi: Çekilen sayıyı (a) kontrol etmeliyiz.
    if secilen_duzine == 1 and 1 <= a <= 12:
        kazandi = True
    elif secilen_duzine == 2 and 13 <= a <= 24:
        kazandi = True
    elif secilen_duzine == 3 and 25 <= a <= 36:
        kazandi = True

    if kazandi:
        # Düzine 1'e 2 öder (Yatırımınız + 2 katı kar = toplam 3 katı)
        kazanc = bahis * 3
        hesap_bakiyesi = hesap_bakiyesi + bahis * 2  # Sadece kârı ekle
        print(f"TEBRİKLER {kazanc} TL KAZANDINIZ (Kâr: {bahis * 2} TL)")
    else:
        print("KAYBETTİNİZ")


# --- MENÜ FONKSİYONU VE ANA DÖNGÜ ---

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
        return  # Fonksiyondan çıkıp döngü başına döner

    if secim not in [1, 2, 3, 4, 5, 6, 7]:
        print("Yanlıs Deger Girdiniz")
        return

    if secim == 7:
        print("\nOyun sonlandırılıyor. Güle güle!")
        return 7  # Ana döngüye özel bir değer gönderir

    if secim == 6:
        hesap()
        return  # Hesap işleminden sonra menüye döner

    # Bahis miktarı alma
    try:
        bahis = int(input("Bahis Miktarı Giriniz:"))
        if bahis <= 0:
            print("Bahis miktarı pozitif olmalıdır.")
            return
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return

    # Bakiye kontrolü
    if hesap_bakiyesi < bahis:
        print("Yetersiz Bakiye. Lütfen önce bakiye yükleyin.")
        x = input("Hesabınıza Bakiye Yüklemek İstermisiniz ? (E / H)").upper()
        if x == "E":
            para_yatır()
        # Hatalı break yerine return kullanıldı.
        return
    else:
        # Bahis başarılı, bakiyeden düş
        hesap_bakiyesi = hesap_bakiyesi - bahis

        if secim == 1:
            Sayı(bahis)
        elif secim == 2:
            Renk(bahis)
        elif secim == 3:
            Tek_Cift(bahis)
        elif secim == 4:
            Alt_Ust(bahis)  # Hata: Duzine yerine Alt_Ust'a AltUst değişkenini kullanıyordu. Düzeltildi.
        elif secim == 5:
            Duzine(bahis)


def main():
    while True:
        result = print_bet_menu()
        if result == 7:
            # print_bet_menu'den 7 gelirse ana döngüyü sonlandır
            break


# Programı başlat
if __name__ == "__main__":
    main()