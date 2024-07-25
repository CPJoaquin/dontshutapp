from django.db import models
from .validators import clean_question
from .validators import clean_phone
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, validators=[clean_phone])
    city = models.CharField(max_length=100)
    created_at = models.DateField()

    def __str__(self):
        return '{} {} {} {} {}'. format(self.name, self.address, self.phone, self.city, self.created_at)

class QuestionLevel(models.TextChoices):
    BAJO = 'BAJO', 'Bajo'
    MEDIO = 'MEDIO', 'Medio'
    ALTO = 'ALTO', 'Alto'

class Question(models.Model):
    description = models.CharField(max_length=100, validators=[clean_question,])
    level = models.CharField(
        max_length=10,
        choices=QuestionLevel.choices, default=QuestionLevel.MEDIO
    )

    def __str__(self):
        return '{} {}'. format(self.description, self.level)

class Answer(models.Model):
    result = models.BooleanField(default=False)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'. format(self.result, self.question_id, self.person_id)

class Help(models.Model):
    location = models.CharField(max_length=100)
    reason = models.CharField(max_length=200)
    created_at = models.DateField()
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {} {}'. format(self.location, self.reason, self.created_at, self.person_id)
