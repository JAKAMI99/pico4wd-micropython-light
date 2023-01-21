import light
import random
###Settings###########################################
modes = ['police', 'animation', 'policeAI', 'buntAI', 'ChatGPT_buntAI_v1', 'ChatGPT_buntAI_v2', 'ChatGPT_buntAI_v3', 'ChatGPT_buntAI_v4', 'ChatGPT_buntAI_v5']
count = 10
mode = random.choice(modes)
# police, animation, policeAI, buntAI, ChatGPT_buntAI[v1,v2,v3,v4,v5]
######################################################
counter = count
progress = 1 
while True:  # added infinite loop
    error_occurred = False
    print("mode is now " + mode)
    while counter > 0:
        if hasattr(light, mode):
            print("Durchlauf " + str(progress) + " von " + str(count))
            light_cmd = getattr(light, mode)
            light_cmd()
            counter -= 1
            progress += 1

            
        else:
            if not error_occurred:
                print(f"{mode} is not a valid mode")
                error_occurred = True
                break # hinzugefügt
    counter = count  # added resetting counter to count
    progress = 1
    mode = random.choice(modes)  # added selecting new mode
    print("Choosing new random mode now")