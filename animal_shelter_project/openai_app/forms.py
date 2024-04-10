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

    AGE_CHOICES = [
        ('any', 'Any Age'),
        ('young', 'Young (0-2 years)'),
        ('adult', 'Adult (3-8 years)'),
        ('senior', 'Senior (9+ years)'),
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

    pet_type = forms.ChoiceField(label='Pet Type', choices=PET_CHOICES)
    size = forms.ChoiceField(label='Size', choices=SIZE_CHOICES)
    age = forms.ChoiceField(label='Age', choices=AGE_CHOICES)
    activity_level = forms.ChoiceField(label='Activity Level', choices=ACTIVITY_CHOICES)
    temperament = forms.ChoiceField(label='Temperament', choices=TEMPERAMENT_CHOICES)
    compatibility = forms.CharField(label='Compatibility with Other Pets or Children', max_length=250)
    grooming = forms.ChoiceField(label='Grooming Needs', choices=GROOMING_CHOICES)
    living_environment = forms.ChoiceField(label='Living Environment', choices=ENVIRONMENT_CHOICES)
    time_commitment = forms.ChoiceField(label='Time Commitment', choices=TIME_CHOICES)