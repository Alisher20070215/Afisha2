import os
from django.core.asgi import get_asgi_application
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view (['GET'])
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'news'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.hello_world),
    path('api/v1/news/', views.get_news),
    path('api/v1/news/<int:news_id>/', views.get_news_by_id),
    path('api/v1/comments/', views.comments_list)
    ]

@api_view(['GET', 'POST'])
def get_news(request):
  if request.method == 'GET':
        news = News.objects.all() \
            .select_related('category') \
            .prefetch_related('tag', 'comments')

        search = request.query_params.get('search', None)
        if search is not None:
            news = news.filter(title__icontains=search)

        serializer = NewsDetailSerializer(instance=news, many=True)

        return Response(serializer.data)

 elif request.method == 'POST':
        title = request.data.get('title')
        content = request.data.get('content')
        category_id = request.data.get('category_id')
        tags = request.data.get('tags', [])

return Response(
            {
                "message": "Created!",
                "data": serializer.data
            },
            status=201
        )

if request.method == 'PUT':
        news.directors = request.data.get('directors', news.movies)
        news.movies = request.data.get('movies', news.movies)
        news.reviews = request.data.get('reviews', news.reviews)
        news.category_id = request.data.get('category_id', news.category_id)

        tags = request.data.get('tags', news.tag.all())
        news.tag.set(tags)

        news.save()

        serializer = NewsDetailSerializer(instance=news, many=False)

        return Response(
            data={
                "message": "updated!",
                "data": serializer.data
            },
            status=200
        )

    if request.method == 'DELETE': 
        news.delete()
        return Response(
            data={
                'message': 'deleted'
            },
            status=204
        )
