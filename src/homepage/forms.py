# src/homepage/forms.py

from django import forms

class HomePageForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    email2 = forms.EmailField(label='Confirm Email')

    # How to update the css class for the form fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print(self.fields)
        for field in self.fields:
            # print(field)
            default_css_class = 'form-control' # bootstrap

            new_attrs = {
                'class': default_css_class,
                'id': f'{field}',
                'placeholder': f'Your {field}'
            }

            if field == 'email2':
                new_attrs['placeholder'] = f'Confirm your email'
            self.fields[field].widget.attrs.update(new_attrs)

    # fields data and error
    def clean(self):
        data = self.cleaned_data
        email = data.get('email')
        email2 = data.get('email2')

        if email2 != email:
            # self.add_error('email', 'Email not match, please try again')
            raise forms.ValidationError('Email not match, please try again')
        return data
