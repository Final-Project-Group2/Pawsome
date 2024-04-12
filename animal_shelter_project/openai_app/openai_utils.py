from openai import OpenAI
import re
import os

def generate_openai_query(form_data):
    query = f"I am looking to adopt a {form_data['pet_type']} with the following preferences:\n\n"
    
    query += f"Pet Type: {form_data['pet_type']}\n"
    query += f"Size: {form_data['size']}\n"
    query += f"Activity Level: {form_data['activity_level']}\n"
    query += f"Temperament: {form_data['temperament']}\n"
    query += f"Compatibility with Other Pets or Children: {form_data['compatibility']}\n"
    query += f"Grooming Needs: {form_data['grooming']}\n"
    query += f"Living Environment: {form_data['living_environment']}\n"
    query += f"Time Commitment: {form_data['time_commitment']}\n\n"

    query += """Based on this information, could you please provide recommendations for breeds of pets for adoption? Please provide recommendations for adoption in the format: 
        'Based of yor preference I'd recomend you next breeds : **Breed Name**: Description'\n\n"""
    return query

def get_openai_response(openai_query):
    client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a pet adoption assistant, thar can recomend the breeds of pets that I can adopt regarding my preference and explain more about this spaces."},
            {"role": "user", "content": openai_query}
        ]
    )

    response_text = completion.choices[0].message.content

    return response_text


#def extract_recommended_breeds(response_text):
    #pattern = r'\*\*(.*?)\*\*'

    #matches = re.findall(pattern, response_text)

    #recommended_breeds = [match.strip() for match in matches if len(match.split()) > 1]

    #return recommended_breeds
