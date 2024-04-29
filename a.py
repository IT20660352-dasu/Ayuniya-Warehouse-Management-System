from flask import Flask , render_template ,request
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.models import load_model
import os
from tensorflow.keras.preprocessing import image
model1 = load_model(os.path.join('D:/HairDonation/Models','color.h5'))
model2 = load_model(os.path.join('D:/HairDonation/Models','dandruff.h5'))
model3 = load_model(os.path.join('D:/HairDonation/Models','Bleached.h5'))
model4 = load_model(os.path.join('D:/HairDonation/Models','dryness.h5'))
model5 = load_model(os.path.join('D:/HairDonation/Models','Hair.h5'))
app = Flask(__name__)



@app.route('/')
def Home():
    return  render_template("home.html")

@app.route('/step1', methods=['POST'])
def Hello_word():
    return  render_template("step1.html")

@app.route('/thankyou')
def thankyou():
    return  render_template("thankyou.html")

@app.route('/step1_active', methods=['POST'])
def Hair_detection():
    imagefile = request.files["imagefile"]
    image_path = "./image/" + imagefile.filename
    imagefile.save(image_path)

    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize the image data

    prediction5 = model5.predict(img_array)

    threshold = 0.5

    if prediction5[0][0] < threshold:
                classification = (" This is Not Hair ")
                return render_template ("donateReject.html", prediction=classification )
    else:
                classification = ("  hair")
                return render_template ("next.html", prediction=classification )


@app.route('/step2_active', methods=['POST'])
def upload_file():
    imagefile = request.files["imagefile"]
    image_path = "./image/" + imagefile.filename
    imagefile.save(image_path)

    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize the image data
    prediction1 = model1.predict(img_array)
    prediction3 = model3.predict(img_array)
    prediction4 = model4.predict(img_array)
 

    threshold = 0.5
    if prediction1[0][0] > threshold:
        classification = (" Black Hair ")
        if prediction3[0][0] < threshold:
            classification = (" Black Hair And Not Bleach Hair ")
            if prediction4[0][0] > threshold:
                classification = (" Black Hair And Not Bleach Hair And Dry Hair")
                return render_template ("next2.html", prediction=classification )
            else:
                classification = (" Hair is wet")
                return render_template ("donateReject.html", prediction=classification )
        else:
            classification = ("  Bleached Hair ")
            return render_template ("donateReject.html", prediction=classification )
    else:
        classification = ("Not Black Hair")
        return render_template ("donateReject.html", prediction=classification )
    

@app.route('/new', methods=['POST'])
def Hello_word1():
    return  render_template("step2.html")

@app.route('/new2', methods=['POST'])
def Hello_word2():
    return  render_template("step3.html")



@app.route('/danruff_upload', methods=['POST'])
def Hello_word3():
    imagefile = request.files["imagefile"]
    image_path = "./image/" + imagefile.filename
    imagefile.save(image_path)

    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize the image data

    prediction2 = model2.predict(img_array)

    threshold = 0.5

    if prediction2[0][0] > threshold:
                classification = (" Danruff hair ")
                return render_template ("donateReject.html", prediction=classification )
    else:
                classification = (" Not a danruff hair and you can donate your hair")
                return render_template ("thankyou.html", prediction=classification )






    

if __name__ =="__main__":
    app.run(port =3000,debug=True)