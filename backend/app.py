from flask import Flask, jsonify, request
import csv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/phones', methods=['GET'])
def get_phones():
    phones = []
    with open('phone_prices.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            phone_data = {
                'Website': row.get('Website', ''),
                'Phone Name': row.get('Phone Name', ''),
                'Price': row.get('Price', ''),
                'Link': row.get('Link', '')
            }
            phones.append(phone_data)

    return jsonify(phones)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Phone Price Tracker API! Use the /api/phones endpoint to access phone data."

if __name__ == "__main__":
    app.run(debug=True)
