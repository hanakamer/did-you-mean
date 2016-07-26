# did-you-mean

Edit Distance

Bir kelimeyi başka bir kelimeye çevirmek için gerekli olan düzenleme sayısı. Bu düzenlemeler; silme (bir harf silme), yer değişikliği (yan yana olan iki harfin birbiri ile yer değiştirmesi) , harf değişimi (bir harfin baska bir harfe değişimi) veya harf eklenmesi olabilir.

Bizim durumumuzda text trainig yapmiyoruz. Çünkü elimizde tek bir referans var o da txt dosyasıdır. Bu problemde izlenecek yaklaşım; kullanıcının girdiği kelimenin, txt dosyasindaki her kelimeye olan "değişim uzaklığı"nı (edit distance) hesaplayıp en yakın olanını dönmektir. Burada söz konusu olan değişim bir harfin silinmesi/eklenmesi (kaset <-> kase), ardışık iki harfin birbiri ile yer değiştirmesi (akca <-> kaca) veya bir harfin baska bir harf olarak değiştirilmesi (kaç <-> koç) olabilir.

Min Edit Distance

```python
_|_|a|b|c|d|e|f
_|0|1|2|3|4|5|6
a|1|0|1|2|3|4|5 x
z|2|1|1|2|3|4|5 xx
c|3|2|2|1|2|3|4 xxx
e|4|3|3|2|2|2|3
d|5|4|4|3|2|3|3
```

x a'yi _'ya çevirmek 1

x a'yi a'ya çevirmek 0

x a'yi ab'ye çevirmek 1 (b'yi silmek)

x a'yi abc'ye çevirmek 2 (b ve c'yi silmek)

x ...


xx az'yi _ çevirmek 2 (az eklemek)

xx az'yi a'ya çevirmek 1 (z'yi eklemek) 

xx az'yi ab'ye çevirmek 1


Değişik olan harf geldiğinde yazacağımız sayıya nasıl karar veriyoruz?
yazacağımız kutunun solu, çaprazı ve üstündeki kutular arasında en küçük değere sahip olan değere 1 eklenir.

```python
|a|b|
|c|X|
```
Yukarıdaki gibi X in yerine yazacağımız değer min(a,b,c)+1 dir.

Yani özetle elimizde az ve abcdef şeklinde iki kelime varsa; birini digerine çevirmek için 5 değişiklik yapmak gerekir.

xxx Bu satırda da bir önceki satırların işlemlerini devam ettiriyoruz. Burada farklı olarak karşılaşacağımız şey aynı harfe denk gelmemiz durumunda yağacağımız değerlendirme.
Yani abc ve azc'deki c harfi. Bu durum ab nin az ye dönmesi ile aynıdır çünkü c harfi bir değişikliğe sebep olmaz. Özetle kutunun çaprazındaki değer alınır.
