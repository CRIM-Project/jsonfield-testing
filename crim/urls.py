from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from crim.views.observation import ObservationList, ObservationDetail, api_root, ObservationListJSON, ObservationDetailJSON
from crim.views.relationship import RelationshipList, RelationshipDetail, RelationshipListJSON, RelationshipDetailJSON
from crim.views.definition import DefinitionList, DefinitionDetail, DefinitionListJSON, DefinitionDetailJSON
from crim.views.relationship_form import get_relationship
urlpatterns = [
    path('observations/', ObservationList.as_view(), name='crimobservation-list'),
    path('observations/<int:pk>/', ObservationDetail.as_view(), name='crimobservation-detail'),
    path('data/observations/', ObservationListJSON.as_view(), name='crimobservation-list-json'),
    path('data/observations/<int:pk>/', ObservationDetailJSON.as_view(), name='crimobservation-detail-json'),

    path('relationships/', RelationshipList.as_view(), name='crimrelationship-list'),
    path('relationships/<int:pk>/', RelationshipDetail.as_view(), name='crimrelationship-detail'),
    path('data/relationships/', RelationshipListJSON.as_view(), name='crimrelationship-list-json'),
    path('data/relationships/<int:pk>/', RelationshipDetailJSON.as_view(), name='crimrelationship-detail-json'),
    
    path('definitions/', DefinitionList.as_view(), name='crimdefinition-list'),
    path('definitions/<int:pk>/', DefinitionDetail.as_view(), name='crimdefinition-detail'),
    path('data/definitions/', DefinitionListJSON.as_view(), name='crimdefinition-list-json'),
    path('data/definitions/<int:pk>/', DefinitionDetailJSON.as_view(), name='crimdefinition-detail-json'),

    path('forms/relationship/', get_relationship, name='relationship-form'),
    path('', api_root, name='home-view'),
]

urlpatterns = format_suffix_patterns(urlpatterns)