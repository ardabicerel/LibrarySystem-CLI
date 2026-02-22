# Console-Based Library Management System | Konsol Tabanlı Kütüphane Yönetim Sistemi

*[Türkçe açıklama için aşağıya kaydırın / Scroll down for the Turkish version](#türkçe-sürüm)*

---

## 🇬🇧 English Version

This project is a console-based library database management (CRUD) application developed using Python and SQLite3. It allows users to add books, list existing books, and delete books from the database.

### Features

- **Data Persistence:** Data is stored in a local `.db` file, not in RAM. Records are not lost even if the program is closed.
- **Secure Data Entry:** Parameterized queries (`?`) are used to prevent SQL Injection attacks.
- **Exception Handling:** Type mismatches in user inputs (e.g., entering letters instead of numbers) are caught using `try-except` blocks to prevent the program from crashing.
- **Secure Deletion:** A user confirmation mechanism (Y/N) is implemented before deletion to prevent accidental data loss.

### Technologies Used

- Python 3
- SQLite3 (Built-in library)

### How to Run?

You do not need to install any extra modules to run the project on your computer.

1. Download or clone the repository to your computer.
2. Open a terminal or command prompt and navigate to the project folder.
3. Run the following command:

```bash
python main.py
```

*Note: When the application is run for the first time, it will automatically create a database file named `kutuphane_veritabani.db` in its directory.*

### File Structure

- `main.py`: Contains the user interface (console menu) and the main loop of the program.
- `database.py`: The database layer handling SQLite connections and SQL queries. Designed according to the Separation of Concerns principle.

---

<a name="türkçe-sürüm"></a>
## 🇹🇷 Türkçe Sürüm

Bu proje, Python ve SQLite3 kullanılarak geliştirilmiş konsol tabanlı bir kütüphane veri tabanı yönetim (CRUD) uygulamasıdır. Kullanıcıların kitap eklemesine, mevcut kitapları listelemesine ve veri tabanından kitap silmesine olanak tanır.

### Özellikler

- **Veri Kalıcılığı:** Veriler RAM'de değil, yerel bir `.db` dosyasında saklanır. Program kapansa bile kayıtlar kaybolmaz.
- **Güvenli Veri Girişi:** SQL Injection saldırılarına karşı parametreli sorgular (`?`) kullanılmıştır.
- **Hata Yönetimi (Exception Handling):** Kullanıcı girişlerindeki tip uyuşmazlıkları (harf/sayı karışıklığı) `try-except` blokları ile yakalanarak programın çökmesi engellenmiştir.
- **Güvenli Silme İşlemi:** Yanlışlıkla veri silinmesini önlemek için işlem öncesi kullanıcı onay mekanizması (E/H) bulunmaktadır.

### Kullanılan Teknolojiler

- Python 3
- SQLite3 (Dahili kütüphane)

### Nasıl Çalıştırılır?

Projeyi bilgisayarınızda çalıştırmak için ekstra bir modül yüklemenize gerek yoktur. 

1. Depoyu bilgisayarınıza indirin veya klonlayın.
2. Terminal veya komut satırını açarak proje klasörünün içine gidin.
3. Aşağıdaki komutu çalıştırın:

```bash
python main.py
```

*Not: Uygulama ilk kez çalıştırıldığında, bulunduğu dizinde otomatik olarak `kutuphane_veritabani.db` adında bir veri tabanı dosyası oluşturacaktır.*

### Dosya Yapısı

- `main.py`: Kullanıcı arayüzünü (konsol menüsü) ve programın ana döngüsünü barındırır.
- `database.py`: SQLite bağlantılarını ve SQL sorgularını işleyen veri tabanı katmanıdır. Sorumlulukların ayrılması (Separation of Concerns) prensibine uygun olarak tasarlanmıştır.
