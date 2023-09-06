from flask import Flask, jsonify, request
import pandas as pd
import xgboost as xgb

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def do_prediction():
    json = request.get_json()
    model = xgb.Booster({'nthread': 4})
    model.load_model('model.json')

    df = pd.DataFrame(json, index=[0])
    df['category'] = df["category"].astype("category")
    dmat_reg = xgb.DMatrix(df, enable_categorical=True)

    y_predict = model.predict(dmat_reg)

    result = {"FraudPr" : float(y_predict[0])}
    return jsonify(result)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')