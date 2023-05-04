from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from api.models import Category, Book, Favorite
from api.serializers import BookSerializer, FavoriteSerializer


@api_view(['GET'])
def book_by_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        books = Book.objects.filter(category=category)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def book_list(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def favorite(request, user_id):
    if request.method == "GET":
        favorite = Favorite.objects.get(user_id = user_id)
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_id(request):
    user_id = request.user.id
    return JsonResponse({'user_id': user_id})


@api_view(['DELETE','GET'])
def remove_from_favorites(request, book_id):
    user_id = request.user.id
    try:
        favorite = Favorite.objects.get(user_id=user_id)
        favorite.books.remove(book_id)
        favorite.save()
        return Response({'message': f'Book item {book_id} has been removed from favorites.'})
    except Favorite.DoesNotExist:
        return Response({'error': 'No favorite found for this user.'}, status=status.HTTP_404_NOT_FOUND)
    except ValueError:
        return Response({'error': 'The specified book ID is invalid.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST','GET'])
def add_to_favorites(request, book_id):
    user_id = request.user.id
    try:
        favorite = Favorite.objects.get(user_id=user_id)
        favorite.books.add(book_id)
        favorite.save()
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data)
    except Favorite.DoesNotExist:
        return Response({'error': 'No favorite found for this user.'}, status=status.HTTP_404_NOT_FOUND)
    except ValueError:
        return Response({'error': 'The specified book ID is invalid.'}, status=status.HTTP_400_BAD_REQUEST)