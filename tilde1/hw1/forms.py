from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=200)


class ActionForm(forms.Form):
    action = forms.CharField(label='Action', max_length=200)
    amount = forms.IntegerField()


