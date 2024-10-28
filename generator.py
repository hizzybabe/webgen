import google.generativeai as genai
import os

def generate_webpage(framework, page_type, components, js_features, color_palette, api_key=None):
    # Sanitize and validate API key
    api_key_to_use = None
    if api_key and api_key.strip():
        api_key_to_use = api_key.strip()
    else:
        api_key_to_use = os.getenv('GEMINI_API_KEY')

    if not api_key_to_use:
        raise ValueError("No valid API key provided. Please either set GEMINI_API_KEY in your environment or provide an API key in the form.")

    # Validate key format before using
    if not isinstance(api_key_to_use, str) or len(api_key_to_use) < 32:
        raise ValueError("Invalid API key format")

    try:
        # Configure the Gemini API with the appropriate key
        genai.configure(api_key=api_key_to_use)
        
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
    finally:
        # Clear the API key from memory after use
        api_key_to_use = None
