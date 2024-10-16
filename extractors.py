# extractors.py

import pickle
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Global driver variable
driver = None

# Function to Load Session Cookies and Bypass Login
def load_session_cookies(cookie_file, profile_url):
    global driver
    driver.get("https://www.linkedin.com/")
    time.sleep(2)

    # Load cookies from the file and add them to the browser
    cookies = pickle.load(open(cookie_file, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    # Refresh the page to apply cookies and navigate to the profile
    driver.get(profile_url)
    print("Successfully loaded session cookies and accessed profile!")

# Function to Print a Progress Bar
def print_progress_bar(iteration, total, length=50):
    percent = (iteration / total) * 100
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r|{bar}| {percent:.2f}% Complete')
    sys.stdout.flush()  

def remove_repeated_phrases(text):
    # Split the text into lines/phrases and strip whitespace
    phrases = [line.strip() for line in text.splitlines() if line.strip()]
    
    # Use a set to track seen phrases and a list for unique phrases
    seen_phrases = set()
    unique_phrases = []

    for phrase in phrases:
        if phrase not in seen_phrases:
            seen_phrases.add(phrase)
            unique_phrases.append(phrase)

    # Join unique phrases back into a single string with newline characters
    return '\n'.join(unique_phrases)

# Function to Extract Profile Information
def extract_profile_info(driver):
    profile_data = {}

    # Extract profile name 
    try:
        name = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span/a/h1").text
        profile_data["Name"] = name
    except:
        profile_data["Name"] = "N/A"
        print("Failed to extract name")

    # Extract profile headline
    try:
        headline = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[2]").text
        profile_data["Headline"] = headline
    except:
        profile_data["Headline"] = "N/A"
        print("Failed to extract headline")

    # Extract additional info
    try:
        additional_info = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[4]/div[3]/div/div/div/span[1]/text()[2]").text
        profile_data["Additional Info"] = additional_info
    except:
        profile_data["Additional Info"] = "N/A"
        print("Failed to extract additional info")

    # Extract About section
    try:
        about_section = driver.find_element(By.XPATH, "//div[@id='about']/following-sibling::div[2]/div/div/div/span[1]").text
        profile_data["About"] = about_section
    except:
        profile_data["About"] = "N/A"
        print("Failed to extract About section")

    # Extract entire Activity section
    try:
        activity_section = driver.find_element(By.XPATH, "//div[@id='content_collections']/following-sibling::div[3]/div/div/div[1]/ul").text
        profile_data["Activity"] = activity_section
    except:
        profile_data["Activity"] = "N/A"
        print("Failed to extract Activity section")

    # Extract Experience section
    try:
        experience_section = driver.find_element(By.XPATH, "//div[@id='experience']/following-sibling::div[2]/ul").text
        profile_data["Experience"] = remove_repeated_phrases(experience_section) 
    except:
        profile_data["Experience"] = "N/A"
        print("Failed to extract Experience section")

    # Extract Licenses and Certifications section
    try:
        certifications_section = driver.find_element(By.XPATH, "//div[@id='licenses_and_certifications']/following-sibling::div[2]/ul").text
        profile_data["Certifications"] = remove_repeated_phrases(certifications_section) 
    except:
        profile_data["Certifications"] = "N/A"
        print("Failed to extract Certifications section")

    return profile_data

# Function to Extract Contact Info
def extract_contact_info(driver,profile_url):
    contact_info = {}

    # Navigate to the contact info overlay
    driver.get(profile_url + "overlay/contact-info/")
    time.sleep(3)  # Wait for the overlay to load

    try:
        # Find the contact info section
        contact_section = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/section/div")

        # Get all <a> tags in the contact section
        links = contact_section.find_elements(By.TAG_NAME, "a")

        # Extract text from all <a> tags except the last one
        contact_texts = [link.text for link in links[:-1]]  # Exclude the last <a>

        # Join the extracted texts into a single string
        contact_info["Contact Info"] = ", ".join(contact_texts)
    except:
        contact_info["Contact Info"] = "N/A"
        print("Failed to extract Contact Info section")

    return contact_info

# Function to Display Profile Information in JSON Format
def display_profile_info(profile_data):
    json_output = json.dumps(profile_data, indent=4)  # Convert to JSON with indentation
    print(json_output)
    return json_output

# Function to Save Profile Information to a TXT file
def save_profile_info_to_file(profile_data, file_path):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write profile data to the specified file path
    with open(file_path, 'w') as file:
        json_output = json.dumps(profile_data, indent=4)  # Convert to JSON format
        file.write(json_output)
    print(f"Profile information saved to {file_path}")

