from flask import Flask, render_template, request
from API import get_prediction

app = Flask(__name__)

# Path to the trained model
model_path = r"/home/manav/Phishing-Attack-Domain-Detection/models/Malicious_URL_Prediction.h5"

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_result = None

    if request.method == 'POST':
        url = request.form['url']
        prediction_result = get_prediction(url, model_path)

    return render_template('index.html', prediction_result=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)

