from flask import Flask, redirect, request, render_template, url_for, redirect
from vocab_dict import vocab
from aux import find_word
import random
import time

app = Flask(__name__)


random.seed(time.time())

@app.route('/', methods = ['POST', 'GET'])
def home():
    status = ""
    color = ""
    right_answer=""
    if request.method == 'POST':
        answer = request.form['answer'].lower()
        question = request.form['question']
        idx = find_word(question, vocab)        
        right_answer = vocab[idx]['spa'] 
        if answer == right_answer:
            status = 'correcto'
            color = 'green'
        else:
            status = 'incorrecto'
            color = 'red'
    
    return render_template('index.html', palabra = vocab[random.randint(0,len(vocab)-1)]['ita'],
                           status = status, color = color, right_answer=right_answer)


    
