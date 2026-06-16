import pickle
from scripts.config import MODEL_PATH

# load model
with open(MODEL_PATH, "rb") as f:
    xgb_model = pickle.load(f)

print(xgb_model.predict([[10000, 20, 5, 1, 0, 0]]))
