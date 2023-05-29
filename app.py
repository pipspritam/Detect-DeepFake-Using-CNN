from flask import Flask, render_template, request
from keras.preprocessing.image import ImageDataGenerator
import os
import tensorflow as tf


model = tf.keras.models.load_model("./best_model.h5")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict_deepFake():
    #clean up the data folder if any previous photo is there
    for filename in os.listdir("static/test/"):
        file_path = os.path.join("static/test/", filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)


    uploaded_file = request.files["file"]  # Access the uploaded file
    if uploaded_file:
        file_path = "static/test/" + uploaded_file.filename
        uploaded_file.save(file_path)  # Save the file to the specified path
        os.rename(file_path, "static/test/test_image.jpg")
        
        
    test_datagen = ImageDataGenerator(rescale=1 / 255)

    test_generator = test_datagen.flow_from_directory(
        directory="static",
        target_size=(128, 128),
        color_mode="rgb",
        class_mode=None,
        batch_size=1,
        shuffle=False,
    )

    preds = model.predict(test_generator, verbose=1)

    if preds >= 0.50:
        ans = str(preds) + " Real Image"
    else:
        ans = str(preds) + " Fake Image"
    return render_template("index.html", result=ans)


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=8080)
