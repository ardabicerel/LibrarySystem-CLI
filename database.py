import sqlite3


#   Veritabanı dosyasını ve gerekli tabloyu oluşturan ana kurulum fonksiyonu.
#   The main setup function that creates the database file and the necessary table.

def kurulum_yap():

    baglanti = sqlite3.connect("kutuphane_veritabani.db")

    imlec = baglanti.cursor()

    sorguOlustur = "CREATE TABLE IF NOT EXISTS kitaplar (id INTEGER PRIMARY KEY AUTOINCREMENT, isim TEXT, yazar TEXT, yayinevi TEXT, sayfa_sayisi INTEGER)"

    imlec.execute(sorguOlustur)

    baglanti.commit()
    baglanti.close()


#   Kullanıcıdan alınan kitap bilgilerini veritabanına güvenli bir şekilde ekleyen fonksiyon.
#   The function that securely adds the book information received from the user to the database.

def kitap_ekle(isim, yazar, yayinevi, sayfa_sayisi):
    
    baglanti = sqlite3.connect("kutuphane_veritabani.db")

    imlec = baglanti.cursor()

    imlec.execute("INSERT INTO kitaplar (isim, yazar, yayinevi, sayfa_sayisi) VALUES (?, ?, ?, ?)", (isim, yazar, yayinevi, sayfa_sayisi))
    
    baglanti.commit()
    
    baglanti.close()


#   Veritabanındaki tüm kitap kayıtlarını çekip liste olarak döndüren fonksiyon.
#   The function that fetches all book records from the database and returns them as a list.

def kitaplari_getir():

    baglanti = sqlite3.connect("kutuphane_veritabani.db")

    imlec = baglanti.cursor()

    imlec.execute("SELECT * FROM kitaplar")

    kitap_veri = imlec.fetchall()
    
    baglanti.close()

    return kitap_veri


#   Seçilen kitabın ID numarasına göre veritabanından silinmesini sağlayan fonksiyon.
#   The function that enables the deletion of the selected book from the database based on its ID number.

def kitap_sil(kitap_id):
    baglanti = sqlite3.connect("kutuphane_veritabani.db")

    imlec = baglanti.cursor()

    imlec.execute("DELETE FROM kitaplar WHERE id = ?", (kitap_id,))

    baglanti.commit()
    
    baglanti.close()