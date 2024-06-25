from flask import Flask, render_template, request
from datetime import datetime

CURRENT_YEAR = datetime.now().year

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a5cba07bdd161408d3a4d5435d4e79b0'

data = ''
text = ''

start_time = datetime.now().second


def check_time():
    global start_time, data
    end_time = datetime.now().second
    if end_time - start_time > 4:
        data = ''
        return data
    else:
        return data


@app.route('/', methods=['POST', 'GET'])
def home():
    global start_time
    # form = CreateForm()
    global data
    if request.method == 'POST':
        new_text = request.form.get('text')
        data += f' {new_text}'
        start_time = datetime.now().second
    return render_template('index.html', current_year=CURRENT_YEAR, data=check_time()), {'Refresh': '5; url=http://127.0.0.1:5003/'}




if __name__ == '__main__':
    app.run(debug=True, port=5003, host='0.0.0.0')
    




