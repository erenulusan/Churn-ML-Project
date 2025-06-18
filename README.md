# Churn-ML-Project: Telekom Müşteri Kaybı Tahmini

Bu proje, bir telekomünikasyon şirketinin müşteri verilerini kullanarak müşteri kaybı (churn) olasılığını tahmin etmeyi amaçlayan uçtan uca bir makine öğrenmesi çözümüdür. Temel hedef, potansiyel olarak müşteri kaybı riski taşıyan müşterileri proaktif olarak belirleyerek şirketin müşteri tutma stratejilerini optimize etmesine yardımcı olmaktır.

## Proje Yapısı

Proje, okunabilirliği, sürdürülebilirliği ve modülerliği artırmak amacıyla aşağıdaki ana klasör ve dosya yapısına göre organize edilmiştir:

- `data/`: Ham veri setini içerir (`WA_Fn-UseC_-Telco-Customer-Churn.csv`).
- `notebooks/`: Keşifsel veri analizi (EDA), veri işleme, modelleme ve dağıtım adımlarını gösteren Jupyter Notebook'lar.
- `src/`: Projenin ana Python paketi olan `churn_ml_project` ve ilgili modüllerini içerir.
  - `src/churn_ml_project/`: Ana Python paketi.
    - `__init__.py`: Paketin başlatma dosyası.
    - `data_loader.py`: Veri yükleme ve başlangıç kontrollerini yapma fonksiyonları.
    - `preprocessing.py`: Veri temizleme, eksik değer yönetimi, aykırı değer işleme ve özellik mühendisliği fonksiyonları.
    - `feature_engineering.py`: Özellik mühendisliği fonksiyonları.
    - `models.py`: Makine öğrenmesi modeli tanımlamaları ve eğitim/tahmin fonksiyonları.
    - `evaluation.py`: Model performans metriklerini hesaplama ve raporlama.
    - `utils.py`: Genel yardımcı fonksiyonlar.
- `models/`: Eğitilmiş makine öğrenmesi modellerinin kaydedildiği yer.
- `api/`: Eğitilmiş modeli bir REST API olarak sunan FastAPI uygulamasını ve Dockerfile'ı içerir.
- `requirements.txt`: Projenin tüm Python bağımlılıklarını listeleyen dosya.
- `setup.py`: Projenin Python paketi olarak kurulumunu ve bağımlılıklarını yöneten dosya.
- `template_generator.py`: Proje yapısını otomatik oluşturan script.


## Kullanılan Yaklaşımlar ve Teknolojiler

Bu projede kullanılan temel yaklaşımlar ve teknolojiler şunlardır:

- **Veri Analizi ve İşleme:** Pandas, NumPy, Matplotlib, Seaborn
- **Makine Öğrenmesi Algoritmaları:** Lojistik Regresyon, Karar Ağaçları, Random Forest, Gradient Boosting (XGBoost/LightGBM), Destek Vektör Makineleri (SVM), K-En Yakın Komşu (KNN), Basit Nöral Ağlar (Keras ile)
- **Model Geliştirme ve Değerlendirme:** Scikit-learn
- **Model Dağıtımı:** FastAPI, Docker
- **Versiyon Kontrolü:** Git, GitHub

## Kurulum

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları takip edin:

1.  **Depoyu Klonlayın:**
    ```bash
    git clone [https://github.com/erenulusan/Churn-ML-Project.git](https://github.com/erenulusan/Churn-ML-Project.git)
    cd Churn-ML-Project
    ```
    (Yukarıdaki URL'i kendi GitHub reponuzun doğru adresiyle değiştirmeyi unutmayın.)
2.  **Proje Yapısını Oluşturun:**
    Projenin kök dizininde `template_generator.py` scriptini çalıştırın:
    ```bash
    python template_generator.py
    ```
3.  **Python Ortamı:** Python 3.x sürümünün kurulu olduğundan emin olun.
4.  **Bağımlılıkları Yükleyin:**
    Gerekli tüm paketleri aşağıdaki komut ile yükleyebilirsiniz:
    ```bash
    pip install -r requirements.txt
    ```
    Not: Bu `requirements.txt` dosyası, projenin geliştirildiği Anaconda ortamının (`datasc`) `pip freeze` komutuyla otomatik olarak oluşturulmuştur.
5.  **Projeyi Geliştirme Modunda Yükleyin:**
    `src` klasöründeki modülleri projenin herhangi bir yerinden import edebilmek için, proje kök dizininde (setup.py'nin olduğu yer) Anaconda ortamınız aktifken şu komutu çalıştırın:
    ```bash
    pip install -e .
    ```

## Kullanım

Proje adımları `notebooks/` klasöründeki Jupyter Notebook'lar aracılığıyla takip edilebilir:

1.  `1_EDA_and_Pipeline_Development.ipynb` not defterini çalıştırarak veri analizi ve ön işleme adımlarını keşfedin.
    * **Not:** Notebook'ların başında, `src/churn_ml_project` paketinden modülleri import etmek için `from churn_ml_project.data_loader import load_telco_data` gibi ifadeler kullanın.
2.  `2_Modeling_Evaluation.ipynb` not defterini çalıştırarak model eğitim ve değerlendirme süreçlerini inceleyin.
3.  `3_Deployment.ipynb` not defteri, modelin API olarak nasıl sunulduğunu ve Docker ile nasıl paketlendiğini gösterir.

API'yi yerel olarak çalıştırmak ve model tahminleri almak için:
(Bu bölüm, API aşamasına geldiğimizde doldurulacaktır.)
