from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "✅ Deployed Flask 3.0 App via AWS ECS + CodePipeline 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
