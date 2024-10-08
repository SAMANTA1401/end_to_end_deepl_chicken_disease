from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.stage05_prediction_pipeline import PredictionPipeline


os.putenv('LANG','en_us.UTF-8')
os.putenv('LC_ALL','en_us.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

@app.route("/", methods = ['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    # or
    # os.system("dvc repro")
    return "Traininng done successfully"

@app.route("/predict", methods= ['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    clApp = ClientApp()
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)

if __name__=="__main__":
    app.run(host='0.0.0.0', port = 5000)