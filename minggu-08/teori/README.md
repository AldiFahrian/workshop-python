# BAB 10 Brief Tour of the Standard Library

## 10.1. Operating System Interface

> Modul os menyediakan lusinan fungsi untuk berinteraksi dengan sistem operasi:

```python
>>> import os
>>> os.getcwd()
'C:\\Python311'
>>> os.chdir('/server/accesslogs')
>>> os.system('mkdir today')
0
```

> pastikan untuk menggunakan "import os" , Ini akan menjaga os.open() dari membayangi fungsi built-in open() yang beroperasi jauh berbeda.

```python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>
```

> Untuk tugas manajemen file dan direktori harian, modul shutil menyediakan antarmuka tingkat tinggi yang lebih mudah digunakan:

```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```

## 10.2. File Wildcards

> Modul glob menyediakan fungsi untuk membuat daftar file dari pencarian wildcard direktori:

```python
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```

## 10.3. Command Line Arguments

> skrip utilitas umum seringkali perlu memproses argumen baris perintah

```python
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
```

> Modul argparse menyediakan mekanisme yang lebih canggih untuk memproses argumen baris perintah.

```python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```

## 10.4. Error Output Redirection and Program Termination

> Modul sys juga memiliki atribut untuk stdin, stdout, dan stderr. Yang terakhir berguna untuk memancarkan peringatan dan pesan kesalahan agar terlihat bahkan ketika stdout telah dialihkan:

```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```

## 10.5. String Pattern Matching

```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```

## 10.6. Mathematics

> Modul matematika memberikan akses ke fungsi perpustakaan C yang mendasari untuk matematika floating point:

```python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```

## 10.7. Internet Access

> Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua yang paling sederhana adalah urllib.request untuk mengambil data dari URL dan smtplib untuk mengirim email:

```python
>>> from urllib.request import urlopen
>>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())         # Remove trailing newline

datetime: 2022-01-01T01:36:47.689215+00:00

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
>>> server.quit()
```

## 10.8. Dates and Times

> Modul datetime menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara sederhana dan kompleks. Sementara aritmatika tanggal dan waktu didukung, fokus penerapannya adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi keluaran. Modul ini juga mendukung objek yang sadar zona waktu.

```python

>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```

## 10.9. Data Compression

> Pengarsipan data umum dan format kompresi didukung langsung oleh modul termasuk: zlib, gzip, bz2, lzma, zipfile dan tarfile.

```python
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```

## 10.10. Performance Measurement

> Beberapa pengguna Python mengembangkan minat yang mendalam untuk mengetahui kinerja relatif dari berbagai pendekatan untuk masalah yang sama. Python menyediakan alat pengukuran yang segera menjawab pertanyaan tersebut.

```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```

# BAB 11 Brief Tour of the Standard Library

> Tur kedua ini mencakup modul lanjutan yang mendukung kebutuhan pemrograman profesional. Modul ini jarang muncul dalam skrip kecil.

## 11.1. Output Formatting

> Modul reprlib menyediakan versi repr() yang disesuaikan untuk tampilan singkat dari wadah bersarang besar atau bersarang dalam:

```python
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```

## 11.2. Templating

> Modul string menyertakan kelas Templat serbaguna dengan sintaks sederhana yang cocok untuk diedit oleh pengguna akhir. Ini memungkinkan pengguna untuk menyesuaikan aplikasi mereka tanpa harus mengubah aplikasi.
> Formatnya menggunakan nama placeholder yang dibentuk oleh $ dengan pengidentifikasi Python yang valid (karakter alfanumerik dan garis bawah). Mengelilingi placeholder dengan tanda kurung memungkinkannya diikuti oleh lebih banyak huruf alfanumerik tanpa spasi. Menulis $$ membuat satu $ yang lolos:

```python
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```

## 11.3. Working with Binary Data Record Layouts

> Modul struct menyediakan fungsi pack() dan unpack() untuk bekerja dengan format rekaman biner dengan panjang variabel. Contoh berikut menunjukkan cara mengulang informasi header dalam file ZIP tanpa menggunakan modul zipfile. Kode paket "H" dan "I" masing-masing mewakili dua dan empat byte angka yang tidak ditandatangani. "<" menunjukkan bahwa ukurannya standar dan dalam urutan byte little-endian:

```python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
```

## 11.4. Multi-threading

> Threading adalah teknik untuk memisahkan tugas yang tidak bergantung secara berurutan. Utas dapat digunakan untuk meningkatkan daya tanggap aplikasi yang menerima input pengguna saat tugas lain berjalan di latar belakang. Kasus penggunaan terkait sedang menjalankan I/O secara paralel dengan perhitungan di utas lainnya.

> Kode berikut menunjukkan bagaimana modul threading tingkat tinggi dapat menjalankan tugas di latar belakang sementara program utama terus berjalan:

```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```

## 11.5. Logging

> Modul logging menawarkan sistem logging berfitur lengkap dan fleksibel. Sederhananya, pesan log dikirim ke file atau ke sys.stderr:

```python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```

## 11.6. Weak References

> Python melakukan manajemen memori otomatis (penghitungan referensi untuk sebagian besar objek dan pengumpulan sampah untuk menghilangkan siklus). Memori dibebaskan segera setelah referensi terakhir untuk itu telah dihilangkan.

```python
>>> import weakref, gc
>>> class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

>>> a = A(10)                   # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a            # does not create a reference
>>> d['primary']                # fetch the object if it is still alive
10
>>> del a                       # remove the one reference
>>> gc.collect()                # run garbage collection right away
0
>>> d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entry was automatically removed
  File "C:/python311/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```

## 11.7. Tools for Working with Lists

> Banyak kebutuhan struktur data dapat dipenuhi dengan tipe daftar bawaan. Namun, terkadang ada kebutuhan untuk penerapan alternatif dengan pertukaran kinerja yang berbeda.

> Modul array menyediakan objek array() yang seperti daftar yang hanya menyimpan data homogen dan menyimpannya dengan lebih kompak. Contoh berikut menunjukkan larik angka yang disimpan sebagai angka biner tak bertanda dua byte (kode ketik "H") daripada 16 byte biasa per entri untuk daftar reguler objek int Python:

```python

>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
```

## 11.8. Decimal Floating Point Arithmetic

> Modul desimal menawarkan tipe data Desimal untuk aritmatika floating point desimal. Dibandingkan dengan implementasi float bawaan dari floating point biner, kelas ini sangat membantu
> Misalnya, menghitung pajak 5% untuk biaya telepon 70 sen memberikan hasil yang berbeda dalam floating point desimal dan floating point biner. Perbedaannya menjadi signifikan jika hasilnya dibulatkan ke sen terdekat:

```python
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
```
