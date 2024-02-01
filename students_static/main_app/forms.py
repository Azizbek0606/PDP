from django import forms
from .models import Student


class UpdateStudentsProfile(forms.ModelForm):

    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['student_name', 'age', 'gander', "payment" , 'lavel', 'descrition' , 'img' , 'admin']

        widgets = {
            'student_name': forms.TextInput(attrs={"class": "name_input", 'placeholder': 'Your name'}),
            'age': forms.TextInput(attrs={"class": "name_input", 'placeholder': 'Your age'}),
            'gander': forms.Select(attrs={"class": "name_input"}),
            'lavel': forms.Select(attrs={"class": "name_input"}),
            'descrition': forms.Textarea(attrs={"class": "desctiption", 'placeholder': 'Description'}),
        }
        
