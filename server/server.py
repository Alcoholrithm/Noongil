from flask import Flask, request
import cv2
import numpy as np
from PIL import Image
from papago import translator
from oscar_scripts.bottom_up_encoder import Encoder
from oscar_scripts.captioning_decoder import Decoder

YAML_PATH = '/workspace/detectron2/configs/VG-Detection/'
CHECKPOINT = '/workspace/checkpoint/'
DEVICE = 'cuda'

encoder = Encoder(YAML_PATH)
decoder = Decoder(CHECKPOINT, DEVICE)
papago = translator()

app = Flask(__name__)

def get_caption(img):
    features, classes = encoder.encode(img)
    captions = decoder.decode(features, classes)
    return captions[0]

@app.route('/', methods = ['POST'])
def main():
    file = request.get_data()
    img = cv2.imdecode(np.frombuffer(file, np.uint8), cv2.IMREAD_UNCHANGED)
    img = np.array([img])
    caption = get_caption(img)
    #print(caption)
    eng = 'There is ' + caption
    kor =  papago.translate(eng)
    #print(kor)
    return kor


app.run(host='0.0.0.0', port=5121)



