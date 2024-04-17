from django import forms

class AdoptionPreferenceForm(forms.Form):
    PET_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
    ]

    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    ACTIVITY_CHOICES = [
        ('high', 'High-energy'),
        ('medium', 'Medium-energy'),
        ('low', 'Low-energy'),
    ]

    TEMPERAMENT_CHOICES = [
        ('playful', 'Playful'),
        ('affectionate', 'Affectionate'),
        ('independent', 'Independent'),
    ]

    GROOMING_CHOICES = [
        ('high', 'High maintenance'),
        ('low', 'Low maintenance'),
    ]

    ENVIRONMENT_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House with a yard'),
    ]

    TIME_CHOICES = [
        ('1', '1 hour or less'),
        ('2', '1-2 hours'),
        ('3', '2-3 hours'),
        ('4', '3+ hours'),
    ]

    pet_type = forms.ChoiceField(label='Do you want a dog or cat? Please choose the pet type:', choices=PET_CHOICES)
    size = forms.ChoiceField(label='Now consider size: How big will the pet be when fully grown?', choices=SIZE_CHOICES)
    activity_level = forms.ChoiceField(label='How active will the pet be? Please choose the activity level:', choices=ACTIVITY_CHOICES)
    temperament = forms.ChoiceField(label='What temperament are you looking for in a pet?', choices=TEMPERAMENT_CHOICES)
    compatibility = forms.CharField(label='It is important for your new pet to get along with other family members. Please describe compatibility with other pets or children:', max_length=250)
    grooming = forms.ChoiceField(label='Consider grooming needs: Please choose grooming level:', choices=GROOMING_CHOICES)
    living_environment = forms.ChoiceField(label='Will your pet live in an apartment or a house? Please choose the living environment:', choices=ENVIRONMENT_CHOICES)
    time_commitment = forms.ChoiceField(label='How much time can you commit to spending with your new buddy? Please choose the time commitment:', choices=TIME_CHOICES)
