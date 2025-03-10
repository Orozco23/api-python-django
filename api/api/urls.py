from django.urls import path
from card import views

urlpatterns = [
    path('api/cards', views.card_list, name='card_list'),  # View to obtain all the cards
    path('api/cards/create', views.card_create, name='card_create'),  # View to create a card
    path('api/cards/update/<int:id>', views.card_update, name='card_update'),  # View to update a card
    path('api/cards/delete/<int:id>', views.card_delete, name='card_delete'),  # View to delete a card
    path('api/cards/<int:id>', views.card_detail, name='card_detail')  # View to obtain details of a card by id
]
