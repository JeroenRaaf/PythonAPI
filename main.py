from flask import Flask, request, jsonify

app = Flask(__name__)

strings = []


@app.route('/getArray')
def getArray():
    return strings


@app.route('/addToArray', methods=['POST'])
def addToArray():
    data = request.get_json()
    print(data)
    strings.append(data['string'])
    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(debug=True)
