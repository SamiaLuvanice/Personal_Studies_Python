from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from livraria.models import Book

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control', 'placeholder': 'Digite seu email'
            }
    ))
    
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'form-control', 'placeholder': 'Digite seu nome'
            }
    ))
    last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'form-control', 'placeholder': 'Digite seu sobrenome'
            }
    ))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User name'
        self.fields['username'].label= ''
        self.fields['username'].help_text = '''
            <span class="form-text text-muted">
                <small>Obrigatório. 150 caracteres ou menos. Letras, dígitos e alguns caracteres</small>
            </span>
        '''
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label= ''
        self.fields['password1'].help_text = '''
            <ul class="form-text text-muted small">
                <li>Sua senha não pode ser muito parecida com suas outras informações pessoais.</li>
                <li>Sua senha deve conter pelo menos 8 caracteres.</li>
                <li>Sua senha não pode ser uma senha comumente usada.</li>
                <li>Sua senha não pode ser inteiramente numérica.</li>
            </ul>
        '''
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label= ''
        self.fields['password2'].help_text = '''
            <span class="form-text text-muted">
                <small>Confirme sua senha</small>
            </span>
        '''
        
class AddBookForm(forms.ModelForm):
    title = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite o título do livro'}
        ), label=''
    )
    description = forms.CharField(
        required=True, 
        widget=forms.Textarea(
        attrs={
            'class': 'form-control', 'placeholder': 'Digite a descrição do livro'
            }
        ), label=''
    )
    year = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite o ano do livro'}
        ), label=''
    )
    genre = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite o gênero do livro'}
        ), label=''
    )
    value = forms.FloatField(
        required=True,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite o valor do livro'}
        ), label='' 
    )

    class Meta:
        model = Book
        fields = ['title', 'description', 'year', 'genre', 'value']