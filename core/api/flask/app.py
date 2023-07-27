from flask import Flask, request
import pickle
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the medical Insurance Prediction API'


@app.route('/predict', methods=['POST'])
def index():
    data_json = request.get_json()['data']
    df = pd.DataFrame(data_json)
    path = r'core/models/model.pkl'

    with open(path, 'rb') as file:
        model = pickle.load(file)

    output = model.predict(df).tolist()
    return output


if __name__ == '__main__':
    app.run()
