from flask import Flask, request, send_file, render_template
from rembg import remove
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part", 400
        
        file = request.files["file"]

        if file.filename == "":
            return "No selected file", 400

        try:
            # Read the image and remove the background
            input_image = Image.open(file)
            input_bytes = BytesIO()
            input_image.save(input_bytes, format="PNG")
            input_bytes.seek(0)

            output_bytes = remove(input_bytes.read())
            output_image = BytesIO(output_bytes)
            output_image.seek(0)

            # Return the image as a file-like object
            return send_file(
                output_image,
                mimetype="image/png",
                as_attachment=False,
                download_name="output_rmbg.png"
            )

        except Exception as e:
            print(f"Error processing image: {e}")
            return "An error occurred while processing the image.", 500

    # Render the main HTML page for GET requests
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
