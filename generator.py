import google.generativeai as genai
import os

def generate_webpage(framework, page_type, components, js_features, color_palette, language='en'):
    # Configure the Gemini API
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    
    # Define color schemes
    color_schemes = {
        'modern': 'primary: #2563eb, secondary: #64748b, background: #f8fafc',
        'warm': 'primary: #ea580c, secondary: #92400e, background: #fffbeb',
        'cool': 'primary: #059669, secondary: #0369a1, background: #f0fdfa',
        'minimal': 'primary: #171717, secondary: #404040, background: #ffffff',
        'vibrant': 'primary: #db2777, secondary: #7c3aed, background: #fafafa'
    }
    
    # Construct prompt for Gemini
    prompt = f"""Create a single HTML file in {language} language with:
    Framework: {framework}
    Type: {page_type}
    Components: {', '.join(components)}
    JavaScript features: {', '.join(js_features)}
    Color Palette: {color_schemes.get(color_palette, color_schemes['modern'])}
    
    Include all CSS in a <style> tag and all JavaScript in a <script> tag within the HTML file.
    Please provide your response in the following format:
    ---CODE_START---
    [Your complete HTML file with embedded CSS and JavaScript]
    ---CODE_END---
    """
    
    # Initialize Gemini model
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Generate response
    response = model.generate_content(prompt)
    if response and response.text:
        # Parse the response to get code
        text = response.text
        code_start = text.find('---CODE_START---') + 15
        code_end = text.find('---CODE_END---')
        code = text[code_start:code_end].strip() if code_start > 14 and code_end > 0 else text
        
        return {
            'code': code,
            'comments': ''  # Empty comments since we're not using them
        }
    else:
        raise Exception("Failed to generate webpage content")
