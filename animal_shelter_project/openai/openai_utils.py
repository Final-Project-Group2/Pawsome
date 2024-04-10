import requests

def generate_openai_query(form_data):
    query = f"I am looking to adopt a {form_data['pet_type']} with the following preferences:\n\n"
    
    query += f"Pet Type: {form_data['pet_type']}\n"
    query += f"Breed Preference: {form_data['breed_preference']}\n"
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

def get_openai_response(query):
    # Define the endpoint URL
    endpoint = "https://api.openai.com/v1/completions"

    # Set up the request headers with your API key
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }

    # Define the request body
    data = {
        "model": "text-davinci-002",  # Choose the appropriate model
        "prompt": query,
        "temperature": 0.7,  # Adjust the temperature parameter if needed
        "max_tokens": 150  # Adjust the max_tokens parameter if needed
    }

    # Send the POST request to the OpenAI API
    response = requests.post(endpoint, json=data, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract and return the response data
        return response.json()
    else:
        # Print an error message if the request fails
        print("Error:", response.status_code)
        return None