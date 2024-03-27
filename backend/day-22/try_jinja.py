from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the home page!'

@app.route('/about')
def about():
    title = 'About Us'
    content = 'Welcome to our About Us page!'
    return render_template('index.html', title=title, content=content)

if __name__ == '__main__':
    app.run()