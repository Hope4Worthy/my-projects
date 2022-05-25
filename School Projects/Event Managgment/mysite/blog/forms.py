from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q

RATINGS = (
    (1, 'poor'),
    (2, 'fair'),
    (3, 'average'),
    (4, 'good'),
    (5, 'great')
)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','rating','body',)
        #widget = {
		#	'name':  forms.TextInput(attrs={'class':'form-contral'}),
		#	'rating': forms.Select(choices=RATINGS, attrs={'class':'form-contral'}),
		#	'body':  forms.TextInput(attrs={'class':'form-contral'}),
		#}

def validate_email(value):
	if not value.endswith('.edu'):
		raise ValidationError("only .edu emalis accepted")

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True, validators=[validate_email])

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['name', 'event_type','host', 'location', 'day', 'start_time', 'end_time', 'description']
	
	

class RsoForm(forms.ModelForm):
	class Meta:
		model = Rso
		fields = ['name','description', 'students']

		
