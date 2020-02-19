from django import forms


class Sign_Up(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=30)
    last_name = forms.CharField(label='last_name', max_length=30)
    email = forms.EmailField(label='email', max_length=30)
    password = forms.CharField(label='password', max_length=30)

    def clean(self):
        cleaned_data = super(Sign_Up, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('last_name')
        password = cleaned_data.get('password')

        if not first_name and not last_name and not email and not password:
            raise forms.ValidationError('You have to write something!')


class Login(forms.Form):
    email = forms.EmailField(label='email', max_length=30)
    password = forms.CharField(label='password', max_length=30)
