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
@app.route("/recommendation")
def recommendation():

    return render_template("recommendation.html")

# Prediction Results Page
@app.route("/results", methods=["POST"])
def prediction_results():
    form_data = dict(request.form.items())
    unit = form_data['unit']
    trait = form_data['trait']
    item = form_data['component']
    
    # Prep form data for model
    data0 = pd.read_csv("model/0")
    data1 = pd.read_csv("model/1")
    data2 = pd.read_csv("model/2")
    data3 = pd.read_csv("model/3")
    data4 = pd.read_csv("model/4")
    data5 = pd.read_csv("model/5")
    data6 = pd.read_csv("model/6")
    data7 = pd.read_csv("model/7")
    data8 = pd.read_csv("model/8")
    data9 = pd.read_csv("model/9")
    data10 = pd.read_csv("model/10")
    data11 = pd.read_csv("model/11")
    data12 = pd.read_csv("model/12")
    data13 = pd.read_csv("model/13")
    # Generate, transform, and format predictions
    if unit!="none":
        u_t_rec, u_i_rec, u_u_rec = rec.unit_recommendation(unit, data8, data10, data6, data2)
    if trait!="none":
        t_t_rec, t_u_rec = rec.trait_recommendation(trait, data1, data8, data10, data3)
    if item!="none":
        i_i_rec = rec.item_recommendation(item, data13)
    # Render prediction
    return render_template(
        "results.html",
        # Make dynamic values available for rendering with template
        # key=value,
        unit_to_trait = u_t_rec, unit_to_item = u_i_rec, unit_to_unit = u_u_rec, trait_to_trait = t_t_rec, trait_to_unit = t_u_rec, item_to_item = i_i_rec 
    )
