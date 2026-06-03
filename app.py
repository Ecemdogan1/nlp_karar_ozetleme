from pypdf import PdfReader
from openai import OpenAI

client = OpenAI()

def pdf_oku(dosya_yolu):
    """
    PDF içindeki tüm metni okur.
    """
    metin = ""

    reader = PdfReader(dosya_yolu)

    for sayfa in reader.pages:
        metin += sayfa.extract_text() + "\n"

    return metin


def chunk_olustur(metin, boyut=4000):
    """
    Uzun metni daha küçük parçalara böler.
    Büyük kararlar tek seferde modele gönderilemeyeceği için kullanılır.
    """
    parcalar = []

    for i in range(0, len(metin), boyut):
        parcalar.append(metin[i:i+boyut])

    return parcalar


def parcayi_ozetle(parca):
    """
    Tek bir metin parçasını özetler.
    """

    prompt = f"""
Aşağıdaki mahkeme kararını incele.

Şu başlıklarla özet çıkar:

1. Olay
2. Hukuki Sorun
3. Mahkeme Kararı
4. Sonuç

Metin:

{parca}
"""

    cevap = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return cevap.choices[0].message.content


def nihai_ozet(ozetler):
    """
    Parça özetlerini birleştirir ve tek sonuç üretir.
    """

    birlesik = "\n".join(ozetler)

    prompt = f"""
Aşağıdaki özetleri kullan.

Tek ve düzenli bir çıktı oluştur.

Başlıklar:

- Olay
- Hukuki Sorun
- Mahkeme Kararı
- Sonuç

Özetler:

{birlesik}
"""

    cevap = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return cevap.choices[0].message.content


def main():
    pdf_yolu = "karar.pdf"

    metin = pdf_oku(pdf_yolu)

    parcalar = chunk_olustur(metin)

    ozetler = []

    for parca in parcalar:
        ozetler.append(parcayi_ozetle(parca))

    sonuc = nihai_ozet(ozetler)

    print(sonuc)


if __name__ == "__main__":
    main()
