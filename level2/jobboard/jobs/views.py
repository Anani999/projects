from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView
from .models import Company, Job, Application
from .serializers import CompanySerializer, JobSerializer, ApplicationSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class JobSearchView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description', 'location']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('search', None)
        if query:
            queryset = queryset.filter(title__icontains=query)
        print(f"Search Query: {query}")
        print(f"Filtered Queryset: {query}")
        return queryset

class JobDetailView(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
