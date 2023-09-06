# Görüntü İşleme Algoritmaları

## Canny Edge Detection, Harris Corner Detection, Segmentation, Dehazing
Bu proje, Python ve OpenCV kullanarak farklı görüntü işleme algoritmalarını uygulamayı göstermektedir. Aşağıda projede yer alan işlemler hakkında kısa bir açıklama bulunmaktadır.

### Kenar Tespiti (Edge Detection)

`canny_edge_detection(image)` fonksiyonu ile Canny kenar tespit algoritması uygulanır. Bu işlem için resim gri tonlamalı hale getirilir, ardından Gauss bulanıklaştırma filtresi uygulanarak ayrıntılara daha hassas bir şekilde odaklanılır. Son olarak Canny kenar algılama algoritmasıyla kenarlar tespit edilir.

### Köşe Tespiti (Corner Detection)

`harris_corner_detection(image1)` fonksiyonu ile Harris köşe tespit algoritması uygulanır. Resim gri tonlamalı hale getirildikten sonra Harris corner detection algoritmasıyla köşeler belirlenir. Belirlenen köşeler üzerine kırmızı renkle işaretlenmiştir.

### Bölütlemeye Ayırma (Segmentation)

`segmentation(image2)` fonksiyonu ile Thresholding yöntemiyle resim iki bölgeye ayrılır. Resim gri tonlamalı hale getirildikten sonra bir eşik değeri belirlenerek pikseller siyah veya beyaz olarak sınıflandırılır.

### Sis Giderme (Dehaze)

`dehaze(image3)` fonksiyonu ile resimdeki sis etkisi giderilir. Resmin her pikseli düzeltilerek sisin azaltılması sağlanır. Son olarak, bazı piksel değerleri sınırlandırılarak görüntünün daha net hale gelmesi sağlanır.


## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki gereksinimlere ihtiyacınız vardır:
- Python
- OpenCV
- NumPy

## Nasıl Çalıştırılır?

1. OpenCV ve NumPy kütüphanelerini yükleyin.
``` bash 
pip install opencv-python
pip install numpy
```

2. Projeyi GitHub'dan klonlayın veya indirip kaynak kodunu açın.
3. İlgili resim dosyalarını projenin bulunduğu dizine kopyalayın ve `resim.jpg`, `resim2.jpg`, `resim3.jpg` ve `resim4.jpg` adında kaydedin.
4. Proje dosyasının olduğu dizinde terminal veya komut satırını açın ve python main.py komutunu çalıştırın.
5. Program, menüden seçilen işlemleri gerçekleştirerek sonucu gösterecektir.


## ÇIKTILAR
-------------
### Canny Edge Detection
![](https://github.com/nazli-d/goruntu-isleme-algoritmalari/blob/main/outputs/canny-edge-detection.jpg)

### Harris Corner Detection
![](https://github.com/nazli-d/goruntu-isleme-algoritmalari/blob/main/outputs/harris-corner-detection.jpg)

### Segmentation
![](https://github.com/nazli-d/goruntu-isleme-algoritmalari/blob/main/outputs/segmentation.jpg)

### Dehazing
![](https://github.com/nazli-d/goruntu-isleme-algoritmalari/blob/main/outputs/dehazing.jpg)


## Katkıda Bulunma
Bu proje her türlü katkıya açıktır. Katkıda bulunmak için şu adımları takip edebilirsiniz:

1. "Star" butonuna tıklayarak projeye star verebilirsiniz.
2. Bu depoyu (`repository`) çatallayın (fork).
3. Yaptığınız değişiklikleri içeren yeni bir dal (branch) oluşturun.
4. Değişikliklerinizi bu yeni dalda yapın ve düzenleyin.
5. Değişikliklerinizi başka bir dalda test edin.6. Değişikliklerinizi orijinal depoya (upstream repository) geri göndermek için bir birleştirme isteği (pull request) açın.
