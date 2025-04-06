from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'last_name', 'first_name']

    def clean_user_id(self):
        user_id = self.cleaned_data.get('user_id')
        if not user_id.isdigit() or len(user_id) != 8:
            raise forms.ValidationError("User ID must be an 8-digit number.")
        if User.objects.filter(user_id=user_id).exists():
            raise forms.ValidationError("User ID is already taken.")
        return user_id