from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import json
from math import *

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Safe evaluation context with only allowed functions
SAFE_DICT = {
    'sin': sin, 'cos': cos, 'tan': tan,
    'sqrt': sqrt, 'log': log10, 'ln': log,
    'abs': abs, 'exp': exp, 'ceil': ceil, 'floor': floor,
    'pi': pi, 'e': e,
    '__builtins__': {}
}

class MathCalculator:
    @staticmethod
    def evaluate_expression(expression, x_value):
        """Safely evaluate a mathematical expression"""
        try:
            # Replace symbolic names with their values
            expr = expression.replace('^', '**')
            expr = expr.replace('π', str(pi))
            expr = expr.replace('e', str(e)) if 'e' not in expr or 'exp' not in expr else expr
            
            local_dict = SAFE_DICT.copy()
            local_dict['x'] = x_value
            
            result = eval(expr, {"__builtins__": {}}, local_dict)
            return float(result)
        except:
            return None

    @staticmethod
    def calculate(operation, operand1, operand2=None):
        """Perform basic arithmetic operations"""
        try:
            operand1 = float(operand1)
            operand2 = float(operand2) if operand2 is not None else None
            
            if operation == '+':
                return operand1 + operand2
            elif operation == '-':
                return operand1 - operand2
            elif operation == '×':
                return operand1 * operand2
            elif operation == '÷':
                if operand2 == 0:
                    return None
                return operand1 / operand2
            elif operation == '%':
                return operand1 % operand2
            elif operation == 'pow':
                return operand1 ** operand2
            elif operation == 'sin':
                return sin(operand1)
            elif operation == 'cos':
                return cos(operand1)
            elif operation == 'tan':
                return tan(operand1)
            elif operation == 'sqrt':
                if operand1 < 0:
                    return None
                return sqrt(operand1)
            elif operation == 'log':
                if operand1 <= 0:
                    return None
                return log10(operand1)
            elif operation == 'ln':
                if operand1 <= 0:
                    return None
                return log(operand1)
            else:
                return None
        except:
            return None

    @staticmethod
    def generate_graph_data(expression, x_min, x_max, num_points=1000):
        """Generate x,y data points for graphing"""
        try:
            x_values = np.linspace(x_min, x_max, num_points)
            y_values = []
            
            for x in x_values:
                y = MathCalculator.evaluate_expression(expression, x)
                # Skip very large values
                if y is None or abs(y) > 10000:
                    y_values.append(None)
                else:
                    y_values.append(y)
            
            return x_values.tolist(), y_values
        except Exception as e:
            print(f"Error generating graph: {e}")
            return None, None

# API Routes

@app.route('/api/evaluate', methods=['POST'])
def evaluate():
    """Evaluate an expression at a specific x value"""
    try:
        data = request.json
        expression = data.get('expression', '')
        x_value = float(data.get('x', 0))
        
        result = MathCalculator.evaluate_expression(expression, x_value)
        
        if result is None:
            return jsonify({'error': 'Invalid expression or calculation'}), 400
        
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/calculate', methods=['POST'])
def calculate():
    """Perform a basic calculation"""
    try:
        data = request.json
        operation = data.get('operation', '')
        operand1 = data.get('operand1')
        operand2 = data.get('operand2')
        is_degree = data.get('is_degree', False)
        
        # Convert from degrees to radians if needed
        if is_degree and operation in ['sin', 'cos', 'tan']:
            operand1 = float(operand1) * pi / 180
        
        result = MathCalculator.calculate(operation, operand1, operand2)
        
        if result is None:
            return jsonify({'error': 'Invalid calculation'}), 400
        
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/graph', methods=['POST'])
def graph():
    """Generate graph data for an expression"""
    try:
        data = request.json
        expression = data.get('expression', '')
        x_min = float(data.get('x_min', -10))
        x_max = float(data.get('x_max', 10))
        
        if not expression:
            return jsonify({'error': 'Expression required'}), 400
        
        x_values, y_values = MathCalculator.generate_graph_data(expression, x_min, x_max)
        
        if x_values is None:
            return jsonify({'error': 'Invalid expression'}), 400
        
        return jsonify({
            'x': x_values,
            'y': y_values
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/validate-expression', methods=['POST'])
def validate_expression():
    """Check if an expression is valid"""
    try:
        data = request.json
        expression = data.get('expression', '')
        
        # Try to evaluate at x=0
        result = MathCalculator.evaluate_expression(expression, 0)
        
        if result is None:
            return jsonify({'valid': False, 'message': 'Invalid expression'})
        
        return jsonify({'valid': True, 'message': 'Expression is valid'})
    except Exception as e:
        return jsonify({'valid': False, 'message': str(e)})

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'message': 'Calculator backend is running'})

if __name__ == '__main__':
    print("Starting Advanced Calculator Backend...")
    print("Server running at http://localhost:5000")
    print("Press Ctrl+C to stop")
    app.run(debug=True, port=5000)
