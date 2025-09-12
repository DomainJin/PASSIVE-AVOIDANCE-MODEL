from PIL import Image
import os
import webbrowser

def resize_images(input_folder, output_folder, size=(600, 400)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Check if the input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: The input folder '{input_folder}' does not exist.")
        return

    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            img_path = os.path.join(input_folder, filename)
            with Image.open(img_path) as img:
                img = img.resize(size, Image.ANTIALIAS)
                img.save(os.path.join(output_folder, filename))
                # Open the resized image in the user's browser
                webbrowser.open(os.path.join(output_folder, filename))

# Example usage
resize_images('input_images', 'output_images')
