from setuptools import setup, find_packages # find_packages'ı burada kullanıyoruz

setup(
    name='churn_ml_project',
    version='0.1.0',
    author='Eren Ulusan', 
    author_email='erenulusann@gmail.com', 
    description='An end-to-end machine learning solution for Telco Customer Churn prediction.',
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown',
    url='https://github.com/erenulusan/Churn-ML-Project', 
    packages=find_packages(where='src'), 
    package_dir={'': 'src'}, 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10.16', 
)