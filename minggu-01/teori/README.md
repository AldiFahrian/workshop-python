# BAB 1

## 1. Python

> Python adalah bahasa pemrograman yang cocok untuk pemula dikarenakan mudah untuk digunakan.

> Python menawarkan lebih banyak struktur dan support untuk program yang lebih besar dari kumpulan file. susunan dan kamus yang fleksibel, dan dikarenakan tipe datanya lebih umum python dapat diterapkan untuk masalah yang lebih besar.

> Python memungkinkan Anda membagi program Anda menjadi modul yang dapat digunakan kembali di program Python lainnya. python juga memungkinkan program ditulis dengan kompak dan mudah dibaca.

> Python adalah bahasa yang ditafsirkan, yang dapat menghemat banyak waktu Anda selama pengembangan program karena tidak diperlukan kompilasi dan penautan.

# BAB 2

## 2. Menggunakan Interpreter Python

> interpreter Python biasanya di install pada /usr/local/bin/python3.11 di mesin yang tersedia.

> Interpreter beroperasi seperti shell Unix: ketika dipanggil dengan input standar yang terhubung ke perangkat tty, ia membaca dan mengeksekusi perintah secara interaktif; ketika dipanggil dengan argumen nama file atau dengan file sebagai input standar, ia membaca dan mengeksekusi skrip dari file itu.

> Secara default, file sumber Python diperlakukan sebagai dikodekan dalam UTF-8. Dalam pengkodean itu, karakter dari sebagian besar bahasa di dunia dapat digunakan secara bersamaan dalam literal string, pengidentifikasi, dan komentar — meskipun perpustakaan standar hanya menggunakan karakter ASCII untuk pengidentifikasi, sebuah konvensi yang harus diikuti oleh kode portabel apa pun.

# BAB 3

## 3. Pengantar Python

> Dalam contoh berikut, input dan output dibedakan dengan ada atau tidaknya prompt (>>> dan …): untuk mengulang contoh, Anda harus mengetik semuanya setelah prompt, saat prompt muncul; baris yang tidak dimulai dengan prompt adalah keluaran dari juru bahasa.

### 3.1. menggunakan python sebagai kalkulator.

```
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating point number
1.6
```

> Dengan Python, dimungkinkan untuk menggunakan operator \*\* untuk menghitung kekuatan :

```
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
```

> Tanda sama dengan (=) digunakan untuk memberikan nilai ke variabel. Setelah itu, tidak ada hasil yang ditampilkan sebelum prompt interaktif berikutnya:

```
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```

> dalam mode interaktif, ekspresi terakhir yang dicetak ditugaskan ke variabel \_. Ini berarti ketika Anda menggunakan Python sebagai kalkulator, akan lebih mudah untuk melanjutkan perhitungan, misalnya:

```
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

### 3.1.2 Strings.

> Selain angka, Python juga bisa memanipulasi string, yang bisa diekspresikan dalam beberapa cara. Mereka dapat diapit dengan tanda kutip tunggal ('...') atau tanda kutip ganda ("...") dengan hasil yang sama 2. \ dapat digunakan untuk menghindari tanda kutip:

```
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
```

> Literal string dapat menjangkau beberapa baris. Salah satu caranya adalah menggunakan tanda kutip tiga: """...""" atau '''...'''. Akhir baris secara otomatis dimasukkan ke dalam string, tetapi hal ini dapat dicegah dengan menambahkan tanda \ di akhir baris. Contoh berikut:

```
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```

> menghasilkan keluaran berikut (perhatikan bahwa baris baru awal tidak disertakan):

```
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
```

> String dapat diindeks (berlangganan), dengan karakter pertama memiliki indeks 0. Tidak ada tipe karakter yang terpisah; karakter hanyalah string ukuran satu:

```
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'
```

> String python tidak dapat diubah/tetap. Oleh karena itu, menugaskan ke posisi terindeks dalam string menghasilkan kesalahan:

```
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

> If you need a different string, you should create a new one:

```
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
```

### 3.1.3 lists.

> Python mengetahui sejumlah tipe data majemuk, yang digunakan untuk mengelompokkan nilai lain. Yang paling serbaguna adalah daftar, yang dapat ditulis sebagai daftar nilai (item) yang dipisahkan koma di antara tanda kurung siku. Daftar mungkin berisi item dari tipe yang berbeda, tetapi biasanya semua item memiliki tipe yang sama.

```
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```

> Seperti string (dan semua jenis urutan bawaan lainnya), daftar dapat diindeks dan dipotong:

```
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
```

> Semua operasi irisan mengembalikan daftar baru yang berisi elemen yang diminta. Ini berarti potongan berikut mengembalikan salinan daftar yang dangkal:

```
squares[:]
[1, 4, 9, 16, 25
```

> Tidak seperti string, yang tidak dapat diubah, daftar adalah jenis yang dapat diubah, artinya kontennya dapat diubah:

```
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
```

> Anda juga dapat menambahkan item baru di akhir daftar, dengan menggunakan metode append() (kita akan melihat lebih banyak tentang metode nanti):

```
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```

> Penugasan ke irisan juga dimungkinkan, dan ini bahkan dapat mengubah ukuran daftar atau menghapusnya seluruhnya:

```
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
```

> Fungsi bawaan len() juga berlaku untuk daftar:

```
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
```

> It is possible to nest lists (create lists containing other lists), for example:

```
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```
