import json
from groq import Groq

def extract_profile_id(profile_url):
    """Extracts the LinkedIn profile ID from the profile URL."""
    return profile_url.split("/in/")[1].strip("/")

def generate_messages(api_key, profile_info):
    """Generates personalized messages based on the profile data."""
    client = Groq(api_key=api_key)

    # Prepare the message for the model
    message_content = f"""
    Create three distinct and highly persuasive messages based on the provided target details:

    The first should be an email.
    The second should be a voice message text.
    The third should be an SMS message.
    Each message should:

    Grab the target’s attention and encourage them to take immediate action.
    Leverage their experience, activities, and recent interests to craft a personalized narrative.
    Use:

    Professional, credible language.
    References to exclusive opportunities, high-value offers, or urgent notifications to make the content enticing.
    Salary figures, benefits, or time-sensitive links where suitable to increase engagement.
    Each message should create a strong sense of urgency and be designed to:

    Prompt the recipient to click a link (for the email and SMS).
    Guide the target to check their email inbox or SMS message for more details (for the voice message).
    Ensure that the messages:

    Are highly customized to the target’s profile.
    Seem unique and directly relevant to them.
    Try to use real names for companies or people that are relevant to the target or to their professional experience or posting activity 
    Output Format: is gonna be a list like in python [[X],[Y],[Z]], X is the email,Y is the sms, Z is the voicetext message,dont add any indication like 'email:' or 'sms:' etc
    

  
    Guidelines:

    Do not include any introductory or concluding remarks.
    Output only the formatted messages.
    Avoid using labels, explanations, or extraneous information.
    3 Messages should be coherent.
    All names should be filled. even if you created them but names should cohere with the context
    For the voice text message, try to avoid numbers; if needed, numbers are written in letters and symbols like $ is written in letter (e.g., dollar).
    Generate a concise and engaging text for a voice message, formatted to be clear and natural when read by an AI voice. The message should use simple language, avoid overly complex sentences, and include natural pauses for a smooth and conversational tone. Ensure the message length is suitable for a twelve-second delivery. Include slight variations in sentence structure to keep it engaging, and use language that sounds friendly and approachable.
    
    Target Details:

    Name: {profile_info['Name']}
    Headline: {profile_info['Headline']}
    About: {profile_info['About']}
    Activity: {profile_info['Activity']}
    Experience: {profile_info['Experience']}
    Contact Info: {profile_info['Contact Info']}
    Certifications and Licenses: {profile_info['Certifications']}
    """

    try:
        # Make a request to the LLM model to generate messages
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": message_content
                }
            ],
            model="llama-3.2-90b-text-preview",  # Specify the model you want to use
        )

        # Retrieve the generated messages
        output_messages = chat_completion.choices[0].message.content.strip()
        return output_messages

    except Exception as e:
        print("An error occurred:", e)
        return None
