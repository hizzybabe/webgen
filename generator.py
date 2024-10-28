import google.generativeai as genai
import os

def generate_webpage(framework, page_type, components, js_features):
    # Configure the Gemini API
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    
    # Construct prompt for Gemini
    prompt = f"""Create a webpage with:
    Framework: {framework}
    Type: {page_type}
    Components: {', '.join(components)}
    JavaScript features: {', '.join(js_features)}
    
    Provide complete HTML, CSS, and JavaScript code.
    """
    
    # Initialize Gemini model
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Generate response
    response = model.generate_content(prompt)
    
    return response.text
