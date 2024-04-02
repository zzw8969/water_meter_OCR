import os
os.environ["CUDA_VISIBLE_DEVICES"] = '0'
from paddleocr import PaddleOCR, draw_ocr
from flask import Flask,request,render_template,jsonify
from PIL import Image
import numpy as np
import cv2
import base64




def base64_to_cv2(b64str):

    data = base64.b64decode(b64str.encode('utf8'))
    data = np.frombuffer(data, np.uint8)
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)
    return data

def recognize_ocr(img):
    ocr = PaddleOCR(det_model_dir='./model/ch_PP-OCRv3_det_infer', rec_model_dir='./model/ch_PP-OCRv4_rec_infer',
                    cls_model_dir='./model/ch_ppocr_mobile_v2.0_cls_infer/',use_angle_cls=True)
    result = ocr.ocr(img)
    return result


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/rec', methods=['POST'])
def process_image():
    # try:
    l=[]
    data = request.get_json()
    base64_image = data.get('img', '')
    image = base64_to_cv2(base64_image)
    res= recognize_ocr(image)
    print(res)
    print('***res0',res[0])

    for r in res[0]:
        l.append(r[1][0])

    return jsonify(l)
    # except Exception as e:
    #     return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7000 )