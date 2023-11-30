from django import forms

class usersForm(forms.Form):
    fname = forms.CharField(label="First Name", required=True)
    lname = forms.CharField(label="Last Name", required=False)
    email = forms.EmailField(label="Email ID")
    desc = forms.CharField(label="Desciption", required=False, widget=forms.Textarea(attrs={'class' : 'descr'}))