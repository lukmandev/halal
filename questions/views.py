from rest_framework.viewsets import ModelViewSet

from questions.models import Question
from questions.serializers import QuestionSerializer


class QuestionMVS(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'id'
