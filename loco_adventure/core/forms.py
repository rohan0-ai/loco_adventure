from django import forms
from adventures.models import Adventure
from django.contrib.auth.forms import UserCreationForm
from .models import User

class AdventureForm(forms.ModelForm):
    class Meta:
        model = Adventure
        fields = ['title', 'price', 'capacity', 'start_time', 'end_time', 'adventure_type', 'address', 'description', 'online_booking', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-lg border border-gray-300 focus:ring-2 focus:ring-purple-500',
                'placeholder': 'Adventure Title'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-lg border border-gray-300 focus:ring-2 focus:ring-purple-500',
                'placeholder': 'Base Price (₹)'
            }),
            'capacity': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-lg border border-gray-300 focus:ring-2 focus:ring-purple-500',
                'placeholder': 'Max Capacity'
            }),
            'start_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'mt-1 block w-full rounded-lg border border-gray-300 focus:ring-2 focus:ring-purple-500'
            }),
            'end_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'mt-1 block w-full rounded-lg border border-gray-300 focus:ring-2 focus:ring-purple-500'
            }),
            'adventure_type': forms.Select(attrs={
                'class': 'mt-1 block w-full rounded-lg border border-gray-300 focus:ring-2 focus:ring-purple-500'
            }),
            'address': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-lg border border-gray-300 focus:ring-2 focus:ring-purple-500',
                'placeholder': 'Enter the address of the adventure location'
            }),
            'description': forms.Textarea(attrs={
                'class': 'mt-1 block w-full rounded-lg border border-gray-300 focus:ring-2 focus:ring-purple-500',
                'placeholder': 'Enter a description of the adventure',
                'rows': 4,
            }),
            'online_booking': forms.CheckboxInput(attrs={
                'class': 'mt-1 rounded border-gray-300 text-purple-600 focus:ring-purple-500'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'mt-1 block w-full text-gray-700'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        adventure_type = cleaned_data.get('adventure_type')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if adventure_type == 'EVENT':
            if not start_time:
                self.add_error('start_time', 'Start time is required for event type.')
            if not end_time:
                self.add_error('end_time', 'End time is required for event type.')
        return cleaned_data

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not address or address.strip() == '':
            raise forms.ValidationError("Address is required.")
        if len(address) > 255:
            raise forms.ValidationError("Address must be 255 characters or fewer.")
        return address

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class AdventureFilterForm(forms.Form):
    category = forms.ChoiceField(
        choices=[('', 'All Categories')] + Adventure.TYPES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'p-4 border rounded-xl focus:outline-none focus:ring-2 focus:ring-purple-500'
        })
    )
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search adventures...',
            'class': 'flex-1 p-4 border rounded-xl focus:outline-none focus:ring-2 focus:ring-purple-500'
        })
    )
