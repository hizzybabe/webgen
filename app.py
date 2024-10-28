from flask import Flask, render_template, request, jsonify
import os
from generator import generate_webpage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    
    try:
        generated_content = generate_webpage(
            data.get('framework'),
            data.get('type'),
            data.get('components', []),
            data.get('jsFeatures', []),
            data.get('colorPalette'),
            data.get('apiKey')
        )
        if not generated_content:
            return jsonify({'success': False, 'error': 'No content generated'})
        return jsonify({
            'success': True, 
            'code': generated_content['code'],
            'comments': generated_content['comments']
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
