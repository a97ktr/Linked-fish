# Linked Fish: Exploring Automated Phishing through AI-powered Social Engineering Tools

## 📄 Overview:

Linked Fish is a social engineering tool designed for ethical hacking purposes to simulate phishing attacks and spread awareness of cyber threats. By leveraging LinkedIn’s professional network and automated AI tools, the project demonstrates the risks posed by modern phishing and social engineering, especially with the emergence of AI and Large Language Models (LLMs).

## 🚀 Features:

LinkedIn Profile Scraping: Extracts relevant data from target profiles.
Automated Message Generation: Utilizes AI-based tools to create convincing phishing messages.
User Choice Workflow: Option to use an existing cookie or log in to create a new session.
Text-to-Speech Conversion: Uses ElevenLabs API to convert phishing messages into audio.
Awareness & Testing: Aims to spread awareness or test the security readiness of users and employees.

## 🛑 Disclaimer:

This tool is developed strictly for educational purposes and to spread awareness about the dangers of phishing and automated social engineering attacks. Misuse of this tool is illegal and against the principles of ethical hacking. Use responsibly!

## ⚖️ LinkedIn’s Policy on Scraping:

LinkedIn strictly prohibits unauthorized data scraping or automated extraction of data from its platform. According to LinkedIn’s Terms of Service, any activity involving scraping, data harvesting, or unauthorized access to user information is against their policy. Violating these terms may result in legal action or account suspension.

Linked Fish is intended only for academic and ethical purposes, and any use of the tool must comply with LinkedIn’s policies and legal frameworks. It is important to secure appropriate permissions if the tool is to be applied in real-world scenarios.

## 🛠 Technologies Used

Python for automation and backend logic.
Selenium for target profile extraction.
Groq API for scraping tools.
ElevenLabs API for voice synthesis.
Rich & Pyfiglet for UI enhancements.

📋 Installation & Setup
### Step 1: Clone the Repository
```
git clone https://github.com/a97ktr/Linked-fish.git
cd Linked-fish
```
### Step 2: Create and Activate a Virtual Environment
```
python -m venv env  
source env/bin/activate  # On Mac/Linux
env\Scripts\activate  # On Windows
```
### Step 3: Install Required Libraries
```
pip install -r requirements.txt
```
#### Step 4: Set Up APIs
- Groq API: Sign up and get your API key.
- ElevenLabs API: Sign up and generate your API key.
- LinkedIn: Create a LinkedIn account if you don't already have one.
## ⚙️ Usage Workflow
#### Run the Tool:
```
python main.py
```

Choose Workflow:
New Login: Log in to generate a fresh cookie OR
Existing Cookie: Use an existing session file.
Data Storage:  data is saved in  ./{profile_id}/ for future reference.

Awareness Testing: Run phishing simulations using generated content.

## Project Structure

Linked-Fish/

├── main.py       # Main script  
├── banner.py            # Banner & UI elements  
├── generators.py        # generate phishing messages
├── extractors.py        # Extract target's data
├── selenium_utils.py    # Extraction functions  
├── helper.py            # Utility functions  
├── voice.py             # Text-to-speech logic  
├── requirements.txt     # Python dependencies  
└── README.md            # Project documentation  

## 🛠 Future Perspectives
### Scalability: 
Linked Fish can be extended with advanced data-stealing mechanisms.
### Enterprise Use:
Adaptable for large-scale phishing simulations and employee security training.
### AI Integration:
Enhanced with more sophisticated LLMs for targeted campaigns.

##  Conclusion
Linked Fish highlights the emerging threats of automated social engineering and the importance of security awareness. Use this tool responsibly to educate and test users, ensuring proactive defense against phishing attacks.

