document.getElementById('generatorForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Collect form data
    const formData = new FormData(e.target);
    const data = {
        framework: formData.get('framework'),
        type: formData.get('pageType'),
        components: [...formData.getAll('components')],
        jsFeatures: [...formData.getAll('jsFeatures')],
        colorPalette: formData.get('colorPalette')  // Add this line
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
        
        if (result.success) {
            document.getElementById('result').style.display = 'block';
            document.getElementById('generatedCode').textContent = result.code;
        } else {
            alert('Error generating webpage: ' + result.error);
        }
    } catch (error) {
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
