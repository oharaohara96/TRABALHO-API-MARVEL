from django import forms
from django.core.exceptions import ValidationError

from .models import Todo


class TodoForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Todo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        # Remove a class de is_done.
        self.fields['is_done'].widget.attrs['class'] = None

        # Torna description somente leitura.
        self.fields['description'].widget.attrs['readonly'] = True

    # def clean(self):
    #     self.cleaned_data = super().clean()
    #     self.description = self.cleaned_data.get('description')
    #     self.label = self.fields['description'].label

    #     if self.description or (self.instance.pk and self.description != self.instance.description):
    #         raise ValidationError(f'O campo {self.label} não pode ser editado.')

    #     return self.cleaned_data

    def clean_description(self):
        self.description = self.cleaned_data.get('description')
        self.label = self.fields['description'].label

        if self.description or (self.instance.pk and self.description != self.instance.description):
            raise ValidationError(f'O campo {self.label} não pode ser editado.')

        return self.cleaned_data['description']
