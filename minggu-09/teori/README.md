# BAB 11 Virtual Environments and Packages

## 12.1. Introduction

> Aplikasi Python akan sering menggunakan paket dan modul yang tidak disertakan sebagai bagian dari pustaka standar. Aplikasi kadang-kadang membutuhkan versi perpustakaan tertentu, karena aplikasi mungkin memerlukan bug tertentu yang telah diperbaiki atau aplikasi mungkin ditulis menggunakan versi usang dari antarmuka perpustakaan.

> Ini berarti tidak mungkin satu instalasi Python memenuhi persyaratan setiap aplikasi. Jika aplikasi A membutuhkan versi 1.0 dari modul tertentu tetapi aplikasi B membutuhkan versi 2.0, maka persyaratan tersebut bertentangan dan menginstal versi 1.0 atau 2.0 akan membuat satu aplikasi tidak dapat berjalan.
> Solusi untuk masalah ini adalah membuat lingkungan virtual, pohon direktori mandiri yang berisi instalasi Python untuk versi Python tertentu, ditambah sejumlah paket tambahan.

> Aplikasi yang berbeda kemudian dapat menggunakan lingkungan virtual yang berbeda. Untuk mengatasi contoh konflik persyaratan sebelumnya, aplikasi A dapat memiliki lingkungan virtualnya sendiri dengan versi 1.0 diinstal sementara aplikasi B memiliki lingkungan virtual lain dengan versi 2.0. Jika aplikasi B memerlukan pustaka yang ditingkatkan ke versi 3.0, ini tidak akan memengaruhi lingkungan aplikasi A.

## 12.2. Creating Virtual Environments

> Modul yang digunakan untuk membuat dan mengelola lingkungan virtual disebut venv. venv biasanya akan menginstal versi Python terbaru yang Anda miliki. Jika Anda memiliki beberapa versi Python di sistem Anda, Anda dapat memilih versi Python tertentu dengan menjalankan python3 atau versi apa pun yang Anda inginkan.

> Untuk membuat lingkungan virtual, tentukan direktori tempat Anda ingin meletakkannya, dan jalankan modul venv sebagai skrip dengan jalur direktori:

```python
python -m venv tutorial-env
```

> Ini akan membuat direktori tutorial-env jika tidak ada, dan juga membuat direktori di dalamnya yang berisi salinan interpreter Python dan berbagai file pendukung.
> Lokasi direktori umum untuk lingkungan virtual adalah .venv. Nama ini membuat direktori biasanya tersembunyi di shell Anda dan dengan demikian menyingkir sambil memberinya nama yang menjelaskan mengapa direktori itu ada. Itu juga mencegah bentrok dengan file definisi variabel lingkungan .env yang didukung beberapa perkakas.

> Setelah membuat lingkungan virtual, Anda dapat mengaktifkannya.

> Di Windows, jalankan:

```python
tutorial-env\Scripts\activate.bat
```

> Di Unix atau MacOS, jalankan:

```python
source tutorial-env/bin/activate
```

> (Skrip ini ditulis untuk bash shell. Jika Anda menggunakan csh atau fish shells, ada alternatif skrip activation.csh dan activation.fish yang sebaiknya Anda gunakan.)

> Mengaktifkan lingkungan virtual akan mengubah prompt shell Anda untuk menunjukkan lingkungan virtual apa yang Anda gunakan, dan memodifikasi lingkungan sehingga menjalankan python akan memberi Anda versi dan pemasangan Python tertentu. Misalnya:

```python
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```

> Untuk menonaktifkan lingkungan virtual, ketik:

```python
deactivate
```

> into the terminal.

## 12.3. Managing Packages with pip

> Anda dapat menginstal, memutakhirkan, dan menghapus paket menggunakan program bernama pip. Secara default pip akan menginstal paket dari Python Package Index. Anda dapat menelusuri Indeks Paket Python dengan membukanya di browser web Anda.

> pip memiliki sejumlah subperintah: "install", "uninstall", "freeze", dll. (Lihat panduan Memasang Modul Python untuk dokumentasi lengkap untuk pip.)
> Anda dapat menginstal versi terbaru dari sebuah paket dengan menentukan nama paket:

```python
(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```

> Jika Anda menjalankan kembali perintah ini, pip akan melihat bahwa versi yang diminta telah diinstal dan tidak melakukan apa pun. Anda dapat memberikan nomor versi yang berbeda untuk mendapatkan versi itu, atau Anda dapat menjalankan python -m pip install --upgrade untuk memutakhirkan paket ke versi terbaru:

```python
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```

> python -m pip uninstall diikuti oleh satu atau lebih nama paket akan menghapus paket dari lingkungan virtual.

> python -m pip show akan menampilkan informasi tentang paket tertentu:

```python
(tutorial-env) $ python -m pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
```

> python -m pip list akan menampilkan semua paket yang diinstal di lingkungan virtual:

```python
(tutorial-env) $ python -m pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```

> python -m pip freeze akan menghasilkan daftar serupa dari paket yang diinstal, tetapi hasilnya menggunakan format yang diharapkan oleh python -m pip install.
> Konvensi umum adalah meletakkan daftar ini di file requirements.txt:

```python
(tutorial-env) $ python -m pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```

> Requirement.txt kemudian dapat dikomit ke kontrol versi dan dikirimkan sebagai bagian dari aplikasi. Pengguna kemudian dapat menginstal semua paket yang diperlukan dengan install -r:

```python
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
```

# Getting started with conda

## 1. Starting conda

> Windows
> Dari menu Start, cari dan buka "Anaconda Prompt."

## 2. Managing conda

> Verifikasi bahwa conda diinstal dan dijalankan di sistem Anda dengan mengetik:

```python
conda --version
```

> Perbarui conda ke versi saat ini. Ketik berikut ini :

```python
conda update conda
```

> Jika versi conda yang lebih baru tersedia, ketik y untuk memperbarui:

```python
Proceed ([y]/n)? y
```

## 3. Managing environments

> Conda memungkinkan Anda membuat lingkungan terpisah yang berisi file, paket, dan dependensinya yang tidak akan berinteraksi dengan lingkungan lain.

> Saat Anda mulai menggunakan conda, Anda sudah memiliki lingkungan default bernama base. Anda tidak ingin memasukkan program ke dalam lingkungan dasar Anda. Buat lingkungan terpisah untuk menjaga agar program Anda tetap terisolasi satu sama lain.
>
> 1. Buat lingkungan baru dan instal paket di dalamnya.

> Kami akan memberi nama kepingan salju lingkungan dan menginstal paket BioPython. Di Anaconda Prompt atau di jendela terminal Anda, ketik berikut ini:

```python
conda create --name snowflakes biopython
```

> Conda memeriksa untuk melihat paket tambahan apa ("ketergantungan") yang dibutuhkan BioPython, dan menanyakan apakah Anda ingin melanjutkan:

```python
Proceed ([y]/n)? y
```

## 4. Managing Python

> Saat Anda membuat lingkungan baru, conda menginstal versi Python yang sama dengan yang Anda gunakan saat mengunduh dan menginstal Anaconda. Jika Anda ingin menggunakan versi Python yang berbeda, misalnya Python 3.5, cukup buat lingkungan baru dan tentukan versi Python yang Anda inginkan.
>
> 1. Buat lingkungan baru bernama "snakes yang berisi Python 3.9:

```python
conda create --name snakes python=3.9
```

> Saat conda menanyakan apakah Anda ingin melanjutkan, ketik "y" dan tekan Enter. 2. Aktifkan lingkungan baru:
> Windows: conda activate snakes

> macOS dan Linux: conda activate snakes 3. Verifikasi bahwa snakes environment telah ditambahkan dan aktif:

```python
conda info --envs
```

> 4. verifikasi versi Python mana yang ada di environment Anda saat ini:

```python
python --version
```

> 5. Nonaktifkan snakes environment dan kembali ke environment dasar: "conda aktifkan"

## 5. Managing packages

> Di bagian ini, Anda memeriksa paket mana yang telah Anda instal, memeriksa mana yang tersedia dan mencari paket tertentu dan menginstalnya.
>
> 1. Untuk menemukan paket yang telah Anda instal, aktifkan terlebih dahulu lingkungan yang ingin Anda cari. Lihat di atas untuk perintah untuk mengaktifkan lingkungan ular Anda.

> 2. Periksa untuk melihat apakah paket yang belum Anda instal bernama "beautifulsoup4" tersedia dari repositori Anaconda (harus terhubung ke Internet):

```python
conda search beautifulsoup4
```

> Conda menampilkan daftar semua paket dengan nama itu di repositori Anaconda, jadi kami tahu itu tersedia. 3. Instal paket ini ke lingkungan saat ini:

```python
conda install beautifulsoup4
```

> 4. Periksa untuk melihat apakah program yang baru diinstal ada di environment ini

```python
conda list
```
