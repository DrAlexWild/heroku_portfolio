from django.contrib import admin

# Register your models here.
from .models import Blog_Post
from .models import Professor
from .models import Project
from .models import Class
from .models import Language
from .models import Hobbie
from .models import Quiz
from .models import Project_image_description


admin.site.register(Blog_Post)
admin.site.register(Professor)
admin.site.register(Class)
admin.site.register(Project)
admin.site.register(Language)
admin.site.register(Hobbie)
admin.site.register(Quiz)
admin.site.register(Project_image_description)