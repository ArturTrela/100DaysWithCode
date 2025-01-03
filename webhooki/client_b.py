from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Odebrano dane: {data}")
    return jsonify({"status": "success", "message": "Dane odebrane"}), 200

if __name__ == '__main__':
    app.run(port=5000)