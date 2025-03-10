from django.urls import path
from painting import views

urlpatterns = [
    path('api/paintings', views.painting_list, name='painting_list'),  # View to obtain all the paintings
    path('api/paintings/create', views.painting_create, name='painting_create'),  # View to create a painting
    path('api/paintings/update/<int:id>', views.painting_update, name='painting_update'),  # View to update a painting
    path('api/paintings/delete/<int:id>', views.painting_delete, name='painting_delete'),  # View to delete a painting
    path('api/paintings/<int:id>', views.painting_detail, name='painting_detail'),  # View to obtain details of a painting by id
]
