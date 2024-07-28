from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Person, Question, Help
from.searializers import PersonSerializer, QuestionSerializer, HelpSerializer

# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class HelpViewSet(viewsets.ModelViewSet):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer
@api_view(['GET'])
def help_count(request):
    try:
        helps = Help.objects.all()
        return JsonResponse(
            HelpSerializer(helps, many=True).data,
            safe = False,
            status = 200
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)