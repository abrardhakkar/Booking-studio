from PIL import Image, ImageDraw, ImageFont

# Opret en ny hvid billedfil med de ønskede dimensioner (f.eks. 200x200 pixels).
width, height = 200, 200
background_color = (255, 255, 255)
image = Image.new('RGB', (width, height), background_color)

# Hent en tegnefunktion til at tilføje mikrofon-ikonet.
draw = ImageDraw.Draw(image)

# Definér farver og koordinater for mikrofonikonet (dette er et simpelt eksempel).
microphone_color = (0, 0, 0)
microphone_coordinates = [(100, 75), (100, 150), (125, 175), (75, 175), (100, 150)]
draw.polygon(microphone_coordinates, fill=microphone_color)

# Gem billedet som en fil.
image.save('microphone_logo.png')
