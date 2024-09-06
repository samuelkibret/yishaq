import os
from flask import Flask , render_template
from Buttons import Base_btns , Buildings_btns , Elements_btns , Material_btns
from img import Base_img , Building_img , Elements_img , Material_img
from text import Base_txt , Building_txt , Elements_txt , Material_txt

images = [
        'static/General.png',
        'static/map.png',
        'static/History/Evolution.png',
        # Add more image paths as needed
    ]


app = Flask(__name__)
@app.template_global()
def text_reader(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file at {file_path} does not exist.")
        
        with open(file_path, 'r') as file:
            return file.read()
    
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return None 
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None 
@app.route('/')
def home():
   return render_template('Base.html',Base = Base_btns , img = Base_img , txt = Base_txt, enumerate=enumerate)
@app.route('/Buildings')
def Buildings():
   return render_template('Buildings.html', Base = Buildings_btns , img = Building_img , txt = Building_txt,enumerate=enumerate)
@app.route('/Elements')
def Elements():
   return render_template('Elements.html',Base = Elements_btns , img = Elements_img , txt = Elements_txt,enumerate=enumerate)
@app.route('/Material')
def Materials():
   return render_template('Materials.html',Base = Material_btns , img = Material_img ,txt = Material_txt,enumerate=enumerate)
@app.route('/About')
def About():
   return render_template('horizontal.html', images = images)
@app.route('/Search')
def Search():
   return render_template('404.html' , images = images)
if __name__ == '__main__':
   app.run(debug = True)