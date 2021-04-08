from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<page_name>')
def page_not_found(page_name):
    response = make_response('The page named %s was not found.' % page_name, 404)
    return response

if __name__ == '__main__':
    app.run(debug=True)