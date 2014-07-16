from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
	parent = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'parent'}), required=False)

	class Meta:
		model = Comment
		fields = ('comment',)