import openai
import pyttsx3

# Set up OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Initialize text-to-speech engine
engine = pyttsx3.init()

def get_openai_response(prompt):
    # Call OpenAI's GPT-3 API to generate a response
    response = openai.Completion.create(
        engine="davinci",  # Choose your engine
        prompt=prompt,
        max_tokens=50  # Adjust as needed for response length
    )
    return response.choices[0].text.strip()

def text_to_speech(text):
    # Convert text to speech using pyttsx3
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    # Main loop to interact with the AI
    while True:
        user_input = input("You: ")
        
        # Get AI response
        ai_response = get_openai_response(user_input)
        print("AI:", ai_response)
        
        # Convert AI response to speech
        text_to_speech(ai_response)
