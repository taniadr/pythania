#Home page route (URLS implemented by the app)
#The Handlers here are View Functions 

from app import app

@app.route('/')         
@app.route('/index')
def index():
    user = {'username' : 'Mary'}
    return '''
<html>
    <head>
        <title>Pythania Microblog</title>
    </head>
    <body>
        <h1>Hey you, ''' + user['username'] + '''!</h1>
    </body>
</html>'''