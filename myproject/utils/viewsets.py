from rest_framework import routers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from utils.utils_sat import four_months_before
from utils.views import satellite_analysis
from rest_framework import status
from datetime import datetime


class CalculateFourMonthsBeforeViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def calculate(self, request):
        date = request.data.get('date')
        date = str(datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ'))[:10]
        calculation = four_months_before(date)  # Assuming four_months_before is imported
        return Response({'Calculated date 4 months before': calculation})



class CalculateDeforestationRateViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def calculate(self, request):
        project = request.data.get('project')
        calculation = satellite_analysis(project)  
        return Response({'Calculated Deforestation Rate': calculation})


router = routers.SimpleRouter()
#router.register(r'calculate_four_months_before', CalculateFourMonthsBeforeViewSet, basename="calculate_four_months_before")
router.register(r'calculate_deforestation_rate', CalculateDeforestationRateViewSet, basename="calculate_deforestation_rate")
urlpatterns = router.urls
