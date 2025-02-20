from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return 'Welcome to index page'
    return render_template('index.html')



@app.route('/about')
def about():
    # return 'Welcome to about us page'
    return render_template('aboutus.html')

@app.route('/contactus')
def contact():
    # return 'Welcome to about us page'
    return render_template('contactus.html')


if __name__ == '__main__':
    app.run(debug=True,port=4000)