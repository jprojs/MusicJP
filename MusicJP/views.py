from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer

from models import Album, Genre, Track, Artist


def index(request):
    return HttpResponse(Genre.objects)


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'index.html', {'genres': list(genres)})


@csrf_exempt
def average_artist(request, num=1):
    """API endpoint that allows view average song length of each artist by genre"""

    response_data = {}
    genre = Genre.objects.filter(genreid=num)[0]
    response_data['genre'] = genre

    return render(request, 'artist_average.html', {'artist_avg': response_data})


@csrf_exempt
def average_artist_json(request, num=1):
    """JSON for average_artist view"""

    response_data = []
    artists = Artist.objects.all()

    for artist in artists:
        albums = Album.objects.filter(artistid=artist.artistid)
        count = 0
        number_tracks = 0
        for album in albums:
            tracks = Track.objects.filter(genreid=num, albumid=album.albumid)
            # average
            for track in tracks:
                number_tracks += 1
                secs = int(track.milliseconds)
                count += secs

        if number_tracks != 0:
            average = count / number_tracks
            record = {'name': artist.short_name(), 'avg': str(average)}
            response_data.append(record)

    return JSONResponse(list(response_data))


@csrf_exempt
def list_table(request, num=1):
    response_data = []
    artists = Artist.objects.all()
    genre = Genre.objects.filter(genreid=num)[0];
    for artist in artists:
        albums = Album.objects.filter(artistid=artist.artistid)
        for album in albums:
            tracks = Track.objects.filter(genreid=num, albumid=album.albumid)
            for track in tracks:
                record = {}
                record['track'] = track.name
                record['artist'] = artist.name
                record['album'] = album.title
                record['duration'] = track.milliseconds
                response_data.append(record)

    paginator = Paginator(response_data, 20)
    page = request.GET.get('page')

    try:
        response_data = paginator.page(page)
    except PageNotAnInteger:
        response_data = paginator.page(1)
    except EmptyPage:
        response_data = paginator.page(paginator.num_pages)

    return render(request, 'charts.html', {'tracks': response_data, 'genre': genre})


def index(request):
    return render_to_response('index.html')
