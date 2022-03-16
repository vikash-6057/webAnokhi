from django import forms  
from notice.models import Notices
class NoticesForm(forms.ModelForm):  
    class Meta:  
        model = Notices  
        fields = "__all__"

