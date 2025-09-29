'''

-THIS FILEHANDLES THE GENERAION OF THE REEL FROM THE UPLOADED FILES
IT ALSO USES TEXT TO CREATE AUDIO
HANDLES  WHAT DIRECTORY HAS BEEN DONE

'''

import os
from text_to_audio import text_to_speech_file
import time


def generate_reel(folder):
    print(f"Generating reel for folder: {folder}")
    

def generate_audio(folder):
    print(f"Generating audio for folder: {folder}")
    with open(f"uploads/{folder}/descr.txt", 'r') as f:
        text = f.read()
    # text_to_speech_file(text, folder)
    


if __name__ == "__main__":
     
     '''
      ~ taking the folder name as input
      ~ checking if the folder exists
      ~ if it exists, check if the reel has already been generated
      ~ if it doesn't exist, create the reel and audio
     
     '''
     while True:
        print("Checking for new folders...")
        with open("done.txt", 'r') as f:
            done_folders = f.readlines()
        
        done_folders= [x.strip() for x in done_folders] # remove newline characters
        folders = os.listdir("uploads/") # get the last folder in the uploads directory
        
        for folder in folders:
            if folder not in done_folders: # check if the folder is already done
                generate_reel(folder)            
                generate_audio(folder)
                with open("done.txt", 'a') as f:
                        f.write(folder+"\n")
        
        time.sleep(5)
                        