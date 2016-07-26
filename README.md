# did-you-mean

Edit Distance

Bir kelimeyi başka bir kelimeye çevirmek için gerekli olan düzenleme sayısı. Bu düzenlemeler; silme (bir harf silme), yer değişikliği (yan yana olan iki harfin birbiri ile yer değiştirmesi) , harf değişimi (bir harfin baska bir harfe değişimi) veya harf eklenmesi olabilir.

Bizim durumumuzda text trainig yapmiyoruz. Çünkü elimizde tek bir referans var o da txt dosyasıdır. Bu problemde izlenecek yaklaşım; kullanıcının girdiği kelimenin, txt dosyasindaki her kelimeye olan "değişim uzaklığı"nı (edit distance) hesaplayıp en yakın olanını dönmektir. Burada söz konusu olan değişim bir harfin silinmesi/eklenmesi (kaset <-> kase), ardışık iki harfin birbiri ile yer değiştirmesi (akca <-> kaca) veya bir harfin baska bir harf olarak değiştirilmesi (kaç <-> koç) olabilir.

Min Edit Distance

```python
_|_|a|b|c|d|e|f
_|0|1|2|3|4|5|6 0.satır
a|1|0|1|2|3|4|5 1.satır
z|2|1|1|2|3|4|5 2.satır
c|3|2|2|1|2|3|4 3.satır
e|4|3|3|2|2|2|3 4.satır
d|5|4|4|3|2|3|3
```
Satır 0'dan başladığımızda ' ' (boşluk) ile 'abcdef' yazısı arasındaki uzaklığı adım adım ölçmüş oluyoruz.

```python
      |
      V
    _|_|a|b|c|d|e|f
 -> _|0|1|2|3|4|5|6 0.satır  ('' ile '' arasında 0 fark var)
    a|1|0|1|2|3|4|5 1.satır
    z|2|1|1|2|3|4|5 2.satır
    c|3|2|2|1|2|3|4 3.satır
    e|4|3|3|2|2|2|3 4.satır
    d|5|4|4|3|2|3|3
```

```python
        |
      * V
    _|_|a|b|c|d|e|f
 -> _|0|1|2|3|4|5|6 0.satır  ('' ile 'a' arasında 1 fark var, a'nın eklenmesi)
    a|1|0|1|2|3|4|5 1.satır
    z|2|1|1|2|3|4|5 2.satır
    c|3|2|2|1|2|3|4 3.satır
    e|4|3|3|2|2|2|3 4.satır
    d|5|4|4|3|2|3|3
```

```python
          |
      * * V
    _|_|a|b|c|d|e|f
 -> _|0|1|2|3|4|5|6 0.satır  ('' ile 'ab' arasında 2 fark var, a ve b'nin eklenmesi)
    a|1|0|1|2|3|4|5 1.satır
    z|2|1|1|2|3|4|5 2.satır
    c|3|2|2|1|2|3|4 3.satır
    e|4|3|3|2|2|2|3 4.satır
    d|5|4|4|3|2|3|3
```



```python
            |
      * * * V
    _|_|a|b|c|d|e|f
 -> _|0|1|2|3|4|5|6 0.satır  ('' ile 'abc' arasında 3 fark var, a, b ve c'nin eklenmesi)
    a|1|0|1|2|3|4|5 1.satır
    z|2|1|1|2|3|4|5 2.satır
    c|3|2|2|1|2|3|4 3.satır
    e|4|3|3|2|2|2|3 4.satır
    d|5|4|4|3|2|3|3
```
Satir 0'da aynı şekilde ilerlediğimizde sonuç olarak ' ' ile 'abcdef' yazısı arasında 6 değişim olduğunu ve bunun 6 harfin eklenmesi olduğunu görürüz.


Satır 1'e geçtiğimizde:

```python
      |
      V
    _|_|a|b|c|d|e|f
  * _|0|1|2|3|4|5|6 0.satır  
 -> a|1|0|1|2|3|4|5 1.satır ('a' ile '' arasında 1 fark var)
    z|2|1|1|2|3|4|5 2.satır
    c|3|2|2|1|2|3|4 3.satır
    e|4|3|3|2|2|2|3 4.satır
    d|5|4|4|3|2|3|3
```

```python
        |
      * V
    _|_|a|b|c|d|e|f
  * _|0|1|2|3|4|5|6 0.satır  
 -> a|1|0|1|2|3|4|5 1.satır ('a' ile 'a' arasında 0 fark var)
    z|2|1|1|2|3|4|5 2.satır
    c|3|2|2|1|2|3|4 3.satır
    e|4|3|3|2|2|2|3 4.satır
    d|5|4|4|3|2|3|3
```



Değişik olan harf geldiğinde yazacağımız sayıya nasıl karar veriyoruz?
yazacağımız kutunun solu, çaprazı ve üstündeki kutular arasında en küçük değere sahip olan değere 1 eklenir.

```python
|a|b|
|c|X|
```
Yukarıdaki gibi X in yerine yazacağımız değer min(a,b,c)+1 dir.

Yani özetle elimizde az ve abcdef şeklinde iki kelime varsa; birini digerine çevirmek için 5 değişiklik yapmak gerekir.

Satır 2'de bir önceki satırların işlemlerini devam ettiriyoruz. Burada farklı olarak karşılaşacağımız şey aynı harfe denk gelmemiz durumunda yağacağımız değerlendirme.
Yani abc ve azc'deki c harfi. Bu durum ab nin az ye dönmesi ile aynıdır çünkü c harfi bir değişikliğe sebep olmaz. Özetle kutunun çaprazındaki değer alınır.
