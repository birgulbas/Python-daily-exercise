# **`🏆 BÜYÜK PROJE: Zindan Savaşı Simülatörü`**

**`🟢 1. ADIM: Soyut Altyapıyı Kurmak (Abstraction)`**
Amaç: Oyundaki tüm canlıların (Kahramanlar ve Düşmanlar) uyması gereken zorunlu bir şablon oluşturmak.
**Ne Yapacaksın?:** Karakter adında soyut bir sınıf (ABC) oluştur.
İçinde soyut bir saldir() metodu ve soyut bir hasar_al() metodu tanımla. Bunların içi boş olsun (pass).

**`🔵 2. ADIM: Eşya Sistemini Kurmak (Composition)`**
Amaç: Bir nesnenin içinde başka bir nesneyi barındırma (has-a ilişkisi) mantığını kavramak.
**Ne Yapacaksın?:** Esya adında bir sınıf oluştur. Constructor (__init__) içinde isim ve guc parametrelerini alsın.
Bu sınıftan türeyen iki farklı nesne yaratacağız daha sonra: Biri kılıç olacak (hasarı artıracak), diğeri iksir olacak (canı artıracak).

**`🟡 3. ADIM: Ana Kahraman Sınıfı ve Gizlilik (Constructors & Encapsulation)`**
Amaç: Verileri dış dünyadan gizlemek ve constructor yapısını kurmak.
**Ne Yapacaksın?:** Karakter sınıfından miras alan bir Kahraman sınıfı yaz.
__init__ metodunda isim, can ve taban_hasar değerlerini al.
Kapsülleme: can değişkenini gizli yap (self.__can). Dışarıdan doğrudan değiştirilemesin.
Bu gizli canı okumak için bir Getter (def can_goster) metodu yaz.
Sınıfın içine bir esya özelliği ekle ve ilk başta None (boş) olsun. Bir de esya_kuşan(yeni_esya) metodu yaz, bu metot kahramana bir Esya nesnesi atasın.

**`🔴 4. ADIM: Alt Sınıfları Yaratmak (Inheritance & Self vs Super)`**
Amaç: Kod tekrarı yapmadan üst sınıfın özelliklerini alt sınıfa aktarmak.
**Ne Yapacaksın?:** Kahraman sınıfından miras alan iki alt sınıf oluştur: Savasci ve Buyucu.
__init__ metodlarının içinde super().__init__() fonksiyonunu kullanarak isim, can ve hasar değerlerini üst sınıfa gönder.
Örneğin; Savaşçının canı yüksek olsun (150), Büyücünün ise hasarı yüksek ama canı düşük olsun (80).

**`🟣 5. ADIM: Savaş Mekaniklerini Özelleştirmek (Polymorphism)`**
Amaç: Aynı isimdeki metodun farklı sınıflarda farklı davranmasını sağlamak.
**Ne Yapacaksın?:** Savasci ve Buyucu sınıflarının içine saldir() metodunu yaz (Override et).
Savasci'nin saldırısı: taban_hasar + (Eğer elinde eşya varsa esya.guc). Çıkan sonucu döndürsün ve ekrana "Kılıç savurdu" yazsın.
Buyucu'nun saldırısı: taban_hasar değerinin 1.5 katı (Büyü güçlendirmesi) + (Eğer elinde eşya varsa esya.guc). Ekrana "Alev fırlattı" yazsın.
Her iki sınıf için de hasar_al(miktar) metodunu doldur. Gelen hasar miktarını gizli __can değerinden düşürsün.

**``**`🔥 6. ADIM:** `Büyük Savaş Alanı (Hero Battle / Composition Uygulaması)``**
Amaç: Tüm bu nesneleri birbiriyle etkileşime sokarak simülasyonu çalıştırmak.
**Ne Yapacaksın?:** Temiz bir sayfada veya kodun en altında şu senaryoyu çalıştır:
efsanevi_kılıç = Esya("Excalibur", 20) diyerek bir eşya nesnesi üret.
Bir Savasci nesnesi (Örn: Arthur) ve bir Buyucu nesnesi (Örn: Merlin) üret.
Arthur'a esya_kuşan(efsanevi_kılıç) metoduyla kılıcı ver (Composition).
Bir while döngüsü başlat. İkisinin de canı 0'dan büyük olduğu sürece sırayla birbirlerine saldir() metoduyla vursunlar ve hasar_al() metoduyla canlarını azaltsınlar.
Canı önce 0 olan elensin ve kazananı ekrana yazdır!