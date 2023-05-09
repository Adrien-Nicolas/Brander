from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.conf import settings
import re
import json
from .models import User, TextAnalysis
from .serializers import UserSerializer, TextAnalysisSerializer
from rest_framework.decorators import api_view
import os
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
import openai
import random
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ObtainTokenPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.user
            token_data = serializer.validated_data

            response_data = {
                'user_id': user.id,
                'username': user.username,
                'access_token': token_data['access'],
                'refresh_token': token_data['refresh'],
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class TextAnalysisList(generics.ListCreateAPIView):
    queryset = TextAnalysis.objects.all()
    serializer_class = TextAnalysisSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class TextAnalysisDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TextAnalysis.objects.all()
    serializer_class = TextAnalysisSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class UserTextAnalysisList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        text_analyses = user.textanalysis_set.all()
        serializer = TextAnalysisSerializer(text_analyses, many=True)
        return Response(serializer.data)

    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TextAnalysisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TextAnalysisUserList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, text_analysis_id):
        try:
            text_analysis = TextAnalysis.objects.get(id=text_analysis_id)
        except TextAnalysis.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user = text_analysis.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request, text_analysis_id):
        try:
            text_analysis = TextAnalysis.objects.get(id=text_analysis_id)
        except TextAnalysis.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            text_analysis.user = serializer.instance
            text_analysis.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST', 'GET'])
def generate_design(request):
    # Authenticate OpenAI API client
    # openai_api_key = getattr(settings, 'OPENAI_API_KEY', None)
    # if not openai_api_key:
    #     raise ValueError('OpenAI API key is not set in Django settings file')
    

    #------------------Put your API key here----------------------
    openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    # Get input text and mood from request data
    print(request)
    text = request.GET.get('text')
    mood = request.GET.get('mood')

    if not text:
        return JsonResponse({'error': 'Text is missing from request body'}, status=400)
    
    if not mood:
        return JsonResponse({'error': 'Mood is missing from request body'}, status=400)

    prompt = f"As a design developer, you have to create a total Brand style, " \
         f"give me the hexadecimal code for a good color palette, a proposal of font policy " \
         f"appropriated for the following project: {text} and by taking into account " \
         f"the following mood: {mood} and also an original title for this project described. Your response must be in this correct json format (don't forget double quotes on each properties): " \
         f"Colors: [tab of hexa code],Font: [tab of font policy], Justification: little text of 20 carac to justify the font and colors proposed, Title : name of the project"



    # Generate design parameters using ChatGPT
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=200,
            n=1,
            stop=None,
            timeout=60,
        )
    except openai.Error as e:
        return JsonResponse({'error': str(e)}, status=500)
    #split response to extract color palette and font policy

    # Parse response to extract color palette and font policy
    response_text = response.choices[0].text

    #delete all the text before the first {
    response_text = response_text[response_text.find("{"):]

    print(response_text)
    json_load = json.loads(response_text)
    print(json_load)

    # Return response with generated design parameters
    return JsonResponse({
        'Colors': json_load["Colors"],
        'Font': json_load["Font"],
        'Justification': json_load["Justification"],
        'Title': json_load["Title"]
    })
