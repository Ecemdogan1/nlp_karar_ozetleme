# NLP Karar Özetleme Sistemi

Bu proje uzun mahkeme kararlarını analiz ederek şu başlıklarda özet üretir:

- Olay
- Hukuki Sorun
- Mahkeme Kararı
- Sonuç

## Öğrenilecek Konular

- NLP
- Metin Özetleme (Summarization)
- Chunking
- Prompt Engineering
- PDF İşleme

## Kurulum

pip install openai pypdf python-dotenv

## Çalıştırma

python app.py

## Çalışma Mantığı

1. PDF okunur.
2. Metin parçalara bölünür.
3. Her parça özetlenir.
4. Son özet oluşturulur.
5. Kullanıcıya gösterilir.
