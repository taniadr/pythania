#Home page route (URLS implemented by the app)
#The Handlers here are View Functions 

from app import app

@app.route('/')         
@app.route('/index')
def index():
    return "Hello, World!"

