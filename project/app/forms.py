from django import forms
from app.models import Users

class InputUser(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
