from flask import Flask, render_template,request
from keras.models import load_model
import cv2
from cv2 import resize
import numpy as np
import pickle

# store = Store()

# def create_app():
#     app = Flask(__name__)
#     store.init_app(app)
#     app.config['STORE_DOMAIN'] = 'http://127.0.0.1:5000'
#     app.config['STORE_PATH'] = '/some/path/to/somewhere'

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT']=1

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['GET','POST'])
def result():
    img = request.files['file']

    # provider = store.Provider(request.files.get('file'))
    # provider.save()

    img.save('static/file.jpg')

    def get_pixel(img, center, x, y):
        new_value = 0
        try:
            if img[x][y] >= center:
                new_value = 1
        except:
            pass
        return new_value

    def lbp_calculated_pixel(img, x, y):
        center = img[x][y]
        val_ar = []
        val_ar.append(get_pixel(img, center, x - 1, y - 1))
        val_ar.append(get_pixel(img, center, x - 1, y))
        val_ar.append(get_pixel(img, center, x - 1, y + 1))
        val_ar.append(get_pixel(img, center, x, y + 1))
        val_ar.append(get_pixel(img, center, x + 1, y + 1))
        val_ar.append(get_pixel(img, center, x + 1, y))
        val_ar.append(get_pixel(img, center, x + 1, y - 1))
        val_ar.append(get_pixel(img, center, x, y - 1))
        power_val = [1, 2, 4, 8, 16, 32, 64, 128]
        val = 0
        for i in range(len(val_ar)):
            val += val_ar[i] * power_val[i]
        return val

    filename = "finalized_model.sav"
    loaded_model = pickle.load(open(filename, 'rb'))
    image = cv2.imread('static/file.jpg')
    print(image)
    gray_test = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_test = resize(gray_test, (48, 48))
    height, width= gray_test.shape
    img_lbp = np.zeros((height, width),np.uint8)
    for i in range(0, height):
        for j in range(0, width):
            img_lbp[i, j] = lbp_calculated_pixel(gray_test, i, j)
    img_lbp=img_lbp.flatten()
    b=np.bincount(img_lbp)
    FrequencyList=[]
    FrequencyList.append(b)
    x_test = np.array(FrequencyList)
    label_map = ['You seem to be Surprised!', 'What are you afraid of ?', 'What is making you disgusted ?', 'Yippie! You look Happy', 'Why are you looking sad ?', 'Who are you angry at?','You seem Neutral in this picture!']
    prediction = loaded_model.predict(x_test)
    prediction_number = int(prediction[0])
    final_prediction = label_map[prediction_number]
    # return provider.absolute_url
    return render_template('result.html',data=final_prediction)

if __name__ == "__main__":
    app.run(debug=True)
