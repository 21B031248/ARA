from api import views
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view()),
    path('categories/<int:category_id>', views.CategoryDetailAPIView.as_view()),
    path('categories/<int:category_id>/books', views.book_by_category),
    path('books/', views.book_list),
    path('login/', obtain_jwt_token),
    path('favorite/<int:user_id>', views.favorite),
    path('add-to-favorite/<int:book_id>/', views.add_to_favorites),
    path('user_id/', views.get_user_id),
    path('remove-from-favorite/<int:book_id>/', views.remove_from_favorites),
]