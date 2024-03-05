from flask import Flask, render_template, jsonify, request
from agent import run_conversation

app = Flask(__name__)

@app.route("/process_message", methods = ["POST"])
def process_message_func1():
    msg = request.json['message']
    print("Working...", msg)
    resp = run_conversation(msg)
    return jsonify({"response": resp})
    #return jsonify({"response": "How may I help you?"})

@app.route('/')
# def hello_world():
#     return '<hr><marquee><h1>Hello, The Server is Working...</h1></marquee><hr>'
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
