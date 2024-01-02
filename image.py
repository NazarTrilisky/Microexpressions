
import os
import shutil

from PIL import Image, ImageDraw, ImageFont


def label_image(file_path, emotion_list):
    folder_path = os.path.dirname(os.path.abspath(file_path))
    output_path = os.path.join(folder_path, 'output.png')
    
    main_image = Image.open(file_path)
    edit_image = ImageDraw.Draw(main_image)
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", 20)

    for emtn in emotion_list:
        emotion_str = emtn['dominant_emotion']
        loc = emtn['region']
        coord = (loc['x'], loc['y'], loc['x']+loc['w'], loc['y']+loc['h'])

        edit_image.rectangle(coord, outline='red', fill=None, width=10)
        edit_image.text((coord[0], coord[1]), emotion_str, font=font, fill="#FF0000")

    print("Saving output to: {}".format(output_path))
    main_image.save(output_path)


