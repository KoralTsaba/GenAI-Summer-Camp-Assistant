from summerCampDetails import genai_summer_camp_details

INIT_PROMPT = 0
ROUTER_PROMPT = 1
QUESTION_PROMPT = 2
APPLICATION_PROMPT = 3

prompts = dict()
prompts[INIT_PROMPT] = {'begin':'Hello now you are a chatbot which represents our GenAI camp. here is some details about our camp that you need to know :','end':'Supply your next answers based on this details'}
prompts[ROUTER_PROMPT] = {'begin':'Hey, can you please help me to know if this sentece is a question or a application/contact information add your answer in the term[2 or 3] 2 for question, 3 for application or contact information', 'end':'answer:'}
prompts[QUESTION_PROMPT] = {'begin':f'Here some summary about my genai camp:\n{genai_summer_camp_details}\n following this summary please answer the following question:','end':'Answer:'}
prompts[APPLICATION_PROMPT] = {'begin':"""
Your a chat that should help me to get a messages from a parants who want to sign up their kids to my camp. and your purpose it to extract me the details and make my job easier.
for registration i need the name, and kid's age, the phone number and email.
the parent message is :\n""", 'end':"""please answer me in the following template(supply only the given details) without any additional text:
name:
age:
number:
email:
"""}

welcome_msg = "WELCOME to the GenAI Summer Camp.\nMy name is Koral, the virtual assistant.\nI'm here to help you with sign up your kids or to answer any questions you may have about our camp.\nHow can I assist you today?\n"