import cv2

from pyzbar import pyzbar


def detect_qrcode(frame):

    barcodes = pyzbar.decode(frame)
    qrCodeDetector = cv2.QRCodeDetector()
    decodedText, points, _ = qrCodeDetector.detectAndDecode(frame)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 2)

    cv2.imshow("Image", frame)
    cv2.waitKey()


if __name__ == '__main__':

    img = cv2.imread("/media/mensa/Data/Task/TrolleyDetection/train_data/new_train_data/IMG_20200401_141536.jpg")
    detect_qrcode(frame=img)
