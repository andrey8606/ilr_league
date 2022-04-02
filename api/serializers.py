from rest_framework.serializers import ModelSerializer

from running_results.models import Result


class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
