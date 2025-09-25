FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

RUN pip install --no-cache-dir flask

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

CMD ["python3", "main.py"]