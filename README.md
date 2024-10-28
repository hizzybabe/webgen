![Webgen banner](webgengithub.jpg)

# AI Webpage Generator

A web-based tool that generates custom webpage code using Google's Gemini AI. Users can specify their preferred CSS framework, page type, components, JavaScript features, and color palette to generate tailored webpage code.

## Features

- Support for multiple CSS frameworks (Bootstrap, Tailwind CSS, or custom CSS)
- Various page type templates (Landing Page, Portfolio, Business Site)
- Customizable components (Header, Footer)
- JavaScript feature integration (Responsive Navigation, Dark Mode)
- Pre-defined color palettes
- Real-time code generation
- Code preview and download functionality

## Prerequisites

- Python 3.9.18
- Flask
- Google Generative AI API key

## Installation

1. Clone the repository:
2. Create and activate a virtual environment
3. Install dependencies
4. Create a `.env` file in the root directory and add your Gemini API key

## Usage

1. Start the Flask development server

2. Open your browser and navigate to `http://localhost:5000`

3. Fill out the form with your desired webpage specifications:
   - Select a CSS framework
   - Choose a page type
   - Select desired components
   - Enable JavaScript features
   - Pick a color palette

4. Click "Generate Webpage" to create your custom webpage code

5. Use the "Download Files" button to save the generated code

## Deployment

The application is configured for deployment on platforms like Heroku using Gunicorn. The necessary configuration files (`Procfile` and `runtime.txt`) are included.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## API Key Configuration

There are two ways to use this application with your OpenRouter API key:

1. **Environment Variable (Recommended for Development)**
   - Create a `.env` file in the root directory
   - Add your API key: `GEMINI_API_KEY=your_api_key_here`

2. **Web Interface**
   - Input your API key directly in the web form
   - This method is temporary and the key will only be used for the current session
   - The key is never stored and must be re-entered if the page is refreshed

⚠️ **Security Note**: Never commit your API key to version control. If using the environment variable method, ensure `.env` is listed in your `.gitignore` file.
