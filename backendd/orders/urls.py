from django.urls import path
from .import views

urlpatterns = [
    path('',views.OrderCreationListView.as_view(),name='orders'),
    path('<int:order_id>/',views.OrderDetailView.as_view(),name='order detail'),
    path('update-status/<int:order_id>/',views.OrderStatusUpdateView.as_view(),name='status detail'),
    path('user/<int:user_id>/ordered',views.UserOrderView.as_view(),name='user detail'),
    path('user/<int:user_id>/ordereds/<int:order_id>/',views.UserOrderDetailView.as_view(),name='user detail order'),

]