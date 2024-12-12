from rest_framework import generics, viewsets

from habits import paginators
from habits.models import Habit
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsOwner,)
    pagination_class = paginators.CustomPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PublicListAPIView(generics.ListAPIView):
    queryset = Habit.public_habits.all()
    serializer_class = HabitSerializer
    pagination_class = paginators.CustomPagination
