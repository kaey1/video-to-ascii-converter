from PIL import Image
import cv2
import os
from collections import defaultdict
import time
import shutil
nameofvid=input("give name:\n")
timeofvid=219
# Read the video from specified path
brightness_levelspygame=[
(0,0,0),
(24,24,24),
(48,48,48),
(72,72,72),
(96,96,96),
(120,120,120),
(144,144,144),
(168,168,168),
(192,192,192),
(216,216,216),
(240,240,240),
(255,255,255)]
brightness_levelasci="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1}{[]?-_+~<>i!lI;:,^`'.]"
diff=255//len(brightness_levelasci)

cam = cv2.VideoCapture("D:\\efe\\code2.0\\trynamakebadapple\\"+nameofvid+".mp4")
if not os.path.isdir(nameofvid):
    os.makedirs(nameofvid)
    currentframe = 0

    while(True):
        ret,frame = cam.read()

        if ret:
                name = './'+nameofvid+'/frame' + str(currentframe) + '.jpg'
                print ('Creating...' + name)

                # writing the extracted images
                cv2.imwrite(name, frame)
                # increasing counter so that it will
                # show how many frames are created
                currentframe += 1
        else:
            break
    cam.release()
    cv2.destroyAllWindows()
else:
    currentframe=timeofvid*15

os.chdir(nameofvid)
everysinglefuckingframe=[]
def asciprint(imgframe):
    asciphoto=""
    for row in imgframe:
        ascirow=""
        for rgbvalue in row:
            brightnessasci=(0.2126*rgbvalue[0] + 0.7152*rgbvalue[1] + 0.0722*rgbvalue[2])
            ascirow=ascirow+brightness_levelasci[int(brightnessasci//diff)]
        asciphoto=ascirow+"\n"    
    print(asciphoto)
im = Image.open('frame' + str(0) + '.jpg') 
width, height = im.size
skip="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
if input("asci?")=="y":
    if input("ratio?")=="y":
        ratio=width/height
        height=100
        width=round(height*ratio)
    cmd = (
        f'powershell -command "$Host.UI.RawUI.WindowSize = '
        f'New-Object Management.Automation.Host.Size({width},{height})"'
    )
    os.system(cmd)
    
    os.system("color 0F")
    time.sleep(2)
    for i in range(currentframe):
        im = Image.open('frame' + str(i) + '.jpg') 
        im=im.resize((width, height))
        picture = im.load()
        picrow=""
        for y in range(height):
            for x in range(width):
                r, g, b = picture[x, y]
                    
                brightnessasci=(0.2126*r + 0.7152*g + 0.0722*b)
                picrow=picrow+brightness_levelasci[int(brightnessasci//21)]
            picrow=picrow+"\n"
        
        print(picrow)
else:
    import pygame
    background_colour = (255,255,255)
    scale=min(1920//width,1080//height)
    screen = pygame.display.set_mode((width*scale,height*scale))
    pixel_size=scale
    pygame.display.set_caption('badapple')
    screen.fill(background_colour)
    import numpy as np
    brightness_levelspygame = np.array(brightness_levelspygame, dtype=np.uint8)
    for i in range(currentframe):
        im = Image.open(f'frame{i}.jpg').convert("RGB")
        arr = np.asarray(im, dtype=np.uint8)   

        brightness = (
            0.2126 * arr[:, :, 0] +
            0.7152 * arr[:, :, 1] +
            0.0722 * arr[:, :, 2]
        ).astype(np.uint8)

        color_frame = brightness_levelspygame[brightness // 24]

        surface = pygame.surfarray.make_surface(color_frame.swapaxes(0, 1))

        surface = pygame.transform.scale(
            surface,
            (width * pixel_size, height * pixel_size)
        )

        screen.blit(surface, (0, 0))
        pygame.display.flip()
        print(i)
