from flask import Flask,render_template,request,redirect
from torchvision.transforms import transforms
import base64
import io

# import Model Class
from IC.Prediction import color_prediction
from IE.Predict_IC import prediction_enhan

app=Flask(__name__)

@app.route('/')
def HomePage():
    return render_template('HomePage.html')

@app.route('/ImageEnhancement')
def ImageEnhancement():
    return render_template('ImageEnhancement.html')

@app.route('/ImageColorization')
def ImageColorization():
    return render_template('ImageColorization1.html')

@app.route('/predict_image', methods=['POST'])
def predict_image():
    if request.method == "POST":
        input_image = request.files['file']
    if input_image.filename == '':
        print("Image must have a file name")
        return redirect(request.url)
    
    outputimage_t, inputimage_t = color_prediction(input_image)
    outputimage = process(outputimage_t.permute((2,0,1)))
    input_image = process(inputimage_t)

    return render_template(
        'ImageColorization1_result.html', 
        output_data=outputimage,
        image1 = input_image)


@app.route('/predict_enhan', methods=['POST'])
def predict_enhan():
    if request.method == "POST":
        input_image = request.files['file']
    if input_image.filename == '':
        print("Image must have a file name")
        return redirect(request.url)
    
    outputimage_t, input_image_t= prediction_enhan(input_image)
    outputimage = process(outputimage_t)
    input_image = process(input_image_t)

    return render_template(
        'ImageEnhancement_result.html', 
        output_data=outputimage,
        image1 = input_image)


def process(img):    
    pilinputimage=transforms.ToPILImage()(img)
    buffer=io.BytesIO()
    pilinputimage.save(buffer,format='PNG')
    input_image=base64.b64encode(buffer.getvalue()).decode('UTF-8')
    return input_image


if __name__=='__main__':
    app.run(debug=True)

