# main.py
import os
import json
from selenium_utils import setup_driver, load_session_cookies
from extractors import extract_profile_info, extract_contact_info
from helpers import print_progress_bar
from generator import extract_profile_id, generate_messages
from banner import startup_screen
from login import linkedin_login  # Importing the login function
from voice import extract_and_clean_inner_lists,text_to_speech
import getpass
import time
# Function to prompt user for cookie option
def choose_cookie_option():
    print("\n[1] Use existing cookie file")
    print("[2] Generate new cookies")
    choice = input("Please choose an option (1 or 2): ")
    return choice.strip()

def save_profile_info(profile_data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        json.dump(profile_data, file, indent=4)
    print(f"Data saved to {file_path}")

if __name__ == "__main__":
    startup_screen("Linked  FISH")
    profile_url = input("Enter target's profile link : \t ")

    # Ask user for cookie option
    cookie_option = choose_cookie_option()

    driver = setup_driver()

    if cookie_option == "1":
        # Load existing cookies
        load_session_cookies(driver, "linkedin_cookies.pkl", profile_url)
        time.sleep(5)
    elif cookie_option == "2":
        # Generate new cookies
        username=input('Enter Email or Username: \n')
        password= getpass.getpass("Enter your password: \n")
        linkedin_login(driver, username, password)
    else:
        print("Invalid option selected. Exiting...")
        driver.quit()
        exit()

    profile_id = extract_profile_id(profile_url)

    profile_info = extract_profile_info(driver)
    contact_info = extract_contact_info(driver, profile_url)

    profile_info.update(contact_info)
    save_profile_info(profile_info, f"./{profile_id}/{profile_id}.txt")

    print_progress_bar(7, 7)
    GroqAPIKEY=input('\n Enter your Groq API KEY: \n')
    messages = generate_messages(GroqAPIKEY, profile_info)
    if messages:
        save_profile_info(messages, f"./{profile_id}/{profile_id}_messages.txt")
    driver.quit()
    

    raw_data = messages.strip()
"""
# Extract, clean, and append all content to a single list
final_list = extract_and_clean_inner_lists(raw_data)

# Print the final list
print("Vocal Text", final_list[2])
Eleven_lab_APIKEY=input('Enter Your Elevenlab APIKEY:\n')
text_to_speech(Eleven_lab_APIKEY,final_list[2],"./"+profile_id+"/"+profile_id+".mp3")
""" 