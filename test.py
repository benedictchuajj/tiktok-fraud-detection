import pandas as pd
import xgboost as xgb
import json

def do_prediction():
    with open("test.json") as f:
        data = json.load(f)

    model = xgb.Booster({'nthread': 4})
    model.load_model('model.json')
    print("LOADED MODEL")

    df = pd.DataFrame(data, index=[0])
    df['category'] = df["category"].astype("category")
    print(df)
    dmat_reg = xgb.DMatrix(df, enable_categorical=True)
    print("LOADED DATA")

    y_predict = model.predict(dmat_reg)
    print("PREDICTED PROBABILITY")

    result = {"Predicted Fraud Probability" : y_predict[0]}
    return result

if __name__ == "__main__":
    print(do_prediction())