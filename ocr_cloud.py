import requests
import os

# Replace YOUR_API_KEY with the key you got from OCR.space
API_KEY = "K88147149888957"

# Folder containing images
folder_path = r"C:\Users\Sindhu\Documents\OCRProject"

# Loop through all images in folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'rb') as f:
            payload = {'isOverlayRequired': False, 'apikey': API_KEY, 'language': 'eng'}
            response = requests.post('https://api.ocr.space/parse/image',
                                     files={filename: f},
                                     data=payload)
            result = response.json()
            parsed_text = result['ParsedResults'][0]['ParsedText']
            print(f"--- Text in {filename} ---")
            print(parsed_text)
            print("-------------------------\n")

