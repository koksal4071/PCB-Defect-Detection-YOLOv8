# YOLOv8 ile PCB (Baskı Devre Kartı) Kusur Tespit Sistemi 🚀

Bu proje, yapay zeka ve bilgisayarlı görü (Computer Vision) teknikleri kullanılarak üretim hattındaki PCB kartları üzerindeki üretim hatalarını (açık devre, eksik delik, kısa devre vb.) canlı olarak tespit etmek amacıyla geliştirilmiştir. 

Model, son teknoloji **YOLOv8 (You Only Look Once)** mimarisi kullanılarak eğitilmiştir.

---

## 📊 Model Performansı & Başarı Oranı

Eğitim sürecinde elde edilen **Confusion Matrix (Karmaşıklık Matrisi)** ve başarı grafikleri modelin ne kadar kararlı çalıştığını göstermektedir:

* **mAP50 Skoru:** ~%99 (Neredeyse kusursuz tespit oranı)
* **Açık Devre (Open Circuit) Başarısı:** %100




---

## 🔍 Gerçek Zamanlı Test Sonuçları

Modelin daha önce hiç görmediği test kartları üzerinde yaptığı başarılı tahminlerden bazıları:

### 1. Eksik Delik (Missing Hole) Tespiti
Model, kart üzerinde delinmesi unutulan pin yuvalarını başarıyla yakalamıştır.

### 2. Açık Devre (Open Circuit) Tespiti
Mikro düzeydeki yol kopuklukları nokta atışı olarak belirlenmiştir.

---

