import cv2
import numpy as np                                                            


def canny_edge_detection(image):                                               # Canny algoritmasını kullandım.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur= cv2.GaussianBlur(gray, (3, 3), 0)                                    # daha çok ayrıntıyı tespit etmek için Gaussianın bulanıklaştırma filtresini uuyguladım. 
    kenar = cv2.Canny(blur, 50, 150)                                           
    return kenar


def harris_corner_detection(image1):                                           # Harris corner detection algoritmasını kullandım.
    gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    corner = cv2.cornerHarris(gray, 5, 3, 0.2)
    corner = cv2.dilate(corner, None)
    image_copy = image1.copy()
    image_copy[corner > 0.01 * corner.max()] = [0, 0, 255]
    return image_copy


def segmentation(image2):
    gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)                            # Thresholding algoritmasıyla resmi siyah ve beyaz olacak şekilde iki bölüme ayırdım .
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return thresh


def dehaze(image3):
    gray = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
    dehazed = np.zeros_like(image3, dtype=np.float32)                          # Sisin gitmesi için her pixeli düzelttim.
    for channel in range(3):
        dehazed[:, :, channel] = (image3[:, :, channel] - np.min(image3[:, :, channel])) / \
                                 (np.percentile(gray, 99.9) - np.min(image3[:, :, channel]))
      
    dehazed = np.clip(dehazed, 0, 1) * 255                                     # bazı pixel değerlerini sınırladım.
    return dehazed.astype(np.uint8)


def main():
    
    image  = cv2.imread("resim.jpg")
    image1 = cv2.imread("resim2.jpg")
    image2 = cv2.imread("resim3.jpg")
    image3 = cv2.imread("resim4.jpg")

    while True:
        print("1. Edge Detection")
        print("2. Corner Detection")
        print("3. Segmentation")
        print("4. Dehaze")
        print("5. Exit")

        choice = int(input("Seçiminizi giriniz: "))

        if choice == 1:
            kenar = canny_edge_detection(image)
            cv2.imshow("orijinal resim", image)
            cv2.imshow("Edge detection", kenar)
            cv2.waitKey(0)

        elif choice == 2:
            corner = harris_corner_detection(image1)
            cv2.imshow("orijinal resim",image1)
            cv2.imshow("Corner detection", corner)
            cv2.waitKey(0)

        elif choice == 3:
            tresh = segmentation(image2)
            cv2.imshow("orijinal resim",image2)
            cv2.imshow("Segmentasyon", tresh)
            cv2.waitKey(0)

        elif choice == 4:
            dehazed = dehaze(image3)    
            cv2.imshow("orijinal resim",image3)
            cv2.imshow("Dehaze", dehazed)
            cv2.waitKey(0)

        elif choice == 5:
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()