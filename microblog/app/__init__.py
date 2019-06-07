from flask import Flask

app = Flask(__name__)

from app import routes

#module imported at the bottom:
#this is for handling circular imports problems