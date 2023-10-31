# Laporan Proyek Machine Learning
### Nama : Fauzan Musyaffa
### Nim : 211351158
### Kelas : Malam B

## Domain Proyek

Di berbagai negara, terlebih di negara yang memiliki musim dingin, wine sangat sering dan lumrah di konsumsi dikarenakan dapat menghangatkan badan di kala musim dingin/musim salju datang. Cita rasa wine menjadi hal penting dan menjadi sebuah pertimbangan apakah wine tersebut akan diminum atau tidaknya, selain dari pada itu, kualitas dari wine pun dapat mempengaruhi rasa dari wine itu sendiri.

## Business Understanding

Aplikasi prediksi kualitas wine dapat dipakai guna mempermudah dalam menentukan kualitas dari wine sehingga penikmat wine maupun penjual dapat memilih dan mengetahui terlebih dahulu mana wine yang berkualitas tinggi yang dapat mereka konsumsi dan layak untuk dijual dipasaran.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Pengecekan kualitas wine yang harus di cicipi satu persatu (manual)
- Memakan waktu dalam pengecekan kualitas wine

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Mempermudah dan mempercepat dalam melakukan uji kualitas wine

    ### Solution statements
    - Membuat aplikasi yang hanya memasukan angka-angka dari kadar/komposisi wine yang selanjutkan akan di proses untuk menentukan apakah wine tersebut berkualitas tinggi atau tidak
    - Model yang dipakai pada aplikasi tersebut dibuat menggunakan algoritma Logistic Regression dengan minimum akurasi 70%

## Data Understanding
Dataset yang dipakai yang berasal dari kaggle ini berisi 1599 baris dan 12 kolom. Berisi tentang informasi terkait komposisi dari beberapa wine yang selanjutnya akan di uji untuk menghasilkan sebuah prediksi dari kualitas wine.

dataset: [Wine Quality Classification](https://www.kaggle.com/datasets/nareshbhat/wine-quality-binary-classification).

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

### Variabel-variabel pada Heart Failure Prediction Dataset adalah sebagai berikut:
- fixed_acidity = keasaman tetap ```float64```
- volatile_acidity = keasaman mudah menguap ```float64```
- citric_acid = asam sitrat ```float64```
- residual_sugar = sisa gula ```float64```
- chlorides = klorida ```float64```
- free_sulfur_dioxide = sulfur dioksida bebas ```float64```
- total_sulfur_dioxide = total sulfur dioksida ```float64```
- density = densitas ```float64```
- pH = pH ```float64```
- sulphates = sulfat ```float64```
- alcohol = alkohol ```float64```
- quality = good (bagus) dan bad (buruk) ```object```
```dtypes: float64(11), object(1)```

Visualisasi dari jumlah data kualitas wine:
![image](https://github.com/fauzanm2211/kualitas-wine/assets/149327555/2f93c5a2-098e-4737-a11c-e41344b95d06)

## Data Preparation
Pada dasarnya semua atribut yang akan digunakan sudah sesuai dengan kebutuhan algoritma yang dipakai, hanya saja terdapat data duplikat yang berjumlah 24 data yang mana harus di hapus:
```
df = df.drop_duplicates()
df.duplicated().sum()
```
Selain itu, tipe data labelnya masih object, harus di konversi menjadi numerik:
```
df.replace(('bad','good'), (0,1), inplace=True)
```

## Modeling
Tahap pertama dalam pembuatan model ini adalah menentukan atribut (X) dan Label (Y):
```
X = df.drop (columns='quality', axis=1)
Y = df['quality']
```
Setelah itu pemisahan data training dan testing:
```
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.2, stratify=Y, random_state=2)
```
Selanjutnya, pembuatan model menggunakan Logistic Regression:
```
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, Y_train)
```

## Evaluation
Tahapan evaluasi yang dipakai adalah penggunakan metrik akurasi guna pengecekan kualitas dari model yang sudah dibuat:
```
from sklearn.metrics import accuracy_score
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
```
```
print("Akurasi data training : ", training_data_accuracy)
```
Akurasi data training :  0.7488500459981601

Dari pengujian yang dilakukan didapatkan hasil akurasi sebesar 74% yang mana model tersebut masih dapat dipakai dikarenakan minimum akurasi yang ditentukan sebelum nya adalah 70%.

## Deployment
[Link Aplikasi](https://kualitas-wine-fauzanm.streamlit.app/)

