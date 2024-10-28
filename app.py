from flask import Flask, render_template, request, jsonify
import openai
from generator import generate_webpage
import os

app = Flask(__name__)

# Configure OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    
    # Extract user preferences
    style_framework = data.get('framework')  # bootstrap/tailwind
    page_type = data.get('type')  # landing/portfolio/etc
    components = data.get('components', [])
    js_features = data.get('jsFeatures', [])
    
    # Generate webpage using OpenAI
    try:
        generated_code = generate_webpage(
            style_framework,
            page_type,
            components,
            js_features
        )
        return jsonify({'success': True, 'code': generated_code})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
