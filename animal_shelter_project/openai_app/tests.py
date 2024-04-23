from django.test import TestCase, RequestFactory
from .views import AdoptionPreferenceFormView
from .forms import AdoptionPreferenceForm
from .openai_utils import generate_openai_query, get_openai_response, extract_recommended_breeds
from animal_shelter_app.models import Pet

class OpenaiAppTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_adoption_preference_form_view(self):
        request = self.factory.get('/adoption_preference/')
        response = AdoptionPreferenceFormView.as_view()(request)

        self.assertEqual(response.status_code, 200)

    def test_generate_openai_query(self):
        form_data = {
            'pet_type': 'dog',
            'size': 'small',
            'activity_level': 'high',
            'temperament': 'playful',
            'compatibility': 'good',
            'grooming': 'low',
            'living_environment': 'apartment',
            'time_commitment': '1'
        }
        
        query = generate_openai_query(form_data)

        self.assertIn("Pet Type: dog", query)
        self.assertIn("Size: small", query)
        self.assertIn("Activity Level: high", query)
        self.assertIn("Temperament: playful", query)

    def test_get_openai_response(self):
        query = "Sample query"
        response = get_openai_response(query)

        self.assertIsNotNone(response)

    def test_extract_recommended_breeds(self):
        response_text = "Based on your preference I'd recommend you the following breeds: **Breed 1**: Description, **Breed 2**: Description"

        recommended_breeds = extract_recommended_breeds(response_text)

        self.assertEqual(len(recommended_breeds), 2)
        self.assertIn("Breed 1", recommended_breeds)
        self.assertIn("Breed 2", recommended_breeds)

    def test_matching_pets(self):
        pet1 = Pet.objects.create(breeds="breed1")
        pet2 = Pet.objects.create(breeds="breed2")
        pet3 = Pet.objects.create(breeds="breed3")

        openai_response = "breed1"

        matching_pets = AdoptionPreferenceFormView().filter_matching_pets(openai_response)
        self.assertEqual(matching_pets.count(), 1)
        self.assertEqual(matching_pets.first(), pet1)