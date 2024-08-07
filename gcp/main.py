from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np

model = None

class_names = ["Early Blight", "Late Blight", "Healthy"]

BUCKET_NAME = "potato-tf-model-cnn"

# Function to Downloads File from Google Cloud Storage:
def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client() #Initializes a client client object for interacting with Google Cloud Storage. 
    bucket = storage_client.get_bucket(bucket_name) # specified bucket.
    blob = bucket.blob(source_blob_name) # Accessing that specific file(blob) within the bucket.

    blob.download_to_filename(destination_file_name) #Download the file to the local file system.

    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")

# Cloud Functions
def predict(request):
    global model
    if model is None:
        download_blob(
            BUCKET_NAME,
            "models/potatoes.h5",
            "/tmp/potatoes.h5",  # The local path where the model file will be saved after download.
        )
        model = tf.keras.models.load_model("/tmp/potatoes.h5")

    image = request.files["file"] #Uploaded the image through HTTP request.

    image = np.array(
        Image.open(image).convert("RGB").resize((256, 256)) # Image resizing and convert into 3d array.
    )

    image = image/255 # normalize the image in 0 to 1 range

    img_array = tf.expand_dims(image, 0) # TensorFlow models expect the input shape to include the batch size.The added dimension represents the batch size.
    
    predictions = model.predict(img_array) # Return 2D array, 2nd dimentions shows the probabilities for each class. 
    print("Predictions:",predictions)

    predicted_class = class_names[np.argmax(predictions[0])] # Show the index of the highest prob.
    confidence = round(100 * (np.max(predictions[0])), 2) # Converts this probability into a percentage upto 2 decimal point.

    return {"class": predicted_class, "confidence": confidence}

