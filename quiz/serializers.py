from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields=['id', 'question', 'options', 'right_answer', 'start_date', 'end_date']
            
class QSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields=['id', 'question', 'options', 'start_date', 'end_date']

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields=['id',  'right_answer' ]
