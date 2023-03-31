# BAB 5

## 5.1 More on Lists

> Berikut adalah daftar semua metode objek :

- list.**append**(x)
  > Menambahkan item ke akhir daftar.
- list.**extend**(iterable)
  > Memperpanjang daftar dengan menambahkan semua item dari iterable.
- list.**insert**(i, x)
  > Memasukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen sebelum disisipkan.
- list.**remove**(x)
  > Menghapus item pertama dari daftar yang nilainya sama dengan x. Itu memunculkan **ValueError** jika tidak ada item seperti itu.
- list.**pop**([i])
  > Menghapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop() menghapus dan mengembalikan item terakhir dalam daftar.
- list.**clear**()
  > Menghapus semua item dari daftar.
- list.**index**(x[, start[, end]])
  > Mengembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x. Menimbulkan **ValueError** jika tidak ada item tersebut.
- list.**count**(x)
  > Mengembalikan berapa kali x muncul dalam daftar.
- list.**reverse**()
  > Membalik elemen pada list.
- list.**copy**()
  > Mengembalikan nilai copy dari list

> Contoh yang menggunakan sebagian besar metode daftar:

```Python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting at position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
```

## 5.1.1 Using list as Stacks.

> Metode daftar membuatnya sangat mudah untuk menggunakan daftar sebagai tumpukan, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil (“last-in, first-out”). Untuk menambahkan item ke bagian atas tumpukan, gunakan append(). Untuk mengambil item dari atas tumpukan, gunakan pop() tanpa indeks eksplisit. Misalnya:

```Python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

## 5.1.2. Using Lists as Queues

> Dimungkinkan juga untuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil (“first-in, first-out”); namun, daftar tidak efisien untuk tujuan ini. Sementara menambahkan dan muncul dari akhir daftar cepat, melakukan sisipan atau muncul dari awal daftar lambat (karena semua elemen lain harus digeser satu).

```Python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
>>> deque(['Michael', 'Terry', 'Graham'])
```

## 5.1.3 List Comprehensions

> Pemahaman daftar menyediakan cara ringkas untuk membuat daftar. Aplikasi umum adalah membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota urutan lain atau iterable, atau untuk membuat urutan elemen yang memenuhi kondisi tertentu.
> Sebagai contoh, asumsikan kita ingin membuat daftar kuadrat :

```Python
>>> squares = []
>>> for x in range(10):
...    squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

> Perhatikan bahwa ini membuat (atau menimpa) variabel bernama x yang masih ada setelah loop selesai. Kami dapat menghitung daftar kotak tanpa efek samping menggunakan:

```Python
squares = list(map(lambda x: x**2, range(0)))
```

> a tau menggunakan :

```Python
squares = [x**2 for x in range(10)]
```

> yang mana lebih ringkas dan mudah dibaca

## 5.1.4. Nested List Comprehensions

> Ekspresi awal dalam pemahaman daftar dapat berupa sembarang ekspresi, termasuk pemahaman daftar lainnya.
> Pertimbangkan contoh matriks 3x4 berikut yang diimplementasikan sebagai list :

```Python
>>> matrix = [
...    [1, 2, 3, 4],
...    [5, 6, 7, 8],
...    [9, 10, 11, 12],
... ]
```

> daftar comprehension berikut akan transpose row dan column :

```Python
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

> Seperti yang kita lihat di bagian sebelumnya, pemahaman daftar dalam dievaluasi dalam konteks for yang mengikutinya, jadi contoh ini setara dengan:

```Python
>>> transposed = []
>>> for i in range(4):
...    transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

> Yang juga sama dengan :

```Python
>>> transposed = []
>>> for i in range(4):
...    # the following 3 lines implement the nested listcomp
...    transposed_row = []
...    for row in matrix:
...        transposed_row.append(row[i])
...    transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

> Di dunia nyata, Anda harus memilih fungsi bawaan daripada pernyataan alur yang kompleks. Fungsi zip() akan bekerja dengan baik untuk kasus penggunaan ini:

```Python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

## 5.2 The del statement

> Ada cara untuk menghapus item dari daftar yang diberikan indeksnya alih-alih nilainya: pernyataan del. Ini berbeda dari metode pop() yang mengembalikan nilai. Pernyataan del juga dapat digunakan untuk menghapus irisan dari daftar atau menghapus seluruh daftar (yang kita lakukan sebelumnya dengan menugaskan daftar kosong ke irisan). Misalnya:

```Python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

**del** juga bisa digunakan untuk menghapus seluruh variabel :

```Python
>>> del a
```

## 5.3 Tuples and Sequences

> Kita melihat bahwa daftar dan string memiliki banyak properti umum, seperti operasi pengindeksan dan pemotongan.

> tuple terdiri dari sejumlah nilai yang dipisahkan dengan koma, misalnya:

```Python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

## 5.4 Sets

> Python juga menyertakan tipe data untuk set. Himpunan adalah koleksi tak terurut tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Set objek juga mendukung operasi matematika seperti penyatuan, persimpangan, perbedaan, dan perbedaan simetris.

```Python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words

>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

Seperti list comprehension, set comprehension juga dapat melakukan :

```Python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```

## 5.5 Dictionaries

> Tipe data built-in berguna lainnya yaitu dictionaries. Dictionaries kadang-kadang ditemukan dalam bahasa lain sebagai "associative memories" or "associative arrays". Tidak seperti urutan, yang diindeks oleh rentang angka, kamus diindeks oleh kunci, yang dapat berupa tipe apa pun yang tidak dapat diubah; string dan angka selalu bisa menjadi kunci.

Berikut contoh menggunakan dictionaries :

```Python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

> Konstruktor dict() membangun kamus langsung dari urutan pasangan kunci-nilai :

```Python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

> elain itu, pemahaman dict dapat digunakan untuk membuat kamus dari ekspresi kunci dan nilai arbitrer:

```Python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

```

> Saat kunci berupa string sederhana, terkadang lebih mudah untuk menentukan pasangan menggunakan argumen kata kunci:

```Python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

## 5.6 Looping Technique

> Saat mengulang melalui kamus, kunci dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan metode items().

```Python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...    print(k, v)

gallahad the pure
robin the brave
```

> Saat mengulang urutan, indeks posisi dan nilai terkait dapat diambil pada saat yang sama menggunakan fungsi enumerate().

```Python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...    print(i, v)
...
0 tic
1 tac
2 toe
```

> Untuk mengulangi dua urutan atau lebih pada saat yang sama, entri dapat dipasangkan dengan fungsi zip().

```Python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...    print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

> Untuk mengulangi urutan secara terbalik, pertama tentukan urutan dalam arah maju dan kemudian panggil fungsi reversed() .

```Python
>>> for i in reversed(range(1, 10, 2)):
...    print(i)
...
9
7
5
3
1
```

> Untuk mengulangi urutan dalam urutan terurut, gunakan fungsi sortir() yang mengembalikan daftar terurut baru sambil membiarkan sumbernya tidak berubah.

```Python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...    print(i)
...
apple
apple
banana
orange
orange
pear
```

## 5.7. More on Conditions

> Kondisi yang digunakan dalam pernyataan while dan if dapat berisi operator apa saja, bukan hanya perbandingan.
> Operator pembanding in dan not in adalah uji keanggotaan yang menentukan apakah suatu nilai ada di dalam (atau tidak di dalam) wadah. Operator adalah dan tidak membandingkan apakah dua objek benar-benar objek yang sama. Semua operator pembanding memiliki prioritas yang sama, yang lebih rendah dari semua operator numerik.

> Perbandingan dapat dirantai. Misalnya, a < b == c menguji apakah a kurang dari b dan terlebih lagi b sama dengan c.

> Perbandingan dapat digabungkan menggunakan operator Boolean dan dan atau, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat ditiadakan dengan not. Ini memiliki prioritas lebih rendah daripada operator pembanding; di antara mereka, tidak memiliki prioritas tertinggi dan atau terendah, sehingga A dan bukan B atau C setara dengan (A dan (bukan B)) atau C. Seperti biasa, tanda kurung dapat digunakan untuk menyatakan komposisi yang diinginkan.

> Operator Boolean dan dan atau disebut operator hubung singkat: argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Misalnya, jika A dan C benar tetapi B salah, A dan B dan C tidak mengevaluasi ekspresi C. Ketika digunakan sebagai nilai umum dan bukan sebagai Boolean, nilai kembalian dari operator hubung singkat adalah yang terakhir argumen yang dievaluasi.

> Dimungkinkan untuk menetapkan hasil perbandingan atau ekspresi Boolean lainnya ke variabel. Misalnya :

```Python
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```

## 5.8 Comparing Sequence and Other Types

> objek persamaan biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingannya menggunakan urutan leksikografis: pertama dua item pertama dibandingkan, dan jika berbeda, ini menentukan hasil perbandingan; jika sama, dua item berikutnya dibandingkan, dan seterusnya, sampai salah satu urutannya habis. Jika dua item yang akan dibandingkan itu sendiri adalah urutan dari jenis yang sama, perbandingan leksikografis dilakukan secara rekursif.

> Beberapa contoh perbandingan antar barisan yang sejenis:

```Python
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```
