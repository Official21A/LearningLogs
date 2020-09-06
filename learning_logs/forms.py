from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	# this class is our topic input form
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''}


class EntryForm(forms.ModelForm):
	# this class is our entry input form
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}
