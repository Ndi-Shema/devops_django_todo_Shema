from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ToDo
from .serializers import ToDoSerializer
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create a new ToDo
class ToDoCreateView(generics.CreateAPIView):


    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]



class ToDoListView(generics.ListAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)

# Retrieve, Update or Delete a specific ToDo
class ToDoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')