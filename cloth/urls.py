from django.urls import path
from . import views


urlpatterns = [
    path("cloth_eins_tag/", views.ClothTagEinsView.as_view(), name="first_tag"),
    path("cloth_zwei_tag/", views.ClothTagZweiView.as_view(), name="second_tag"),
    path("cloth_drei_tag/", views.ClothTagDreiView.as_view(), name="third_tag"),
    path("cloth_vier_tag/", views.ClothTagVierView.as_view(), name="fourth_tag"),
    path("cloth/", views.ClothListView.as_view(), name="product"),
    path("add_order/", views.OrderCreateView.as_view(), name="add"),
]