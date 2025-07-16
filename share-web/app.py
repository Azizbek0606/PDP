from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    uploaded_file = request.files["zipfile"]
    if uploaded_file.filename.endswith(".zip"):
        save_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
        uploaded_file.save(save_path)
        return f"✅ Fayl saqlandi: {uploaded_file.filename}"
    return "❌ Faqat .zip fayl yuklang!", 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
