import os
import random
from argparse import ArgumentParser

class CardGenerator:
    def __init__(self) -> None:
        self.path = os.path.dirname(__file__)
        self.data = {}
        self.main()
    
    def main(self):
        parser = ArgumentParser()
        parser.add_argument(
                "--scatter-images",
                action="store_true",
                default=False,
                help="If True, randomizes image order",
            )
        parser.add_argument(
                "--scatter-message",
                action="store_true",
                default=False,
                help="If True, each line in message.txt appears in random order",
            )
        # Create an array of absolute paths to the images
        # Define image array in self.data
        image_folder = f"{self.path}/images"
        file_names = [f"{image_folder}/{f}" for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
        self.data["images"]=file_names
        
        # Read message.txt and move each line to an array
        # Define message array in self.data
        with open(f"{self.path}/message.txt", 'r') as file:
            lines = [line.strip() for line in file]
            self.data["message"] = lines
        
        # Determine if images or message should appear in random order
        args, _ = parser.parse_known_args()
        if "images" in self.data and args.scatter_images:
            random.shuffle(self.data["images"])
        if "message" in self.data and args.scatter_message:
            random.shuffle(self.data["message"])
        
        for val in self.data.values():
            val.reverse()
        # Generate data.json
        with open("data.js", "w") as json_file:
            json_file.write("function get_images(){\n    return %s;\n}\nfunction get_message(){\n    return %s;\n}\n" % (self.data["images"], self.data["message"]))
        

CardGenerator()
    

