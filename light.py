import pico_4wd as car
import time
import random

sleep_animation = 0.01 #Timings
sleep_police = 0.008 #Timings



def animation():
    for i in range(24):
        car.set_light_color_at(i, [255, 0, 0])
        time.sleep(sleep_animation)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 0])
        time.sleep(sleep_animation)
    for i in range(24):
        car.set_light_color_at(i, [0, 255, 0])
        time.sleep(sleep_animation)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 0])
        time.sleep(sleep_animation)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 255])
        time.sleep(sleep_animation)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 0])
        time.sleep(sleep_animation)
    for i in range(24):
        car.set_light_color_at(i, [255, 255, 255])
        time.sleep(sleep_animation)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 0])
        time.sleep(sleep_animation)
        
def police():
    for i in range(24):
        car.set_light_color_at(i, [255, 0, 0])
        time.sleep(sleep_police)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 255])
        time.sleep(sleep_police)
    for i in range(24):
        car.set_light_color_at(i, [255, 0, 0])
        time.sleep(sleep_police)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 255])
        time.sleep(sleep_police)
    for i in range(24):
        car.set_light_color_at(i, [255, 255, 255])
        time.sleep(0.008)
    

def policeAI(): #Generiert von chat.openai.com (ChatGPT Jan 9 Version)
    for i in range(24):
        car.set_light_color_at(i, [255, 0, 0])
    time.sleep(0.1)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 0])
    time.sleep(0.1)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 255])
    time.sleep(0.1)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 0])
    time.sleep(0.1)
    for i in range(24):
        car.set_light_color_at(i, [255, 0, 0])
    time.sleep(0.1)
    for i in range(24):
        car.set_light_color_at(i, [255, 255, 255])
    time.sleep(0.1)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 0])
    time.sleep(0.1)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 255])
    time.sleep(0.1)
    for i in range(24):
        car.set_light_color_at(i, [255, 0, 0])
    time.sleep(0.1)
    for i in range(24):
        car.set_light_color_at(i, [255, 255, 255])
    time.sleep(0.1)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 0])
    time.sleep(0.1)
    for i in range(24):
        car.set_light_color_at(i, [255, 0, 0])
    time.sleep(0.1)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 255])
    time.sleep(0.1)
    for i in range(24):
        car.set_light_color_at(i, [255, 255, 255])
    time.sleep(0.1)

def policeAI2():
    for i in range(8):
        car.set_light_color_at(i, [255, 0, 0])
    time.sleep(0.1)
    for i in range(8, 16):
        car.set_light_color_at(i, [0, 0, 255])
    time.sleep(0.1)
    for i in range(16, 24):
        car.set_light_color_at(i, [255, 255, 255])
    time.sleep(0.1)
    for i in range(8):
        car.set_light_color_at(i, [0, 0, 0])
    time.sleep(0.1)
    for i in range(8, 16):
        car.set_light_color_at(i, [0, 0, 0])
    time.sleep(0.1)
    for i in range(16, 24):
        car.set_light_color_at(i, [0, 0, 0])
    time.sleep(0.1)


def buntAI():
    # Funktion "buntAI" wurde von ChatGPT erstellt
    for i in range(24):
        car.set_light_color_at(i, [random.randint(0,255),random.randint(0,255),random.randint(0,255)])
    
def ChatGPT_buntAIv1():
    # Funktion "ChatGPT_buntAI" wurde von ChatGPT erstellt
    for i in range(24):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        while (r > 100 and g > 100 and b > 100):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
        car.set_light_color_at(i, [r,g,b])
        time.sleep(0.1)

def ChatGPT_buntAI_v2():
    # Funktion "ChatGPT_buntAI_v2" wurde von ChatGPT erstellt
    last_color = [0, 0, 0]
    for i in range(24):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        while (r > 100 and g > 100 and b > 100) or (abs(last_color[0] - r) + abs(last_color[1] - g) + abs(last_color[2] - b) < 20) :
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
        last_color = [r, g, b]
        car.set_light_color_at(i, [r,g,b])
        time.sleep(0.1)

def ChatGPT_buntAI_v3():
    # Funktion "ChatGPT_buntAI_v3" wurde von ChatGPT erstellt
    for i in range(24):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        while (r > 100 and g > 100 and b > 100) or (r < 50 and g < 50 and b < 50):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
        car.set_light_color_at(i, [r,g,b])
        time.sleep(0.05)

def ChatGPT_buntAI_v4():
    # Funktion "ChatGPT_buntAI_v4" wurde von ChatGPT erstellt
    for i in range(24):
        r = random.randint(0,200)
        g = random.randint(0,200)
        b = random.randint(0,200)
        while (r < 50 or g < 50 or b < 50):
            r = random.randint(0,200)
            g = random.randint(0,200)
            b = random.randint(0,200)
        car.set_light_color_at(i, [r,g,b])
        time.sleep(0.05)
    
def ChatGPT_buntAI_v5():
    # Funktion "ChatGPT_buntAI_v5" wurde von ChatGPT erstellt
    for i in range(24):
        r = random.randint(0,200)
        g = random.randint(0,200)
        b = random.randint(0,200)
        while (r < 50 and g < 50 and b < 50):
            r = random.randint(0,200)
            g = random.randint(0,200)
            b = random.randint(0,200)
        car.set_light_color_at(i, [r,g,b])
        time.sleep(0.05)


