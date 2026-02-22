import database # Veritabanı komutlarımızı içeri aktarıyoruz. / We are importing our database commands.


#   Veritabanımızı uygulama başladığında oluşturuyoruz.
#   We create our database when the application starts.

database.kurulum_yap() 


while True:

    print("-----------------\n1- Kitap Ekle\n2- Kitapları Listele\n3- Kitap Sil\n4- Çıkış\n-----------------")
    
    
    #   Kütüphanedeki işlemleri yapabilmek için menüdeki seçenekleri kullanıyoruz.
    #    We use the options in the menu to perform library operations.
    
    try:
        secenek = int(input("Yapmak istediğiniz işlemi seçiniz(Select the action you wish the perform): ")) 
    except ValueError:
        print("Hatalı giriş! Lütfen menüdeki işlemlerden birini (1, 2, 3 veya 4) seçiniz.")
        continue
    
    #    Eğer 1. seçeneği seçersek kütüphaneye kitap ekleyebiliriz.
    #    If we choose the first option, we add books to the library.
    

    if secenek == 1:
        kitap_isim = input("Kitap adını giriniz: ")
        yazar = input("Yazarın adını giriniz: ")
        yayinevi = input("Yayınevi adını giriniz: ")
        
        while True:
            try:
                sayfa_sayisi = int(input("Kitabın sayfa sayısını giriniz: "))
                break
            except ValueError:
                print("Hatalı giriş! Lütfen sayfa sayısını rakam olarak giriniz.")

        database.kitap_ekle(kitap_isim, yazar, yayinevi, sayfa_sayisi)
        print("Kitap başarıyla eklendi.")

    
    #   Eğer 2. seçeneği seçersek kütüphanedeki mevcut kitapları listeleriz.
    #   If we choose the second option, we list the books currently in the library.
    

    elif secenek == 2: 
        kitaplar = database.kitaplari_getir()
        print("\n-----KÜTÜPHANE LİSTESİ-----")
        for kitap in kitaplar:
            print(f"İsim: {kitap[1]} | Yazar: {kitap[2]} | Yayınevi: {kitap[3]} | Sayfa: {kitap[4]}")

    
    #   Eğer 3. seçeneği seçersek kütüphanede bulunan kitapları veritabanından silebiliriz.
    #   If we choose the third option, we can delete the books which in the library from the database. 
    
    elif secenek == 3:

        kitaplar = database.kitaplari_getir()

        if len(kitaplar) > 0:
            print("\n-----KÜTÜPHANE LİSTESİ-----")
            gecerli_idler = []
            for kitap in kitaplar:
                print(f"ID: {kitap[0]} | İsim: {kitap[1]} | Yazar: {kitap[2]} | Yayınevi: {kitap[3]} | Sayfa: {kitap[4]}")
                gecerli_idler.append(kitap[0])

            try:
                silinecek_kitap_id = int(input("Yukarıda silmek istediğiniz kitabın ID'sini giriniz: "))
            except ValueError:
                print("Hatalı giriş! Lütfen sadece sayı kullanın.")
                continue

            if silinecek_kitap_id in gecerli_idler:
                
                onay = input(f"{silinecek_kitap_id} ID numarasına sahip kitabı silmek istediğinize emin misiniz?(E/H): ").upper()
                
                if onay == 'E':
                    database.kitap_sil(silinecek_kitap_id)
                    print(f"{silinecek_kitap_id} ID'li kitap veritabanından silindi.")
                elif onay == 'H':
                    print("Kitap silme işlemi iptal edildi.")
                else:
                    print("Geçersiz giriş")
            else:
                print("Bu ID numarasına sahip bir kitap bulunmuyor.")
        
        elif len(kitaplar) == 0:
            print("Kütüphane envanterinde şu an kitap bulunmuyor.")


    #   Eğer 4. seçeneği seçersek sistemden çıkış yaparız.
    #   If we choose the fourth option, we log out of the system.

    elif secenek == 4:
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz İşlem")

