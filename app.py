from flask import Flask, request, Response, render_template
from PIL import Image
import io

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/jpgtopng", methods=["GET"])
def jpgtopng():
    return render_template("jpgtopng.html")

@app.route("/pngtojpg", methods=["GET"])
def pngtojpg():
    return render_template("pngtojpg.html")

@app.route("/webptopng", methods=["GET"])
def webptopng():
    return render_template("webptopng.html")

@app.route("/bmptopng", methods=["GET"])
def bmptopng():
    return render_template("bmptopng.html")

@app.route("/pngtopdf", methods=["GET"])
def pngtopdf():
    return render_template("pngtopdf.html")

@app.route("/api/jpgtopng", methods=["POST"])
def jpg_to_png():
    file = request.files["image"]
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    png_image = io.BytesIO()
    img.save(png_image, "PNG")
    png_image.seek(0)
    response = make_response(png_image.getvalue())
    response.headers.set("Content-Type", "image/png")
    response.headers.set("Content-Disposition", "attachment", filename=f"{file.filename.split('.')[0]}.png")
    return response
    
@app.route("/api/pngtojpg", methods=["POST"])
def png_to_jpg():
    file = request.files["image"]
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    jpg_image = io.BytesIO()
    img.save(jpg_image, "JPEG")
    jpg_image.seek(0)
    response = make_response(jpg_image.getvalue())
    response.headers.set("Content-Type", "image/jpeg")
    response.headers.set("Content-Disposition", "attachment", filename=f"{file.filename.split('.')[0]}.jpg")
    return response
    
@app.route("/api/webptopng", methods=["POST"])
def webp_to_png():
    file = request.files["image"]
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    png_image = io.BytesIO()
    img.save(png_image, "PNG")
    png_image.seek(0)
    response = make_response(png_image.getvalue())
    response.headers.set("Content-Type", "image/png")
    response.headers.set("Content-Disposition", "attachment", filename=f"{file.filename.split('.')[0]}.png")
    return response
    
@app.route("/api/bmptopng", methods=["POST"])
def bmp_to_png():
    file = request.files["image"]
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    png_image = io.BytesIO()
    img.save(png_image, "PNG")
    png_image.seek(0)
    response = make_response(png_image.getvalue())
    response.headers.set("Content-Type", "image/png")
    response.headers.set("Content-Disposition", "attachment", filename=f"{file.filename.split('.')[0]}.png")
    return response
    
@app.route("/api/pngtopdf", methods=["POST"])
def png_to_pdf():
    file = request.files["image"]
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    png_image = io.BytesIO()
    img.save(png_image, "PDF")
    png_image.seek(0)
    response = Response(png_image.getvalue())
    response.headers.set("Content-Type", "image/png")
    response.headers.set("Content-Disposition", "attachment", filename=f"{file.filename.split('.')[0]}.png")
    return response  

if __name__ == "__main__":
    app.run()