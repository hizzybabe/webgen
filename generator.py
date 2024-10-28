import openai

def generate_webpage(framework, page_type, components, js_features):
    # Construct prompt for OpenAI
    prompt = f"""Create a webpage with:
    Framework: {framework}
    Type: {page_type}
    Components: {', '.join(components)}
    JavaScript features: {', '.join(js_features)}
    
    Provide complete HTML, CSS, and JavaScript code.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a web development expert."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content
