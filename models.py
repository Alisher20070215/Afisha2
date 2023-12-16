class News(models.Model):
    directors = models.CharField(max_length=150, verbose_name='Directors')
    movies = models.CharField(max_length=150, verbose_name='Movies')
    content = models.TextField(blank=True, verbose_name='Reviews')

class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'director', 'movies')

@api_view(['GET'])
def directors_list(request):
    directors = Directors.objects.all()

@api_view(['GET'])
def directors_list(request):
    SELECT * FROM
    directors_directors
    WHERE
    id = directors_id

@api_view(['GET'])
def movies_list(request):
    movies = Movies.objects.all()

@api_view(['GET'])
def movies_list(request):
    SELECT * FROM
    movies_movies
    WHERE
    id = movies_id

@api_view(['GET'])
def reviews_list(request):
    reviews = Reviews.objects.all()

@api_view(['GET'])
def reviews_list(request):
    SELECT * FROM
    reviews
    WHERE
    id = reviews_id
