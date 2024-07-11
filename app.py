from flask import Flask
from routes import setup_routes

app = Flask(__name__)
setup_routes(app)

if __name__ == '__main__':
    app.run(host='192.168.29.216', port=5000, debug=True)
