from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
    return render_template('index.html')

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        print(request.form)
    return render_template('contacts.html')

@app.route('/catalog', methods=['GET', 'POST'])
def catalog():
    if request.method == 'POST':
        print(request.form)
    return render_template('catalog.html')

@app.route('/category', methods=['GET', 'POST'])
def category():
    if request.method == 'POST':
        print(request.form)
    return render_template('category.html')

if __name__ == '__main__':
    app.run(debug=True)
