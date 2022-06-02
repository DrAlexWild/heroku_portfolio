from django.db import models

# Create your models here.

#autor data titulo descricao

class Blog_Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    data = models.DateField()
    descricao = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.titulo[:50]

# models.py

class Language(models.Model):
    nome = models.CharField(max_length=60)
    ano = models.IntegerField()
    descricao = models.TextField(max_length=2000)
    def __str__(self):
        return self.nome[:50]

class Professor(models.Model):
    nome = models.CharField(max_length=60)
    link = models.CharField(max_length=2000)
    def __str__(self):
        return self.nome[:50]

class Projetc_topic(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=2000)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name[:60]

class Project(models.Model):
    nome = models.CharField(max_length=60)
    ano = models.IntegerField()
    descricao = models.TextField()
    linguagens = models.ManyToManyField(Language)
    project_topics = models.ManyToManyField(Projetc_topic)
    link = models.CharField(max_length=2000)
    def __str__(self):
        return self.nome[:50]

class Class(models.Model):
    nome = models.CharField(max_length=60)
    ano = models.IntegerField()
    descricao = models.TextField(max_length=2000)
    linguagens = models.ManyToManyField(Language)
    docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE)
    docentes_praticas = models.ManyToManyField(Professor, related_name='caderias')
    projetos = models.ForeignKey(Project, on_delete=models.CASCADE)
    ects = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    def __str__(self):
        return self.nome[:50]

class Hobbie(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=2000)
    link = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name[:50]

class Quiz(models.Model):
    #when was django launched: 2005
    question_0 = models.IntegerField(default=0)
    #whats the programming language most often used with django: Python
    question_1 = models.CharField(max_length=20)
    #whats the file extension most often used to add style to an html file: css
    question_2 = models.CharField(max_length=20)
    #to display multiple elements inside a div we can use display: :flex
    question_3 = models.CharField(max_length=10)

    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name[:50]


class News_Article(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=2000)
    link = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name[:100]

class Web_Techniques(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=2000)
    link = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name[:100]


