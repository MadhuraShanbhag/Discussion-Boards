from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
	message = forms.CharField(
		widget=forms.Textarea(
			attrs={'rows': 5, 'placeholder': 'What\'s on your mind today?'}
			),
		max_length=5000,
		help_text='Maximum text length is 5000 characters.'
		)

	class Meta:
		model = Topic
		fields = ['subject', 'message']