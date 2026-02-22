# Konsol Tabanlı Kütüphane Yönetim Sistemi

Bu proje, Python ve SQLite3 kullanılarak geliştirilmiş konsol tabanlı bir kütüphane veri tabanı yönetim (CRUD) uygulamasıdır. Kullanıcıların kitap eklemesine, mevcut kitapları listelemesine ve veri tabanından kitap silmesine olanak tanır.

## Özellikler

- **Veri Kalıcılığı:** Veriler RAM'de değil, yerel bir `.db` dosyasında saklanır. Program kapansa bile kayıtlar kaybolmaz.
- **Güvenli Veri Girişi:** SQL Injection saldırılarına karşı parametreli sorgular (`?`) kullanılmıştır.
- **Hata Yönetimi (Exception Handling):** Kullanıcı girişlerindeki tip uyuşmazlıkları (harf/sayı karışıklığı) `try-except` blokları ile yakalanarak programın çökmesi engellenmiştir.
- **Güvenli Silme İşlemi:** Yanlışlıkla veri silinmesini önlemek için işlem öncesi kullanıcı onay mekanizması (E/H) bulunmaktadır.

## Kullanılan Teknolojiler

- Python 3
- SQLite3 (Dahili kütüphane)

## Nasıl Çalıştırılır?

Projeyi bilgisayarınızda çalıştırmak için ekstra bir modül yüklemenize gerek yoktur. 

1. Depoyu bilgisayarınıza indirin veya klonlayın.
2. Terminal veya komut satırını açarak proje klasörünün içine gidin.
3. Aşağıdaki komutu çalıştırın:

```bash
python main.py
