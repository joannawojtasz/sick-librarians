from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        object_id = forms.IntegerField(widget=forms.HiddenInput)
        content = forms.CharField(label='', widget=forms.Textarea)
        model = Comment
        fields = ('body',)
