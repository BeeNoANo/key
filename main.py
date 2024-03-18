from flask import Flask, request, jsonify
from api import Key
app = Flask(__name__)



@app.route("/create_key", methods=["POST"])
def create_key():
    key = request.args.get("key")
    key_number = request.args.get("amount")
    Key(key).create(key_number)
    return jsonify({"success": True})

@app.route("/get_key", methods=["GET"])
def get_key():
    key = request.args.get("key")
    status = Key(key).check()
    return jsonify({"status": status})

@app.route("/delete_key", methods=["DELETE"])
def delete_key():
    key = request.args.get("key")
    a = Key(key).remove()
    return jsonify({"status": a})

if __name__ == "__main__":
    app.run()
