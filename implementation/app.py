# Python Standard Library Modules
from os import path
import pickle
# 3rd-party installed modules
import pandas
from flask import Flask, render_template, request
# Custom Project Modules (*.py files)
import rec

# Load pre-fitted preprocessors, models, transformers
APP_DIR = path.dirname(path.abspath(__file__))

# repeat for each pickle file
with open(f"{APP_DIR}/model/<FILENAME>", "r") as file:
    variable_name = pickle.load(file)

# Define Flask app
app = Flask(__name__)

# Landing Page
@app.route("/")
def index():
    return render_template("index.html")

# Prediction Form Page
@app.route("/recommendation", methods=["GET"])
def recommendation():

    return render_template("recommendation.html", data=datasets)

# Prediction Results Page
@app.route("/results", methods=["POST"])
def prediction_results():
    
    raw_form_data = request.form
    
    # Prep form data for model
    data0 = pd.read_csv("model/0)
    data1 = pd.read_csv("model/1)
    data2 = pd.read_csv("model/2)
    data3 = pd.read_csv("model/3)
    data4 = pd.read_csv("model/4)
    data5 = pd.read_csv("model/5)
    data6 = pd.read_csv("model/6)
    data7 = pd.read_csv("model/7)
    data8 = pd.read_csv("model/8)
    data9 = pd.read_csv("model/9)
    data10 = pd.read_csv("model/10)
    data11 = pd.read_csv("model/11)
    data12 = pd.read_csv("model/12)
    # Generate, transform, and format predictions
    u_t_rec, u_i_rec, u_u_rec = rec.unit_recommendation('Ryze')
    t_t_rec, t_u_rec = rec.trait_recommendation('Mage')
    i_i_rec = rec.item_recommendation('Chain Vest')
    # Render prediction
    return render_template(
        "results.html",
        # Make dynamic values available for rendering with template
        # key=value,
        unit_by_trait = u_t_rec, 
    )
