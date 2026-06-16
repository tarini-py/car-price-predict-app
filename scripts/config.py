from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = ROOT / "data" / "cars24-car-price-cleaned-new.csv"
MODEL_PATH = ROOT / "models" / "xgb_car_price_model.pkl"
