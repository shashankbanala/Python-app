from flask import Flask, render_template, request, jsonify
import math
import re

app = Flask(__name__)

def evaluate_expression(expression):
    """
    Safely evaluate a mathematical expression.
    Only allows basic math operations and common functions.
    """
    # Remove any whitespace
    expression = expression.strip()
    
    # Define allowed characters and functions
    allowed_chars = set('0123456789+-*/()., ')
    allowed_funcs = ['sin', 'cos', 'tan', 'sqrt', 'log', 'exp', 'abs']
    
    # Check for disallowed characters
    for char in expression:
        if char not in allowed_chars and not any(func in expression for func in allowed_funcs):
            return None, "Invalid characters in expression"
    
    # Replace common mathematical functions
    expression = expression.replace('sin', 'math.sin')
    expression = expression.replace('cos', 'math.cos')
    expression = expression.replace('tan', 'math.tan')
    expression = expression.replace('sqrt', 'math.sqrt')
    expression = expression.replace('log', 'math.log')
    expression = expression.replace('exp', 'math.exp')
    expression = expression.replace('abs', 'abs')
    
    try:
        # Evaluate the expression
        result = eval(expression, {"__builtins__": {}}, {"math": math})
        return result, None
    except Exception as e:
        return None, f"Error evaluating expression: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    
    if not expression:
        return jsonify({'error': 'No expression provided'})
    
    result, error = evaluate_expression(expression)
    
    if error:
        return jsonify({'error': error})
    else:
        return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) # Change port to 80 for standard HTTP access