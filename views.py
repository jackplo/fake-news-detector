from flask import Blueprint, request, url_for, redirect, render_template, flash
import pickle
import pandas as pd
from model.predictions import Prediction

app = Blueprint('fake_news', __name__, template_folder="templates/")

@app.post("/")
@app.get("/")
def main():

    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':

        title = request.form['title']
        text = request.form['text']

        prediction = Prediction.get_prediction(text, convert_to_label=True)

        return render_template('index.html', result=prediction.title(), result_percentage=95)

    return 0

@app.get("/disclaimer")
def disclaimer():
    return render_template('disclaimer.html')

@app.app_errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html'), 404
