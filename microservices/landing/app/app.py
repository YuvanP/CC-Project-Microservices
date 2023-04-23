from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

# def add(n1, n2):
#     return n1+n2

# def minus(n1, n2):
#     return n1-n2

# def multiply(n1, n2):
#     return n1*n2

# def divide(n1, n2):
#     return n1/n2

@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    
    if number_1 == None:
        number_1 = 0
    else:
        number_1 = int(number_1)
        
    if number_2 == None:
        number_2 = 0   

    else:
        number_2 = int(number_2)

    operation = request.form.get('operation')
    result = 0
    if operation == 'add':
        result = requests.get('http://addition:5051/add/'+str(number_1) +'/'+str(number_2)).text
    elif operation == 'minus':
        result =  requests.get('http://subtraction:5053/sub/'+str(number_1) +'/'+str(number_2)).text
    elif operation == 'multiply':
        result = requests.get('http://multiplication:5052/mul/'+str(number_1) +'/'+str(number_2)).text
    elif operation == 'divide':
        result = requests.get('http://division:5054/div/'+str(number_1) +'/'+str(number_2)).text
    elif operation == 'equal':
        result = requests.get('http://equalto:5055/equalto/'+str(number_1) +'/'+str(number_2)).text
    elif operation == 'exponent':
        result = requests.get('http://exponent:5056/exponent/'+str(number_1) +'/'+str(number_2)).text
    elif operation == 'modulus':
        result = requests.get('http://modulus:5057/modulus/'+str(number_1) +'/'+str(number_2)).text

    if result != None:
        flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )