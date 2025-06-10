from flask import Flask, request

app = Flask(__name__)

def render_html(filename):
    with open(f'templates/{filename}', encoding='utf-8') as file:
        return file.read(), 200, {'Content-Type': 'text/html'}

@app.route('/')
def index():
    return render_html('index.html')

@app.route('/catalog')
def catalog():
    return render_html('catalog.html')

@app.route('/category1')
def category1():
    return render_html('category1.html')

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        print("Данные формы:")
        print(request.form)
    return render_html('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
