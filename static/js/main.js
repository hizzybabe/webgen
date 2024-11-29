document.getElementById('generatorForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Show loading indicator, hide result
    document.getElementById('loadingIndicator').style.display = 'block';
    document.getElementById('result').style.display = 'none';
    document.getElementById('generatorForm').querySelector('button[type="submit"]').disabled = true;
    
    // Collect form data
    const formData = new FormData(e.target);
    const data = {
        framework: formData.get('framework'),
        type: formData.get('pageType'),
        components: [...formData.getAll('components')],
        jsFeatures: [...formData.getAll('jsFeatures')],
        colorPalette: formData.get('colorPalette'),
        language: formData.get('language')
    };

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        
        // Hide loading indicator
        document.getElementById('loadingIndicator').style.display = 'none';
        document.getElementById('generatorForm').querySelector('button[type="submit"]').disabled = false;
        
        if (result.success) {
            document.getElementById('result').style.display = 'block';
            document.getElementById('generatedCode').textContent = result.code;
            document.getElementById('generatedComments').style.display = 'none';
            
            // Add preview button click handler
            document.getElementById('previewBtn').onclick = () => {
                const code = result.code;
                const previewWindow = window.open('');
                if (previewWindow) {
                    previewWindow.document.write(code);
                    previewWindow.document.close();
                } else {
                    alert('Pop-up blocked! Please allow pop-ups for this site to use the preview feature.');
                }
            };
        } else {
            alert('Error generating webpage: ' + result.error);
        }
    } catch (error) {
        // Hide loading indicator and show error
        document.getElementById('loadingIndicator').style.display = 'none';
        document.getElementById('generatorForm').querySelector('button[type="submit"]').disabled = false;
        alert('Error: ' + error.message);
    }
});

// Download functionality
document.getElementById('downloadBtn').addEventListener('click', () => {
    const code = document.getElementById('generatedCode').textContent;
    const blob = new Blob([code], { type: 'text/html' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'generated-webpage.html';
    a.click();
    window.URL.revokeObjectURL(url);
});

// Dark mode functionality
function initDarkMode() {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
    
    // Check for saved user preference, if any, on load of the website
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
    }
    
    // Listen for toggle button click
    darkModeToggle.addEventListener('click', () => {
        let theme = document.documentElement.getAttribute('data-theme');
        
        if (theme === 'dark') {
            document.documentElement.removeAttribute('data-theme');
            localStorage.setItem('theme', 'light');
        } else {
            document.documentElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
        }
    });
    
    // Listen for system theme changes
    prefersDarkScheme.addListener((e) => {
        const theme = localStorage.getItem('theme');
        if (!theme) {
            if (e.matches) {
                document.documentElement.setAttribute('data-theme', 'dark');
            } else {
                document.documentElement.removeAttribute('data-theme');
            }
        }
    });
}

// Initialize dark mode when DOM is loaded
document.addEventListener('DOMContentLoaded', initDarkMode);
