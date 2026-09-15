from django.shortcuts import render
from .models import register
from .models import MediaItem

def index(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        password = request.POST.get('password')

        register.objects.create(userid=userid, password=password)

        return render(request, "index.html")

    return render(request, "index.html")


def sign(request):
    return render(request, "sign.html")


def login(request):
    return render(request, "login.html")


def download(request):
    return render(request, "download.html")





def home(request):
    songs = MediaItem.objects.filter(category='song')
    artists = MediaItem.objects.filter(category='artist')
    albums = MediaItem.objects.filter(category='album')
    radios = MediaItem.objects.filter(category='radio')

    context = {
        'songs': songs,
        'artists': artists,
        'albums': albums,
        'radios': radios,
    }

    return render(request, 'index.html', context)
