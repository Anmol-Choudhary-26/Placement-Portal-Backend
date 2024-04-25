from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SlotViewSet
from . import views
from .views import SlotViewSet, UnbookedSlotsView, UserSlotsView, UserBookedSlotsView, Bookslot


router = DefaultRouter()
router.register(r'slots', SlotViewSet)

urlpatterns = [
    path('', views.SlotViewSet.as_view(),name = "slot-list"),
    path('unbooked/', UnbookedSlotsView.as_view(), name='unbooked_slots'),
    path('user/<int:user_id>', UserSlotsView.as_view(), name='user_slots'),
    path('booked/', UserBookedSlotsView.as_view(), name='user_booked_slots'),
    path('book_slot/', views.Bookslot.as_view(), name='book_slot'),
]