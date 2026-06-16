# Base image - python + os
FROM python:3.13-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY apps/flask_app.py .
COPY models/xgb_car_price_model.pkl ./models/

# Tell Docker that the container listens on port 80
EXPOSE 80

# # Run the Flask app (Make sure host is 0.0.0.0!) : dev server
# CMD ["python", "flask_app.py"]

# Default to 1 workers(vertical scaling) if nothing is passed, but allow overrides like below command
# docker run -p 80:5000 -e WORKERS=5 image_name
ENV WORKERS=1

# Run Gunicorn using the environment variable for Production environment
CMD ["/bin/sh", "-c", "gunicorn -w $WORKERS -b 0.0.0.0:80 flask_app:app"]