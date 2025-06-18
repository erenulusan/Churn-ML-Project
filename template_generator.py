import os
from pathlib import Path


project_name = "churn_ml_project" 

list_of_files = [
    
    f"src/{project_name}/__init__.py", 
    # Temel modüller
    f"src/{project_name}/data_loader.py",
    f"src/{project_name}/preprocessing.py",
    f"src/{project_name}/feature_engineering.py",
    f"src/{project_name}/models.py",
    f"src/{project_name}/evaluation.py",
    f"src/{project_name}/utils.py",

    "README.md",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    "app.py", 
]


for filepath in list_of_files:
    filepath = Path(filepath) 
    filedir, filename = os.path.split(filepath) 

    if filedir != "": 
        os.makedirs(filedir, exist_ok=True) 

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass # Boş dosya oluştur
    else:
        print(f"file is already present at: {filepath}")

print("Proje yapısı başarıyla oluşturuldu veya güncellendi.")