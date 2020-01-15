from flask import Flask
from handlers.routes import setup_routes
import json


def test_base_route():
    app = Flask(__name__)
    setup_routes(app)
    client = app.test_client()
    url = '/'
    response = client.get(url)
    print(response)
    assert response.get_data() == b'<h1>Hello, welcome to our mock calculator</h1>'
    assert response.status_code == 200

# Added a new comment just to show GitHub Actions
