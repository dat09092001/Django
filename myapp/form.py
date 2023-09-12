from django import forms
from .models import sinhvien,khoa,comment
class sinhvienFrom(forms.ModelForm):
    class Meta:
        model=khoa
        # fields=["masv","tensv","school","khoa","lop","image","gender"]
        fields="__all__"
class sinhvienForm1(forms.ModelForm):
    class Meta:
        model=sinhvien
        fields="__all__"
class formlogin(forms.Form):
    username=forms.CharField(max_length=10)
    password=forms.CharField(widget=forms.PasswordInput)
class commentsfrom(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta:
        model=comment
        fields=("text",)