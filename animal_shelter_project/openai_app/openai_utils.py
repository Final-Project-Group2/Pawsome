from openai import OpenAI

def generate_openai_query(form_data):
    query = f"I am looking to adopt a {form_data['pet_type']} with the following preferences:\n\n"
    
    query += f"Pet Type: {form_data['pet_type']}\n"
    query += f"Size: {form_data['size']}\n"
    query += f"Age: {form_data['age']}\n"
    query += f"Activity Level: {form_data['activity_level']}\n"
    query += f"Temperament: {form_data['temperament']}\n"
    query += f"Compatibility with Other Pets or Children: {form_data['compatibility']}\n"
    query += f"Grooming Needs: {form_data['grooming']}\n"
    query += f"Living Environment: {form_data['living_environment']}\n"
    query += f"Time Commitment: {form_data['time_commitment']}\n\n"

    query += "Based on this information, could you please provide recommendations for pets available for adoption?\n\n"

    return query

def get_openai_response(openai_query):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a pet adoption assistant."},
            {"role": "user", "content": openai_query}
        ]
    )

    return completion.choices[0].message