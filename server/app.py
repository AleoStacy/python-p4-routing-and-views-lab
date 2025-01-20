from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('<h1>Python Operations with Flask Routing and Views</h1>')

@app.route('/print/<string:text>')
def print_string(text):
    print(text)  
    return f'<h1>{text}</h1>'  
@app.route('/count/<int:number>')
def count(number):
    numbers = [str(i) for i in range(1, number + 1)]  
    return '<br>'.join(numbers)  

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operation == '%':
        result = num1 % num2
    else:
        return f"Error: '{operation}' is not a valid operation."

    return f'<h1>Result of {num1} {operation} {num2} = {result}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
