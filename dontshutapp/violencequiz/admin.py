from django.contrib import admin
from .models import Person
from .models import Question
from .models import Answer
from .models import Help
# Register your models here.

admin.site.register(Person)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Help)
