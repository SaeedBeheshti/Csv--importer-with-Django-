from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ImportJob
from .serializers import ImportJobSerializer
from .celery_tasks import process_csv

class ImportJobViewSet(viewsets.ModelViewSet):
    queryset = ImportJob.objects.all()
    serializer_class = ImportJobSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'], url_path='import-csv')
    def import_csv(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        job = ImportJob.objects.create(status='pending')
        process_csv.delay(file.read().decode('utf-8'), job.id)
        return Response(ImportJobSerializer(job).data, status=status.HTTP_201_CREATED)

"""
                                        ANOTHER WAY OF CREATING VIEWS WITH APIviews:
                    
"""
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import ImportJob
# from .serializers import ImportJobSerializer
# from .celery_tasks import process_csv
#
#
# class ImportCSVView(APIView):
#     def post(self, request):
#         file = request.FILES.get('file')
#         if not file:
#             return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)
#
#         job = ImportJob.objects.create(status='pending')
#         process_csv.delay(file.read().decode('utf-8'), job.id)
#         return Response(ImportJobSerializer(job).data, status=status.HTTP_201_CREATED)
#
