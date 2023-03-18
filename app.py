import os
import random
from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__, static_folder='')

IMAGE_DIR = None

# Add this new route to your Flask app
@app.route('/next_image')
def next_image():
    global IMAGE_DIR
    images = [f for f in os.listdir(IMAGE_DIR) if os.path.isfile(os.path.join(IMAGE_DIR, f))]
    image = random.choice(images)
    image_url = url_for('static', filename=f'{IMAGE_DIR}/{image}')
    return jsonify({"image_url": image_url})
    
@app.route('/', methods=['GET', 'POST'])
def display_images():
    global IMAGE_DIR
    if request.method == 'POST':
        # Retrieve the value from the form
        image_dir = request.form['image_dir']
        # Set the global variable to the new value
        IMAGE_DIR = image_dir
    
    if IMAGE_DIR:
        # Get a list of all the image files in the folder
        images = [f for f in os.listdir(IMAGE_DIR) if os.path.isfile(os.path.join(IMAGE_DIR, f))]
        # Choose a random image from the list
        image = random.choice(images)
        # Generate a URL for the image
        image_url = url_for('static', filename=f'{IMAGE_DIR}/{image}')
        # Render the template with the image URL
        return render_template('index.html', image_url=image_url)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
