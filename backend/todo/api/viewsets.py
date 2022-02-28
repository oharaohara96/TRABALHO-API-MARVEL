from rest_framework import viewsets

from backend.todo.api.serializers import TodoSerializer
from backend.todo.models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, status='a')
