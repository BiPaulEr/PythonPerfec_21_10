from PIL import Image 
import os

def generator_image(directory):
    for image_path in os.listdir(directory):
        if image_path.endswith(".jpg"):
            image_full_path = os.path.join(directory, image_path)
            yield Image.open(image_full_path)


for index, image in enumerate(generator_image("C:/Users/PaulE/Documents/DataSet/AbstractArt")):
    image.save("C:/Users/PaulE/Documents/DataSet/AbstractArt/test/"+ str(index) + ".jpg")