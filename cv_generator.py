from datetime import datetime

def bilgi_al(metin):
    return input(metin + ": ").strip()

def liste_al(baslik, sayi, alanlar):
    liste = []
    print(f"\n📌 {baslik}")
    for i in range(sayi):
        print(f"\n{baslik} {i+1}")
        veri = {}
        for alan in alanlar:
            veri[alan] = bilgi_al(f"{alan}")
        liste.append(veri)
    return liste


print("📝 CV Oluşturucu Başlıyor...\n")
ad = bilgi_al("Ad Soyad")
meslek = bilgi_al("Meslek")
ozet = bilgi_al("Kendinizi kısa tanıtın")
email = bilgi_al("E-posta")
telefon = bilgi_al("Telefon")


egitim_sayisi = int(bilgi_al("Kaç adet eğitim bilgisi gireceksiniz"))
egitim_listesi = liste_al("Eğitim", egitim_sayisi, ["Okul", "Bölüm", "Mezuniyet Yılı"])


deneyim_sayisi = int(bilgi_al("Kaç adet iş deneyimi gireceksiniz"))
deneyim_listesi = liste_al("İş Deneyimi", deneyim_sayisi, ["Şirket", "Pozisyon", "Yıl"])


yetenekler = bilgi_al("Yeteneklerinizi virgülle ayırarak girin (örnek: Python, HTML, SQL)")
yetenek_listesi = yetenekler.split(',')


cv_md = f"""# {ad}

## {meslek}

### 📌 Hakkımda
{ozet}

### 📧 İletişim
- E-posta: {email}
- Telefon: {telefon}

### 🎓 Eğitim
"""

for egitim in egitim_listesi:
    cv_md += f"- **{egitim['Okul']}**, {egitim['Bölüm']} ({egitim['Mezuniyet Yılı']})\n"

cv_md += "\n### 🧰 İş Deneyimi\n"
for deneyim in deneyim_listesi:
    cv_md += f"- **{deneyim['Şirket']}**, {deneyim['Pozisyon']} ({deneyim['Yıl']})\n"

cv_md += "\n### 💻 Yetenekler\n"
for yetenek in yetenek_listesi:
    cv_md += f"- {yetenek.strip()}\n"


tarih = datetime.now().strftime("%Y%m%d_%H%M")
dosya_adi = f"cv_{ad.lower().replace(' ', '_')}_{tarih}.md"

with open(dosya_adi, "w", encoding="utf-8") as dosya:
    dosya.write(cv_md)

print(f"\n✅ CV dosyanız '{dosya_adi}' olarak oluşturuldu!")
