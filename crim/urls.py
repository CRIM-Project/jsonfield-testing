from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from crim.views.observation import ObservationList, ObservationDetail, api_root, ObservationListJSON, ObservationDetailJSON
from crim.views.relationship import RelationshipList, RelationshipDetail, RelationshipListJSON, RelationshipDetailJSON

urlpatterns = [
    path('observations/', ObservationList.as_view(), name='crimobservation-list'),
    path('observations/<int:pk>/', ObservationDetail.as_view(), name='crimobservation-detail'),
    path('data/observations/', ObservationListJSON.as_view(), name='crimobservation-list-json'),
    path('data/observations/<int:pk>/', ObservationDetailJSON.as_view(), name='crimobservation-detail-json'),

    path('relationships/', RelationshipList.as_view(), name='crimrelationship-list'),
    path('relationships/<int:pk>/', RelationshipDetail.as_view(), name='crimrelationship-detail'),
    path('data/relationships/', RelationshipListJSON.as_view(), name='crimrelationship-list-json'),
    path('data/relationships/<int:pk>/', RelationshipDetailJSON.as_view(), name='crimrelationship-detail-json'),
    
    path('', api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)