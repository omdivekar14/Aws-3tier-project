from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    try:
        connection = mysql.connector.connect(
            host='your-rds-endpoint',  # Replace with your RDS endpoint later
            user='admin',
            password='Admin123!',
            database='mydatabase'
        )
        if connection.is_connected():
            return "✅ Flask App connected to AWS RDS successfully!"
    except Exception as e:
        return f"❌ Database connection failed: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
