from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', home, name='about'),
    #
    path('documents/', documents, name='documents'),
    # driver documents
    path('documents/d_docs', driver_docs, name='driver_docs'),
    path('documents/d_docs/create', create_ddoc, name='create_ddoc'),
    path('documents/d_docs/<str:pk>/', driver_doc, name='driver_doc'),
    path('documents/d_docs/<str:pk>/edit', edit_ddoc, name='edit_ddoc'),
    path('documents/d_docs/<str:pk>/delete', delete_ddoc, name='delete_ddoc'),
    # driver documents
    path('documents/p_docs', partner_docs, name='partner_docs'),
    path('documents/p_docs/create', create_pdoc, name='create_pdoc'),
    path('documents/p_docs/<str:pk>/', partner_doc, name='partner_doc'),
    path('documents/p_docs/<str:pk>/edit', edit_pdoc, name='edit_pdoc'),
    path('documents/p_docs/<str:pk>/delete', delete_pdoc, name='delete_pdoc'),
    # vehicle documents
    path('documents/v_docs', vehicle_docs, name='vehicle_docs'),
    path('documents/v_docs/create', create_vdoc, name='create_vdoc'),
    path('documents/v_docs/<str:pk>/', vehicle_doc, name='vehicle_doc'),
    path('documents/v_docs/<str:pk>/edit', edit_vdoc, name='edit_vdoc'),
    path('documents/v_docs/<str:pk>/delete', delete_vdoc, name='delete_vdoc'),
    # drivers
    path('drivers/', drivers, name='drivers'),
    path('drivers/create', create_driver, name='create_driver'),
    path('drivers/<str:pk>/', driver, name='driver'),
    path('drivers/<str:pk>/edit', edit_driver, name='edit_driver'),
    path('drivers/<str:pk>/delete', delete_driver, name='delete_driver'),
    # partners
    path('partners/', partners, name='partners'),
    path('partners/create', create_partner, name='create_partner'),
    path('partners/<str:pk>/', partner, name='partner'),
    path('partners/<str:pk>/edit', edit_partner, name='edit_partner'),
    path('partners/<str:pk>/delete', delete_partner, name='delete_partner'),
    # vehicles
    path('vehicles/', vehicles, name='vehicles'),
    path('vehicles/<str:pk>/', vehicle, name='vehicle'),
    path('vehicles/create', create_vehicle, name='create_vehicle'),
    path('vehicles/<str:pk>/edit', edit_vehicle, name='edit_vehicle'),
    path('vehicles/<str:pk>/delete', delete_vehicle, name='delete_vehicle'),
    # incidents
    path('incidents/', incidents, name='incidents'),
    path('incidents/create', create_incident, name='create_incident'),
    path('incidents/<str:pk>/', incident, name='incident'),
    path('incidents/<str:pk>/edit', edit_incident, name='edit_incident'),
    path('incidents/<str:pk>/delete', delete_incident, name='delete_incident'),
    # parameters
    path('parameters/', parameters, name='parameters'),
]
