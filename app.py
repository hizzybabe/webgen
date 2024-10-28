from flask import Flask, render_template, request, jsonify
import os
from generator import generate_webpage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    api_key = request.headers.get('X-API-Key')
    data = request.json
    
    try:
        # Basic API key validation
        if api_key and not api_key.strip():
            return jsonify({'success': False, 'error': 'Invalid API key format'}), 400
            
        generated_content = generate_webpage(
            data.get('framework'),
            data.get('type'),
            data.get('components', []),
            data.get('jsFeatures', []),
            data.get('colorPalette'),
            api_key
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

@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' https://cdn.jsdelivr.net; style-src 'self' https://cdn.jsdelivr.net"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

if __name__ == '__main__':
    app.run(debug=True)
