function previewImage(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function() {
            const imgElement = document.getElementById('uploaded-image');
            imgElement.src = reader.result;
            imgElement.style.display = 'block';
            imgElement.style.maxHeight = 'none';
            imgElement.style.width = '100%';

            // Hide the upload icon and label
            document.getElementById('upload-icon').style.display = 'none';
            document.getElementById('upload-label').style.display = 'none';

            // Automatically start processing the image
            uploadImage(file);
        }
        reader.readAsDataURL(file);
    }
}

function uploadImage(file) {
    if (!file) {
        alert('Please select an image file.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    const spinner = document.getElementById('spinner');
    spinner.style.display = 'block';
    document.getElementById('result').innerText = '';

    fetch('/predict', { // Replace '/predict' with your actual API endpoint
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(result => {
        spinner.style.display = 'none';
        document.getElementById('result').innerHTML = `<div style="background: transparent; padding: 0px; border-radius: 0px; color: white;"><strong>Label:</strong> ${result.class}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>Confidence:</strong> ${(parseFloat(result.confidence)).toFixed(2)}%</div>`;
        // Show the clear button after the result is shown
        document.getElementById('clear-button').style.display = 'block';
    })
    .catch(error => {
        spinner.style.display = 'none';
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error processing the image.';
        // Show the clear button even if there is an error
        document.getElementById('clear-button').style.display = 'block';
    });
}

function dropHandler(event) {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function() {
            const imgElement = document.getElementById('uploaded-image');
            imgElement.src = reader.result;
            imgElement.style.display = 'block';
            imgElement.style.maxHeight = 'none';
            imgElement.style.width = '100%';

            // Hide the upload icon and label
            document.getElementById('upload-icon').style.display = 'none';
            document.getElementById('upload-label').style.display = 'none';

            // Automatically start processing the image
            uploadImage(file);
        }
        reader.readAsDataURL(file);
    }
}

function dragOverHandler(event) {
    event.preventDefault();
}

function clearImage() {
    const imgElement = document.getElementById('uploaded-image');
    imgElement.src = '#';
    imgElement.style.display = 'none';

    // Show the upload icon and label
    document.getElementById('upload-icon').style.display = 'block';
    document.getElementById('upload-label').style.display = 'block';

    // Clear the result text
    document.getElementById('result').innerText = '';

    // Hide the clear button
    document.getElementById('clear-button').style.display = 'none';

    // Clear the file input
    document.getElementById('file-input').value = '';
}
