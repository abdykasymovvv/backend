from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('eatadd/', views.EatCreate.as_view()),
    path('eats/', views.EatList.as_view()),
    path('eat/<int:pk>/', views.EatUpdateRetrieveDelete.as_view()),
    path('tables/', views.TableListCreate.as_view()),
    path('table/<int:pk>/', views.TableUpdateRetrieveDelete.as_view()),
    path('orderHomeAdd/', views.OrderHomeListCreate.as_view()),
    path('orderhome/<int:pk>/', views.OrderHomeUpdateRetrieveDelete.as_view()),
    path('preOrderAddlist/', views.PreOrderListCreate.as_view()),
    path('preOrder/<int:pk>/', views.PreOrderUpdateRetrieveDelete.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
