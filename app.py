from flask import Flask, redirect, render_template, request
from bs4 import BeautifulSoup
import re, requests, json, os
from dotenv import load_dotenv

from helpers import createPage, apology, getImage

load_dotenv()

app = Flask(__name__, template_folder="templates")

token = os.getenv("token")
databaseId = os.getenv("databaseId")

headers = {
    "Content-type": "application/json",
    "Authorization": "Bearer " + token,
    "Notion-Version": "2022-02-22"
}

proteinlist = ['beef', 'chicken', 'pork', 'lamb', 'fish', 'salmon', 'cod', 'tuna', 
    'mackerel', 'egg', 'eggs', 'tofu', 'lentils', 'sausage', 'chickpeas', 'ham']
vegetablelist = ['pepper', 'peppers', 'zucchini', 'courgette', 'artichoke', 'kale', 'spinach', 
    'broccoli', 'cauliflower', 'corn', 'tomato', 'mushrooms', 'fennel', 'carrots']
dairylist = ['yogurt', 'cheese', 'feta', 'parmesan']
otherslist = ['miso', 'gochugaru', 'tahini']
carbslist = ['pasta', 'rice', 'beans', 'spaghetti', 'noodles', 'soup']

joinedlist = proteinlist + vegetablelist + dairylist + otherslist + carbslist

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/record", methods=["GET", "POST"])
def record():

    # User reached route via POST (as by submitting a form)
    if request.method == "POST":

        '''Get URl of BA recipe'''
        urlInput = request.form.get("link")
        if not urlInput:
            return apology("Invalid link", 400)
        # Request to website and download HTML contents
        req = requests.get(urlInput)
        content = req.text
        if not content:
            return apology("No HTML from site", 400)

        # Format downloaded content into readable format
        # Pass in parser 
        soup = BeautifulSoup(content, features="html.parser")

        # To find the header
        title = soup.find("h1", {"data-testid": "ContentHeaderHed"})
        titleInput = title.text
        #print(title.text)
        if not titleInput:
            return apology("Recipe does not have title", 400)

        # To find ingredients
        ingredients = soup.find_all(class_='Description-dSNklj')
        ingredientlist = []

        for ingredient in ingredients:
            text = ingredient.text
            text = re.sub(",", "", text)
        
            # Split text for .remove method to work
            words = text.split()

            for word in words:
                if word in joinedlist and word not in ingredientlist:
                    ingredientlist.append(word)

        # Create single comma-separated string from ingredientlist to be inputted as text
        ingredientsInput = ",".join(ingredientlist)
        #print(ingredientsInput)
        if not ingredientsInput:
            return apology("Recipe does not have ingredients", 400)

        result = createPage(databaseId, headers, titleInput, ingredientsInput, urlInput)
        if result != 200:
            return apology("Recipe did not get recorded", 400)

        # Show image of recorded recipe
        image = getImage(urlInput)

        return render_template("recorded.html", titleInput=titleInput, image=image)
    
    if request.method == "GET":
        return render_template("record.html")