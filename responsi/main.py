from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://admin:adminpass@cluster0.scwbbeq.mongodb.net/inventory?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route("/")
def home():
    inventories = mongo.db.inventory.find({})
    return render_template('index.html', inventories = inventories)