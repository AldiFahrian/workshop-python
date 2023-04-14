# BAB 6 Modules

> Jika Anda keluar dari juru bahasa Python dan memasukkannya lagi, definisi yang Anda buat (fungsi dan variabel) akan hilang. Oleh karena itu, jika Anda ingin menulis program yang agak panjang, lebih baik Anda menggunakan editor teks untuk menyiapkan input untuk juru bahasa dan menjalankannya dengan file tersebut sebagai input. Ini dikenal sebagai membuat skrip. Saat program Anda semakin panjang, Anda mungkin ingin membaginya menjadi beberapa file untuk pemeliharaan yang lebih mudah. Anda mungkin juga ingin menggunakan fungsi praktis yang telah Anda tulis di beberapa program tanpa menyalin definisinya ke setiap program.
> Untuk mendukung ini, Python memiliki cara untuk meletakkan definisi dalam file dan menggunakannya dalam skrip atau dalam contoh interaktif dari juru bahasa. File seperti itu disebut modul; definisi dari modul dapat diimpor ke modul lain atau ke modul utama.
> A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.

```python
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

> Sekarang masukkan juru bahasa Python dan impor modul ini dengan perintah berikut:

```python
>>> import fibo
```

> Ini tidak menambahkan nama fungsi yang didefinisikan di fibo langsung ke namespace saat ini (lihat Python Scopes dan Namespaces untuk detail lebih lanjut); itu hanya menambahkan nama modul fibo di sana. Menggunakan nama modul Anda dapat mengakses fungsi:

```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```

## 6.1. More on Modules

> Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul. Mereka dieksekusi hanya saat pertama kali nama modul ditemukan dalam pernyataan impor. 1 (Mereka juga dijalankan jika file dijalankan sebagai skrip.)
> Ada varian dari pernyataan impor yang mengimpor nama dari modul langsung ke ruang nama modul pengimpor. Misalnya:

```python
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

> Ini tidak memperkenalkan nama modul dari mana impor diambil di namespace lokal (jadi dalam contoh, fibo tidak ditentukan).

> Bahkan ada varian untuk mengimpor semua nama yang ditentukan modul:

```python
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

### 6.1.1. Executing modules as scripts

> Saat Anda menjalankan modul Python dengan

```python
python fibo.py <arguments>
```

> kode dalam modul akan dieksekusi, sama seperti jika Anda mengimpornya, tetapi dengan **name** disetel ke "**main**". Itu artinya dengan menambahkan kode ini di akhir modul Anda:

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

> Anda dapat menjadikan file tersebut dapat digunakan sebagai skrip dan juga sebagai modul yang dapat diimpor, karena kode yang mem-parsing baris perintah hanya berjalan jika modul dijalankan sebagai file "utama":

```python
python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

> If the module is imported, the code is not run:

```python
>>> import fibo
>>>
```

> Ini sering digunakan baik untuk menyediakan antarmuka pengguna yang mudah digunakan ke modul, atau untuk tujuan pengujian (menjalankan modul saat skrip menjalankan rangkaian pengujian).

### 6.1.2. The Module Search Path

> Saat modul bernama spam diimpor, interpreter pertama-tama akan mencari modul bawaan dengan nama tersebut.

> Nama modul ini tercantum dalam sys.builtin_module_names. Jika tidak ditemukan, ia akan mencari file bernama spam.py di daftar direktori yang diberikan oleh variabel sys.path. sys.path diinisialisasi dari lokasi berikut:

> Setelah inisialisasi, program Python dapat memodifikasi sys.path. Direktori yang berisi skrip yang sedang dijalankan ditempatkan di awal jalur pencarian, di depan jalur pustaka standar. Ini berarti skrip di direktori itu akan dimuat alih-alih modul dengan nama yang sama di direktori perpustakaan. Ini adalah kesalahan kecuali penggantian dimaksudkan. Lihat bagian Modul Standar untuk informasi lebih lanjut.

### 6.2. Standard Modules

> Python hadir dengan pustaka modul standar, yang dijelaskan dalam dokumen terpisah, Referensi Pustaka Python (“Referensi Pustaka” selanjutnya).

> Satu modul tertentu patut mendapat perhatian: sys, yang dibangun di setiap juru bahasa Python. Variabel sys.ps1 dan sys.ps2 mendefinisikan string yang digunakan sebagai prompt primer dan sekunder:

```python
>>> import sys
>>> sys.ps1
'>>> '
sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```

> Kedua variabel ini hanya ditentukan jika penafsir berada dalam mode interaktif.
> Variabel sys.path adalah daftar string yang menentukan jalur pencarian modul oleh juru bahasa. Ini diinisialisasi ke jalur default yang diambil dari variabel lingkungan PYTHONPATH, atau dari default bawaan jika PYTHONPATH tidak disetel. Anda dapat memodifikasinya menggunakan operasi daftar standar:

```python
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

### 6.3 The dir() Function

Fungsi built-in dir() digunakan untuk mengetahui nama mana yang didefinisikan oleh modul. Ini mengembalikan daftar string yang diurutkan:

```Python
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']
```

Tanpa argumen, dir() mencantumkan nama yang telah Anda tetapkan saat ini:

```Python
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

dir() tidak mencantumkan nama fungsi dan variabel bawaan. Jika Anda menginginkan daftar itu, mereka ditentukan dalam modul standar bawaan:

```Python
>>> import builtins
>>> dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
```

### 6.4 Packages

Package adalah cara menyusun ruang nama modul Python dengan menggunakan "nama modul bertitik".

Misalkan Anda ingin merancang kumpulan modul ("paket") untuk penanganan file suara dan data suara yang seragam. Ada banyak format file suara yang berbeda (biasanya dikenali dari ekstensinya, misalnya: .wav, .aiff, .au), jadi Anda mungkin perlu membuat dan memelihara koleksi modul yang terus bertambah untuk konversi antara berbagai format file. Ada juga banyak operasi berbeda yang mungkin ingin Anda lakukan pada data suara (seperti mencampur, menambahkan gema, menerapkan fungsi equalizer, membuat efek stereo buatan), jadi selain itu Anda akan menulis aliran modul tanpa henti untuk dilakukan. operasi ini. Berikut adalah kemungkinan struktur untuk paket Anda (dinyatakan dalam sistem file hierarkis):

```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

Pengguna paket dapat mengimpor modul individual dari paket, misalnya:

```Python
import sound.effects.echo
```

Ini memuat submodule sound.efek.echo. Itu harus dirujuk dengan nama lengkapnya

```Python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

Cara alternatif mengimpor submodule adalah:

```Python
from sound.effects import echo
```

Ini juga memuat gema submodule, dan membuatnya tersedia tanpa awalan paketnya, sehingga dapat digunakan sebagai berikut:

```Python
echo.echofilter(input, output, delay=0.7, atten=4)
```

Variasi lainnya adalah mengimpor fungsi atau variabel yang diinginkan secara langsung:

```Python
from sound.effects.echo import echofilter
```

Sekali lagi, ini memuat gema submodule, tetapi ini membuat fungsinya echofilter() langsung tersedia:

```Python
echofilter(input, output, delay=0.7, atten=4)
```
