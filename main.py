import matplotlib.pyplot as plt

# Sorular ve CO2 eşdeğerleri için katsayılar
sorular = [
    "Günlük su tüketiminiz (litre)?",
    "Günlük kahve tüketiminiz (bardak)?",
    "Haftada kaç gün duş alırsınız? (gün)",
    "Duşta harcadığınız su miktarı (litre)?",
    "Günlük araba ile seyahat mesafeniz (km)?",
    "Günlük harcanan elektrik miktarı? (kWh)",
    "Evde kaç kişi yaşıyorsunuz? (kişi)",
    "Günlük çöp miktarınız (kg)?",
    "Günlük harcanan doğalgaz miktarı?(m3)",
    "Kağıt geri dönüşümü için harcanan CO2 miktarı (kg)?",
    "Yiyecek ve içeceklere harcanan miktar (TL)?",
    "Kıyafetlere harcanan miktar (TL)?",
    "Kitap, gazete gibi kağıt ürünlerine harcanan miktar (TL)?",
    "Bilgisayar ve yazılım sistemlerine harcanan miktar (TL)?",
    "Televizyon ve telefona harcanan miktar (TL)?",
    "Motorlu taşıtlara harcanan miktar (TL)?",
    "Mobilyalara harcanan miktar (TL)?",
    "Otel ve restoranlara harcanan miktar (TL)?",
    "Eğitime harcanan miktar (TL)?",
    "Ayda kaç kilogram et tüketiyorsunuz (KG)?",
    "Aylık ortalama ne kadar kağıt tüketiyorsunuz (kg)?",
    "Yılda kaç kilometre uçakla seyahat ediyorsunuz (km)?",
    "Aylık kaç km toplu taşıma kullanıyorsunuz (km)?",
    "Haftada kaç kilo fast food tüketiyorsunuz (kg)?",
    "Yıllık kaç kilogram odun kullanıyorsunuz (kg)?"
]

katsayilar = [0.11, 0.02, 1.5, 0.15, 0.1, 0.2, 0.5, 1.0, 0.07, 0.02, 0.15, 0.1, 0.05, 0.2, 0.15, 0.1, 0.4, 0.15, 0.1, 1.5, 0.7, 2.5, 1.2, 0.9, 0.1]

# Kullanıcıdan cevapları al
cevaplar = []
for soru in sorular:
    cevap = input(soru + ": ")
    if cevap.replace('.', '', 1).isdigit():
        cevaplar.append(float(cevap))
    else:
        cevaplar.append(0)  # If the response is not numeric, consider it as 0 for the calculation

# CO2 eşdeğerini hesapla
co2_esdegeri = sum([cevap * katsayi for cevap, katsayi in zip(cevaplar, katsayilar)])

# Sonucu ekrana yazdır
print(f"\nToplam CO2 Eşdeğeri: {co2_esdegeri} kgCO2")

# Grafiği çiz
plt.bar(sorular[3:], [cevap * katsayi for cevap, katsayi in zip(cevaplar[3:], katsayilar[3:])])
plt.xticks(rotation=45, ha="right")
plt.xlabel("Sorular")
plt.ylabel("CO2 Eşdeğeri (kgCO2)")
plt.title("Kullanıcı Çıktılarına Göre CO2 Eşdeğeri")
plt.tight_layout()
plt.show()
