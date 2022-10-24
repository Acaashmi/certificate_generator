
from turtle import position
from PIL import ImageFont, ImageDraw, Image
import os
def coupons(names: list, certificate: str, font_path1: str,font_path2: str):
   
    for name in names:
          
        # adjust the position according to 
        # your sample
        name_y_position = 720
        team_y_position= 935
        position_y=1026
   
        # opens the image
        img = Image.open(certificate, mode ='r')
          
        # gets the image width
        image_width = img.width
          
        # gets the image height
        image_height = img.height 
   
        # creates a drawing canvas overlay 
        # on top of the image
        draw = ImageDraw.Draw(img)
   
        # gets the font object from the 
        # font file (TTF)
        name_font = ImageFont.truetype(
            font_path1,
            150 # change this according to your needs
        )
        # font file (TTF)
        secondary_font = ImageFont.truetype(
            font_path2,
            35 # change this according to your needs
        )
   
        # fetches the text width for 
        # calculations later on
        name_width, _ = draw.textsize(name[0], font = name_font)
        team_width,_=draw.textsize(name[1],font=secondary_font)
        position_width,_=draw.textsize(name[2],font=secondary_font)
        draw.text(
            (
                # this calculation is done 
                # to centre the image
                (image_width - name_width) / 2,
                name_y_position
            ),
            name[0],
            fill=(0,255,0),
            font = name_font        )
    
        

        draw.text(
            (
                # this calculation is done 
                # to centre the image
                #(image_width - position_width) / 2,
                635,
                team_y_position
            ),
            name[1],
            fill=(0,255,0),
            font = secondary_font        )

        draw.text(
            (
                # this calculation is done 
                # to centre the image
                #(image_width - team_width) / 2,
                1391,
                position_y
            ),
            name[2],
            fill=(0,255,0),
            font = secondary_font        )
   
        # saves the image in png format
        img.save("generated_certificate/{}.png".format(name[0])) 
  
# Driver Code
if __name__ == "__main__":
   
    # some example of names
    NAMES = [["Gayatri Agarwal","NAAM MEIN KYA RAKHA HAI","WINNER"],["Kashish Agarwal","OCTAVIOUS","RUNNERS UP"]]
    
    # path to font
    FONT1 = "fonts\Praise-Regular.ttf"
    FONT2= "fonts\Poppins-Regular.ttf"
      
    # path to sample certificate
    CERTIFICATE = "cert.png"
   
    coupons(NAMES, CERTIFICATE, FONT1, FONT2)

    #font=ImageFont.truetype("Praise-Regular.ttf",72)
    #draw.text((664,854),i.title(),fill=colour,font=font)
    #image.save("generated_certificate/"+i+".png")
    