import cv2

from src.object_detection.object_detection_runner import ObjectDetector


def detect_beverage():

    obj_detector = ObjectDetector()

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        detect_img, coordinate, obj_description = obj_detector.detect_object(frame)

        cv2.imshow("Detected beverage", detect_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
            break
    cap.release()


if __name__ == '__main__':

    detect_beverage()
