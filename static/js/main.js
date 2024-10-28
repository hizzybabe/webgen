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
        colorPalette: formData.get('colorPalette')
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
            
            // Update the preview with sandbox attribute and try-catch
            const previewFrame = document.getElementById('previewFrame');
            try {
                previewFrame.setAttribute('sandbox', 'allow-same-origin allow-scripts');
                const frameDoc = previewFrame.contentDocument || previewFrame.contentWindow.document;
                frameDoc.open();
                frameDoc.write(result.code);
                frameDoc.close();
            } catch (frameError) {
                console.error('Preview frame error:', frameError);
                // Fallback - display a message that preview is unavailable
                previewFrame.srcdoc = '<p>Preview unavailable due to security restrictions. Please use the download button to view the generated code.</p>';
            }
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
