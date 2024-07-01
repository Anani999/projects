from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, JobSearchView, ApplicationViewSet, JobDetailView

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'applications', ApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('jobs/search/', JobSearchView.as_view(), name='job-search'),  # Ensure the search path is correct
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),  # Add this line for job detail view
]
