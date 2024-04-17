from django.shortcuts import render
from .forms import AdoptionPreferenceForm
from .openai_utils import generate_openai_query, get_openai_response, extract_recommended_breeds
from animal_shelter_app.models import Pet
from django.views.generic import FormView

class AdoptionPreferenceFormView(FormView):
    template_name = 'adoption_preference.html'
    form_class = AdoptionPreferenceForm
    success_url = '/adoption_preference_result/'

    def form_valid(self, form):
        # Get the cleaned form data
        form_data = form.cleaned_data

        # Geerate the OpenAI query based on the form data
        openai_query = generate_openai_query(form_data)
        
        # Interact with the OpenAI API to get recommendations
        openai_response = get_openai_response(openai_query)

        all_pets = Pet.objects.all()
        
        matching_pets = Pet.objects.none()

        for pet in all_pets:
            if pet.breeds.lower() in openai_response.lower():  
                matching_pets |= Pet.objects.filter(pk=pet.pk)
                break 

        print(matching_pets)


        return render(self.request, 'adoption_preference_result.html', {
            'openai_response': openai_response,
            'matching_pets': matching_pets
        })