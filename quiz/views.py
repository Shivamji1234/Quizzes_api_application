from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Quiz
from .serializers import QuizSerializer,QSerializer,ResultSerializer
from django.utils import timezone

#Create your view here
@api_view(['POST'])
def create_quiz(request):
    serializer = QuizSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_active_quiz(request):
    quiz = Quiz.objects.filter(Stauts="active").values()
    if quiz:
        serializer = QSerializer(quiz,many=True)
        return Response(serializer.data)
        
    return Response({'message': 'No active quiz found'}, status=404)
    
@api_view(['GET'])
def get_quiz_result(request, id):
    try:
        quiz = Quiz.objects.get(id=id)
        serializer = ResultSerializer(quiz)
        return Response(serializer.data)
    except Quiz.DoesNotExist:
        return Response({'message': 'No quiz found'},status=404)

@api_view(['GET'])
def get_all_quizzes(request):
    try:
        quiz = Quiz.objects.all() 
        serializer = QSerializer(quiz, many=True)
        return Response(serializer.data)
    except Quiz.DoesNotExist:
        return Response({'message': 'No quiz found'},status=404)
