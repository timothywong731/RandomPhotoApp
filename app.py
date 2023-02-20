import os
import random
from flask import Flask, render_template, url_for, request

app = Flask(__name__, static_folder='/')

# Define a route to display a form for user input
@app.route('/set_image_dir', methods=['GET', 'POST'])
def set_image_dir():
    if request.method == 'POST':
        # Retrieve the value from the form
        image_dir = request.form['image_dir']
        # Set the global variable to the new value
        global IMAGE_DIR
        IMAGE_DIR = image_dir
        return "Image directory set to: " + IMAGE_DIR
    else:
        return render_template('set_image_dir.html')

# Define a route to display the images
@app.route('/')
def display_images():
    global IMAGE_DIR
    # Get a list of all the image files in the folder
    images = [f for f in os.listdir(IMAGE_DIR) if os.path.isfile(os.path.join(IMAGE_DIR, f))]
    # Choose a random image from the list
    image = random.choice(images)
    # Generate a URL for the image
    image_url = url_for('static', filename=f'{IMAGE_DIR}/{image}')
    # Render the template with the image URL
    return render_template('index.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)