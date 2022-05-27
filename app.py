import requests

from flask import Flask, request, jsonify
from flask_caching import Cache

from config import get_settings

app = Flask(__name__)
settings = get_settings()
app.config.from_object(settings)
cache = Cache(app)

@app.route("/universities")
@cache.cached(timeout=30, query_string=True)
def get_universities():
    API_URL = "http://universities.hipolabs.com/search?country="
    search = request.args.get('country')
    r = requests.get(f"{API_URL}{search}")
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)

    

