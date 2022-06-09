from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.TypeView.as_view(), name='type'),
    path('<type_name>/', views.MealsView.as_view(), name='meals'),
    path('<type_name>/<int:pk>/', views.IngredientsView.as_view(), name='ingredients'),
    path('<int:pk>/review/', views.ReviewView.as_view(), name='review'),
    path('<int:meals_id>/vote/', views.on_vote, name='on'),
]