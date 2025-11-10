intent_responses = {
    "greeting":["Hello!How can I help you today?","Hi,there what can i do for you?"],
    "goodbye":["Goodbye!Have a nice day.","See you later"],
    "hours":["Our working hours are 9 AM to 6 PM,Monday to Friday","We are open from 9AM TO 6PM on weekdays."],
    "services":["We offer AI&DS course , chatbot development, and data analytics training."],
    "thanks":["You're welcome!","Happy to help!"]
}
keywords = {
    "greeting":["hi","hello","hey"],
    "goodbye":["bye","exit","quit","see you"],
    "hours":["hours","time","working hours","open"],
    "services":["service","courses","training","offer"],
    "thanks":["thanks","thank you","thx"],
}
def identify_intent(user_input):
    user_input = user_input.lower()
    for intent , keys in keywords.items():
        for key in keys:
            if key in user_input:
                return intent
    return "unknown"
import random
def generate_response(intent):
    if intent in intent_responses:
        return random.choice(intent_responses[intent])
    else:
        return "Sorry,I didn't understand that . Can you rephrase it ?"
def chatbot():
    print("Chatbot:Hello ! I am your assistant.Type 'bye' to exit.")
    while True:
        user_input = input("You : ")
        if user_input.lower() in ["bye","exit","quit"]:
            print("Chatbot:Goodbye!Have a nice day.")
            break
        intent=identify_intent(user_input)
        response=generate_response(intent)
        print("Chatbot: ",response)
chatbot()