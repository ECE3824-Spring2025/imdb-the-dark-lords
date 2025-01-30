from flask import Flask, render_template, url_for, request

app = Flask(__name__) # definng flask app

@app.route('/', methods=['POST','GET']) 
def index_func():

    data = ''
    # check for request data through GET method
    if request.method == 'GET':

        # evalate the choices 
        genre = request.args.get('genre')
        if      genre == 'comedy':
            data = 'SEND COMEDY LIST'

        elif    genre == 'drama':
            data = 'SEND DRAMA LIST'
            
        elif    genre == 'action':
            data = 'SEND ACTION LIST'

        return render_template("index.html",type = data)

if __name__ == "__main__":
    app.run(debug=True)