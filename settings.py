import os

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
LABEL_PATH = os.path.join(CUR_DIR, 'utils', 'model', "label_map.pbtxt")
MODEL_PATH = os.path.join(CUR_DIR, 'utils', 'model', "frozen_inference_graph.pb")
EXCEL_FILE = os.path.join(CUR_DIR, 'result.xlsx')
SHEET_NAME = "Beverage"

MARGIN = 10
WEB_CAM = False
TRACK_CYCLE = 40
LOCAL = True
THRESHOLD = 0.8
