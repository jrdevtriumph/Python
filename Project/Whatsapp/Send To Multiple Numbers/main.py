import pandas as pd
import pywhatkit
import time
import random
import os

# Function to send WhatsApp messages with an optional image
def send_whatsapp_messages_with_image(file_path, image_path):
    try:
        # Check if the image file exists
        if not os.path.exists(image_path):
            print(f"Error: The image file at {image_path} does not exist.")
            return

        # Read the Excel file
        data = pd.read_excel(file_path)

        # Check if the required columns exist
        if 'name' not in data.columns or 'number' not in data.columns:
            print("Error: Excel file must contain 'name' and 'number' columns.")
            return

        # Loop through each row in the Excel file
        for index, row in data.iterrows():
            name = row['name']
            
            number = str(row['number']).strip()  # Ensure the number is a string

            # Ensure the number includes the '+' sign
            if not number.startswith('+'):
                number = '+' + number

            # Prepare the message
            message = f"Hi, {name}\nHave a good day."

            # Send the message with the image
            print(f"Sending message to {name} at {number} with image...")

            # Sending WhatsApp message with image
            pywhatkit.sendwhats_image(
                receiver=number, 
                img_path=image_path, 
                caption=message, 
                wait_time=10,  # Give a bit more time for WhatsApp to load
                tab_close=True
            )

            # Introduce a random delay of 10 to 20 seconds
            delay = random.randint(10, 20)
            print(f"Waiting for {delay} seconds before sending the next message...")
            time.sleep(delay)

        print("All messages sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


# Replace 'your_file_path.xlsx' with the path to your Excel file
file_path = "Contacts.xlsx"
# Replace 'your_image_path.jpg' with the full path to the image you want to send
image_path = "logo.png"  # Full absolute path to the image
send_whatsapp_messages_with_image(file_path, image_path)