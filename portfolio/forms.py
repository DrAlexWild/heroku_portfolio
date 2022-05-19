from django import forms
from django.forms import ModelForm
from .models import Blog_Post

from .models import Class
from .models import Project
from .models import Professor
from .models import Language
from .models import Hobbie
from .models import Quiz


"""class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da tarefa...'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
        }


        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'concluido': 'Concluída',
        }


        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'prioridade': 'prioridade: baixa=1, media=2, alta=3',
        }"""

class BlogPostForm(ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Blog_Post
        fields = '__all__'

        #autor data titulo descricao

        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor...'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titulo...'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descricao...'}),

            'data': forms.DateInput(format='%m/%d/%Y'),

        }


        # texto a exibir junto à janela de inserção
        labels = {
            'autor': 'Author',
            'data': 'Data',
            'titulo': 'Title',
            'descricao': 'Description',
            'image': 'Image',
        }


        # texto auxiliar a um determinado campo do formulário
        help_texts = {}

class Professor(ModelForm):
    link = forms.CharField(required=False)
    class Meta:
        model = Professor
        fields = '__all__'

class Class(ModelForm):
    class Meta:
        model = Class
        fields = '__all__'

class Project(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class Language(ModelForm):
    class Meta:
        model = Language
        fields = '__all__'

class  Hobbie(ModelForm):
    image = forms.ImageField(required=False)
    link = forms.CharField(required=False)
    class Meta:
        model = Hobbie
        fields = '__all__'


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

        # texto a exibir junto à janela de inserção
        labels = {
            #when was django launched: 2005
            'question_0': 'when was django launched',
            #whats the programming language most often used with django: Python
            'question_1': 'whats the programming language most often used with django',
            #whats the file extension most often used to add style to an html file: css
            'question_2': 'whats the file extension most often used to add style to an html file',
            #to display multiple elements inside a div we can use display: :flex
            'question_3': 'to display multiple elements inside a div we can use display',
            'name': 'the name you would like to display on the leaderboard'
        }


        # texto auxiliar a um determinado campo do formulário
        help_texts = {}