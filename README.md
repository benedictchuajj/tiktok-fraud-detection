# Tiktok Fraud Detection ML Model

## Quick Start
1. Clone this repository.
2. Build the docker image:
```
docker build -t fraud-model .
```
3. Run the docker container, exposting port 5000:
```
docker run -d -p 5000:5000 fraud-model
```
4. Invoke the model using curl/any other REST client:
```
curl --location --request POST 'http://localhost:5000/predict' --header 'Content-Type: application/json' --data-raw '{ "category": "travel", "amt": 300, "lat": 40.1362, "long": -95.2138, "merch_lat": 40.591103, "merch_long": -94.445245, "age": 70, "hour": 17, "day": 6, "month": 7 }' 
```

## Model Details:

xgboost model trained using the [Credit Card Fraud Detection](https://www.kaggle.com/datasets/kartik2112/fraud-detection?datasetId=817870&sortBy=voteCount) dataset. 

Dataset imbalanced is tackled using SMOTE.

### Current Performance
Precision: 0.93
Recall: 0.8

### Input
```
{
    "category": category*,
    "amt": float,
    "lat": float,
    "long": float,
    "merch_lat": float,
    "merch_long": float,
    "age": int,
    "hour": int,
    "day": int,
    "month": int
}
```

where category* refers to any categories below:
```
['grocery_pos', 'entertainment', 'shopping_pos', 'misc_pos', 'shopping_net', 'gas_transport', 'misc_net', 'grocery_net', 'food_dining', 'health_fitness', 'kids_pets', 'home', 'personal_care', 'travel']
```

### Output
Probability of whether a single transcation is a fraud transaction
