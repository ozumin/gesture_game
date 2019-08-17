import pandas as pd
import random
from flask import Flask, render_template, request
app = Flask(__name__)

words = pd.read_csv('odai.csv')
words = words.as_matrix().tolist()
random.shuffle(words)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        word = words.pop()[0]
        if word.find("<br>") != -1:
            tmp = word.split("<br>")
            return render_template('index.html', word1=tmp[0], word2=tmp[1])
        else:
            return render_template('index.html', word1=word)

if __name__ == '__main__':
    app.run()
