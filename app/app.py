from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/health')
def health():
    return 'OK', 200


@app.route('/data')
def data():
    return jsonify({"message": "Hello from DevOps!"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
