from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('fetch.html')

@app.route('/async')
def async_index():
    return render_template('fetch_async.html')

@app.route('/randomtext', methods=['GET'])
def randomtext():
    return jsonify({"text": "Hello, world!"})

if __name__ == '__main__':
    app.run(debug=True)
