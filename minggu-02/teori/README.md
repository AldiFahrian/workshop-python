# BAB 4

## 4. More Control Flow Tools

> Selain pernyataan while yang baru saja diperkenalkan, Python menggunakan pernyataan kontrol aliran biasa yang dikenal dari bahasa lain, dengan beberapa perubahan.

### 4.1 if statements.

> if statments :

```Python
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

```

### 4.2 for Statements.

> Pernyataan **for** di Python sedikit berbeda dari yang biasa gunakan di C atau Pascal. Daripada selalu mengulangi perkembangan aritmatika angka (seperti di Pascal), atau memberi pengguna kemampuan untuk menentukan langkah iterasi dan menghentikan kondisi (sebagai C), pernyataan for Python mengulangi item dari urutan apa pun.

```python
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```

```python
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

```

### 4.3 The range() Function.

> Jika Anda memang perlu mengulangi urutan angka, fungsi built-in **range()** sangat berguna. Ini menghasilkan progresi aritmatika:

```python
for i in range(5):
    print(i)

```

```python
list(range(5, 10))
[5, 6, 7, 8, 9]

list(range(0, 10, 3))
[0, 3, 6, 9]

list(range(-10, -100, -30))
[-10, -40, -70]
```

> Untuk mengulangi indeks urutan, Anda dapat menggabungkan **range()** dan **len()** sebagai berikut:

```python
list(range(5, 10))
[5, 6, 7, 8, 9]

list(range(0, 10, 3))
[0, 3, 6, 9]

list(range(-10, -100, -30))
[-10, -40, -70]
```

> Hal yang aneh terjadi jika Anda hanya mencetak rentang:

```python
range(10)
range(0, 10)
```

> **sum()** dan **range()** juga dapat digabungkan :

```python
sum(range(4))  # 0 + 1 + 2 + 3
6
```

### 4.4 break and continue Statements, and else Clauses on Loops.

> Break statement, seperti di C, keluar dari loop **for** atau **while** yang terlampir terdalam.

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

```

> Perhatikan baik-baik: klausa else milik loop **for**, bukan pernyataan **if**.

> Pernyataan **continue**, juga dipinjam dari C, dilanjutkan dengan iterasi loop berikutnya:

```python
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
```

### 4.5 pass Statements

> Pernyataan pass tidak melakukan apa-apa. Itu dapat digunakan ketika pernyataan diperlukan secara sintaksis tetapi program tidak memerlukan tindakan. Misalnya:

```python
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)
```

> Ini biasanya digunakan untuk membuat kelas minimal:

```python
class MyEmptyClass:
    pass
```

> Pass tempat lain yang dapat digunakan adalah sebagai placeholder untuk fungsi atau badan kondisional saat Anda mengerjakan kode baru, memungkinkan Anda untuk terus berpikir pada tingkat yang lebih abstrak.

```python
def initlog(*args):
    pass   # Remember to implement this!
```

### 4.6 match Statements

> **Pernyataan kecocokan** mengambil ekspresi dan membandingkan nilainya dengan pola berurutan yang diberikan sebagai satu atau beberapa blok kasus. Ini mirip dengan pernyataan switch di C, Java atau JavaScript (dan banyak bahasa lainnya), tetapi lebih mirip dengan pencocokan pola dalam bahasa seperti Rust atau Haskell. Hanya pola pertama yang cocok yang akan dieksekusi dan juga dapat mengekstrak komponen (elemen urutan atau atribut objek) dari nilai menjadi variabel.

> Bentuk paling sederhana membandingkan nilai subjek terhadap satu atau lebih literal:

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

> Anda dapat menggabungkan beberapa literal dalam satu pola menggunakan | ("atau"):

```python
case 401 | 403 | 404:
    return "Not allowed"
```

> pola dapat terlihat seperti tugas membongkar, dan dapat digunakan untuk mengikat variabel:

```python
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```

> Jika Anda menggunakan kelas untuk menyusun data, Anda dapat menggunakan nama kelas diikuti dengan daftar argumen yang menyerupai konstruktor, tetapi dengan kemampuan untuk menangkap atribut ke dalam variabel:

```python
class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
```

### 4.7 Defining Functions

> Kita dapat membuat fungsi yang menulis deret Fibonacci ke batas arbitrer:

```python
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
```

> Definisi fungsi mengaitkan nama fungsi dengan objek fungsi dalam tabel simbol saat ini. Penerjemah mengenali objek yang ditunjuk oleh nama itu sebagai fungsi yang ditentukan pengguna. Nama lain juga dapat menunjuk ke objek fungsi yang sama dan juga dapat digunakan untuk mengakses fungsi tersebut:

```python
fib
<function fib at 10042ed0>
f = fib
f(100)
0 1 1 2 3 5 8 13 21 34 55 89
```

> Sangat mudah untuk menulis fungsi yang mengembalikan daftar angka deret Fibonacci, alih-alih mencetaknya:

```python
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```
