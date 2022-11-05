from django import forms

from .models import Project, Review


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'thumbnail', 'description', 'live_site', 'source_code', 'tags']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }
    
    # implement style in input form 
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'input'})
        self.fields['description'].widget.attrs.update({'class': 'input'})
        self.fields['live_site'].widget.attrs.update({'class': 'input'})
        self.fields['source_code'].widget.attrs.update({'class': 'input'})


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
