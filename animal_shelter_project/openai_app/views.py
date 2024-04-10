from django.shortcuts import render
from .forms import AdoptionPreferenceForm
from .openai_utils import generate_openai_query, get_openai_response

def adoption_preference_form_view(request):
    if request.method == 'POST':
        form = AdoptionPreferenceForm(request.POST)
        if form.is_valid():
            # Get the cleaned form data
            form_data = form.cleaned_data

            # Generate the OpenAI query based on the form data
            openai_query = generate_openai_query(form_data)
            
            # Interact with the OpenAI API to get recommendations
            openai_response = get_openai_response(openai_query)

            # Render the response in the template
            return render(request, 'adoption_preference_result.html', {'openai_response': openai_response})
    else:
        form = AdoptionPreferenceForm()

    return render(request, 'adoption_preference.html', {'form': form})