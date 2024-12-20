from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!こんにちは！これは僕の人生初Webアプリだよ！"

if __name__ == "__main__":
    app.run(debug=True)
