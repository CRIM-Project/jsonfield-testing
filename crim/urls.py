from django.urls import path
from crim.views.observation import ObservationList, ObservationDetail, api_root
from crim.views.relationship import RelationshipList, RelationshipDetail

urlpatterns = [
    path('data/observations/', ObservationList.as_view(), name='crimobservation-list'),
    path('data/observations/<int:pk>/', ObservationDetail.as_view(), name='crimobservation-detail'),
    path('data/relationships/', RelationshipList.as_view(), name='crimrelationship-list'),
    path('data/relationships/<int:pk>/', RelationshipDetail.as_view(), name='crimrelationship-detail'),
    
    path('', api_root),
]