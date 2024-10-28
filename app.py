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
    
    # Extract user preferences
    style_framework = data.get('framework')
    page_type = data.get('type')
    components = data.get('components', [])
    js_features = data.get('jsFeatures', [])
    color_palette = data.get('colorPalette')  # Add this line
    
    # Generate webpage using Gemini
    try:
        generated_code = generate_webpage(
            style_framework,
            page_type,
            components,
            js_features,
            color_palette
        )
        if not generated_code:
            return jsonify({'success': False, 'error': 'No content generated'})
        return jsonify({'success': True, 'code': generated_code})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
