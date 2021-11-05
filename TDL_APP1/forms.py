from TDL_APP1.models import Content_Article
from django.forms import ModelForm
        
class ContentCreationForm(ModelForm):
    class Meta:
        model=Content_Article
        fields = ['title', 'content']