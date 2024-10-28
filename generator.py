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
    
    Please provide your response in the following format:
    ---CODE_START---
    [Your HTML, CSS, and JavaScript code here]
    ---CODE_END---
    
    ---COMMENTS_START---
    [Your explanations and comments here]
    ---COMMENTS_END---
    """
    
    # Initialize Gemini model
    model = genai.GenerativeModel('gemini-1.5-flash-8b')
    
    # Generate response
    response = model.generate_content(prompt)
    if response and response.text:
        # Parse the response to separate code and comments
        text = response.text
        
        # Extract code
        code_start = text.find('---CODE_START---') + 15
        code_end = text.find('---CODE_END---')
        code = text[code_start:code_end].strip() if code_start > 14 and code_end > 0 else text
        
        # Extract comments
        comments_start = text.find('---COMMENTS_START---') + 19
        comments_end = text.find('---COMMENTS_END---')
        comments = text[comments_start:comments_end].strip() if comments_start > 18 and comments_end > 0 else ''
        
        return {
            'code': code,
            'comments': comments
        }
    else:
        raise Exception("Failed to generate webpage content")
