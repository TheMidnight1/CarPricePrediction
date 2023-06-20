import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score


# load data
vehicle = pd.read_csv("cars_data.csv")

# prepare data
vehicle = vehicle[vehicle["year"].str.isnumeric()]
vehicle["year"] = vehicle["year"].astype(int)
vehicle = vehicle[vehicle["Price"] != "Ask For Price"]
vehicle["Price"] = vehicle["Price"].str.replace(",", "").astype(int)
vehicle["kms_driven"] = (
    vehicle["kms_driven"].str.split(" ").str.get(0).str.replace(",", "")
)
vehicle = vehicle[~vehicle["fuel_type"].isna()]
vehicle["name"] = vehicle["name"].str.split(" ").str.slice(1, 7).str.join(" ")
vehicle = vehicle.reset_index(drop=True)
vehicle = vehicle[vehicle["Price"] < 6e6].reset_index(drop=True)

# split data and price
X = vehicle.drop(columns="Price")
y = vehicle["Price"]

# split data for train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)

# create one hot encoder
ohe = OneHotEncoder()
ohe.fit(X[["name", "company", "fuel_type"]])


column_trans = make_column_transformer(
    (OneHotEncoder(categories=ohe.categories_), ["name", "company", "fuel_type"]),
    remainder="passthrough",
)

# create liner regressin model
lr = LinearRegression()

pipe = make_pipeline(column_trans, lr)

# fit data
pipe.fit(X_train, y_train)

# save model in file
# pickle.dump(pipe, open("prediction_model.pkl", "wb"))


# predictions = pipe.predict(
#     pd.DataFrame(
#         [["Suzuki Swift", "Maruti", 2019, 100, "Petrol"]],
#         columns=["name", "company", "year", "kms_driven", "fuel_type"],
#     )
# )

y_pred = pipe.predict(X_test)
print(r2_score(y_test, y_pred))
# 64.73280934395884 %
