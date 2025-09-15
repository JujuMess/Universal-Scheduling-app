# 🔧 Base image with Python 3.12
FROM python:3.12-slim

# 📂 Set the working directory inside the container
WORKDIR /app

# 📁 Copy everything from your local folder to the container
COPY . .

# 📦 Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 🚀 Run your Flask app
CMD ["python", "scheduling gui.py"]
