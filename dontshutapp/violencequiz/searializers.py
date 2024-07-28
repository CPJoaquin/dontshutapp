from rest_framework import serializers
from .models import Person, Question, Help
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = "__all__"