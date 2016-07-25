# did-you-mean
did you mean
bayes teoremi

Bir olayın, o olayı etkileyen durumlara dayalı olasılığıdır. Bayes teoremi:

P(A|B) = P(B|A)P(A)/P(B),

A ve B birer olay olmak üzere;

P(A) ve P(B) olayların birbirlerinden bağımsız olarak gerçekleşme olasılıklarıdır.

P(A|B) koşullu olasılıktır, B nin doğru olduğu koşullarda A olayının olasılığıdır

P(B|A) da A’nın doğru olduğu koşullarda B olayının gerçekleşme olasılığıdır.

Bayes teoremini elimizdeki ‘did you mean’ olayına uygulayacak olursak:

Bunu mu demek istediniz servisnin sonucunde bize dönmesini istediğimiz kelimeyi (sonuç) ‘s’ olarak, ve arguman olarak verilen kelimeyi (kelime) ‘k’ olarak sembolize edelim.

olası sonuçlar arasında s’nin en büyük olasılığa sahip olduğu sonucu bulmak istiyoruz.

argmax s P(s|k) (k’nin doğru olduğu koşullarda s’nin olasılığı)

bayes teoremine göre şuna eşit:

argmax s P(k|s) P(s)/P(k)

P(w) olasılığı her olası s için aynıdır bu yüzden ihmal edilebilir.

Sonuç olarak elde edilen ifade:

argmax s P(k|s) P(s)

P(s) → sonuç olarak çıkan kelimenin başlı başına görülme olasılığı. ‘dil modeli’. Bunu “s’nin Türkçe’de görülme olasılığı nedir?” sorusunun cevabı olarak düşünebilriz. Örneğin P(‘bir’) oldukça yüksek bir olasılığa sahip iken P(‘kkkkksksksk’) ın olasılığı sıfıra yakın bir değer alır.

P(k|s) → yazarın s demek istediği yazıda k’nin belirme olasılığı. ‘hata modeli’. Bunu “Yazarın c yazacak iken yanlışlıkla k yazmış olma olasılığı nedir?” sorusunun cevabı olarak düşünebiliriz.

argmax s → kontrol mekanizması. s nin bütün olası sonuçlarını değerlendirip, en iyi kombine edilmiş olasılık skorunun kullanılmasını anlatır.

burada train yapmıyoruz çünkü zaten tek bir kaynağımız var. ve olasılıklar yok

NWORDS[w] her kelimenin kac defa goruldugunu tutuyor.

edit distance

bir kelimeyi baska bir kelimeye cevirmek icin gerekli olan duzenleme sayisi. Bu duzenlemeler; silme (bir harf silme), yer degisikligi (yan yana olan iki harfin birbiri ile yer degistirmesi) , harf degisimi (bir harfin baska bir harfe degisimi) veya harf eklenmesi olabilir.

Bizim durumumuzda text trainig yapmiyoruz. Cunku elimizde tek bir referans var o da txt dosyasidir. Bu problemde izlenecek yaklasim; kullanicinin girdigi kelimenin, txt dosyasindaki her kelimeye olan "degisim uzakligi"ini (edit distance) hesaplayip en yakin olanini donmektir. Burada soz konusu olan degisim bir harfin silinmesi/eklenmesi (kaset <-> kase), ardisik iki harfin birbiri ile yer degistirmesi (akca <-> kaca) veya bir harfin baska bir harf olarak degistirilmesi (kac <-> koc) olabilir.
Min Edit Distance

```python
_|_|a|b|c|d|e|f
_|0|1|2|3|4|5|6
a|1|0|1|2|3|4|5 *
z|2|1|1|2|3|4|5 **
c|3|2|2|1|2|3|4 ***
e|4|3|3|2|2|2|3
d|5|4|4|3|2|3|3
```

* a'yi _'ya cevirmek 1
* a'yi a'ya cevirmek 0
* a'yi ab'ye verimek 1 (b'yi silmek)
* a'yi abc'ye cevirmek 2 (b ve c'yi silmek)
* ...

* * az'yi _ cevirmek 2 (az eklemek)
* * az'yi a'ya cevirmek 1 (z'yi eklemek) 
* * az'yi ab'ye cevirmek 1

degisik olan harf geldiginde yazacagimiz sayiya nasil karar veriyoruz?
yazacagimiz kutunun solu, caprazi ve ustundeki kutular arasinda en kucuk degere sahip olan degere bir eklenir.

|a|b|
|c|X|

yukaridaki gibi X in yerine yazacagimiz deger min(a,b,c)+1 dir.

yani ozetle elimizde az ve abcdef seklinde iki kelime varsa; birini digerine cevirmek icin 5 degisiklik yapmak gerekir.

*** bu satirda da bir onceki satirlarin islemlerini devam ettiriyoruz. burada farkli olarak karsilasagimiz sey ayni harfe denk gelmemiz durumunda yapacagimiz degerlendirme.
Yani abc ve azc'deki c harfi. Bu durum ab nin az ye donmesi ile aynidir cunku c harfi bir degisiklige sebep olmaz. Ozetle kutunun caprazindaki deger alinir.
