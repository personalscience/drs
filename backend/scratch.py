# a simple app useful for testing the healthr module
import json

from healthr.bloodtest import find_biomarkers
from healthr.siphox_calls import get_customer_report
from healthr.recommendations import generate_health_recommendation, create_prompt


from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()

# Get the API key from the environment variable

SIPHOX_API_TOKEN = os.getenv("SIPHOX_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Read the prompt string from the text file
with open('./assets/promptstring.txt', 'r') as file:
    prompt_string = file.read()

# Set the environment variable
os.environ['PROMPT_STRING'] = prompt_string

# user_inp = {'exerciseData': 'runs 5 miles daily', 'familyHistoryData': 'nothing serious', 'bloodData': 'N/A', 'weight': 75, 'height': 180, 'sex': 'male', 'age': 40}

# prompt = create_prompt(user_inp)

# answer = generate_health_recommendation(user_inp, OPENAI_API_KEY)

# print(answer)

data = get_customer_report("646b934fae46dcbd6be92385", "SPOTR09QQH")

biomarkers = find_biomarkers(data)

print(biomarkers)
