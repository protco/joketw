from django import forms

from .models import JokeUser


class JokeForm(forms.ModelForm):
    class Meta:
        model = JokeUser
        fields = ['content', 'is_original']
        widgets = {'content': forms.Textarea(attrs={'cols': 40, 'rows': 4})}
        labels = {'content': '', 'is_original': 'This is an original contribution',}


    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        if len(content) < 20 or len(content) > 250:
            raise forms.ValidationError("only english oneliner (20-250 characters) is accepted at this moment.")
        return content.capitalize()



