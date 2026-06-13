# Base image - python + os
FROM python:3.13-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY apps/flask_app.py .
COPY models/xgb_car_price_model.pkl ./models/

# Tell Docker that the container listens on port 5000
EXPOSE 5000

# # Run the Flask app (Make sure host is 0.0.0.0!) : dev server
# CMD ["python", "flask_app.py"]

# Run Gunicorn for Production environment
CMD ["gunicorn", "-b", "0.0.0.0:5000", "flask_app:app"]