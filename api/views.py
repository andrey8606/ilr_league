from rest_framework import status, viewsets
from rest_framework.response import Response

from running_results.models import Result
from .serializers import ResultSerializer
from rest_framework.decorators import api_view


class ResultsViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        many = isinstance(data, list)
        serializer = self.get_serializer(data=data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


@api_view(['DELETE'])
def delete_all(request):
    if request.method == 'DELETE':
        Result.objects.all().delete()
        return Response({'message': 'Таблица с результатами успешно очищена!'})
    return Response({'message': 'Это был не DELETE-запрос!'})
