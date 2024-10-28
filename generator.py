import google.generativeai as genai
import os

def generate_webpage(framework, page_type, components, js_features, color_palette):
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
    prompt = f"""Create a webpage with:
    Framework: {framework}
    Type: {page_type}
    Components: {', '.join(components)}
    JavaScript features: {', '.join(js_features)}
    Color Palette: {color_schemes.get(color_palette, color_schemes['modern'])}
    
    Please use the specified color palette throughout the design and provide complete HTML, CSS, and JavaScript code.
    """
    
    # Initialize Gemini model
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Generate response
    response = model.generate_content(prompt)
    
    return response.text
