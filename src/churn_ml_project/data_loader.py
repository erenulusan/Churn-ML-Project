import pandas as pd

def load_telco_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Veri seti başarıyla yüklendi. Boyut: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Hata: Belirtilen dosya yolu bulunamadı: {file_path}")
        return None
    except Exception as e:
        print(f"Veri yüklenirken bir hata oluştu: {e}")
        return None

if __name__ == "__main__":
    pass