import json, ssl, urllib.request
from flask import Flask
from flask import request
from flask import redirect

app = Flask(__name__)
url=''
context=ssl._create_unverified_context()

@app.route('/')
def home():
    html=''
    with open('index.html',"r",encoding="utf-8") as f:
        html = f.read()
    return html

@app.route('/by_theoyu314159', methods=['POST'])
def search():
    url = request.form.get('url')
    with open('index.html',"r",encoding="utf-8") as f:
        html = f.read()
    with urllib.request.urlopen(url, context=context) as jsondata:
        data = json.loads(jsondata.read().decode('utf-8-sig'))
    opt=''
    for i in data:
      opt+=str(data[i])
      opt+='<br><br>'
    return html.replace('<out/>',opt)

app.run(debug=True, host='0.0.0.0')
