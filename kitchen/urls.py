from django.urls import path
from views import index, DishTypeListView, DishTypeCreateView, DishTypeUpdateView, DishTypeDeleteView, DishListView, \
    DishCreateView, DishUpdateView, DishDeleteView, DishDetailView

urlpatterns = [
    path("", index, name="index"),
    path(
        "dishtypes/",
        DishTypeListView.as_view(),
        name="dish-type-list",
    ),
    path(
        "dishtypes/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "dishtypes/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dishtypes/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list",
    ),
    path(
        "dishes/create/",
        DishCreateView.as_view(),
        name="dish-create",
    ),
    path(
        "dishes/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update",
    ),
    path(
        "dishes/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete",
    ),
    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail"
    ),
]


app_name = "kitchen"
