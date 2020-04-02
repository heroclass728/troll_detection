import numpy as np
import sys
import tensorflow as tf
import cv2

from src.object_detection.detect_utils import visualization_utils as vis_util
from src.object_detection.detect_utils import label_map_util
from settings import LABEL_PATH, MODEL_PATH, THRESHOLD


class ObjectDetector:

    def __init__(self):
        label_map = label_map_util.load_labelmap(LABEL_PATH)
        self.categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=sys.maxsize,
                                                                         use_display_name=True)
        self.CATEGORY_INDEX = label_map_util.create_category_index(self.categories)
        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(MODEL_PATH, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
        self.threshold = THRESHOLD

    def detect_object(self, frame):
        im_width = frame.shape[1]
        im_height = frame.shape[0]
        with self.detection_graph.as_default():
            with tf.Session(graph=self.detection_graph) as sess:
                image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
                detection_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
                detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
                detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
                num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')

                image_expanded = np.expand_dims(frame, axis=0)

                (boxes, scores, classes, num) = sess.run(
                    [detection_boxes, detection_scores, detection_classes, num_detections],
                    feed_dict={image_tensor: image_expanded})

                vis_util.visualize_boxes_and_labels_on_image_array(
                    frame,
                    np.squeeze(boxes),
                    np.squeeze(classes).astype(np.int32),
                    np.squeeze(scores),
                    self.CATEGORY_INDEX,
                    min_score_thresh=self.threshold,
                    use_normalized_coordinates=True,
                    line_thickness=3)

                object_coordinate = []
                object_description = []
                for box, obj_class, score in zip(boxes[0], classes[0], scores[0]):

                    if score >= self.threshold:
                        y_min, x_min, y_max, x_max = box
                        if y_min != 0 and x_min != 0 and y_max != 0 and y_min != 0:
                            object_coordinate.append((int(x_min * im_width), int(y_min * im_height),
                                                      int(x_max * im_width), int(y_max * im_height)))
                            object_description.append(obj_class)

        return frame, object_coordinate, object_description


def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    if image.getdata().mode != "RGB":
        image = image.convert('RGB')
    return np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)


if __name__ == '__main__':

    object_detector = ObjectDetector()
    img = cv2.imread("/media/mensa/Data/Task/TrolleyDetection/train_data/new_train_data/35.jpg")
    detected_frame, _, _ = object_detector.detect_object(frame=img)
    cv2.imwrite("object detected frame.jpg", detected_frame)
