from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404, HttpResponseRedirect
from models import Feed, FeedItem

def index(request):
    planet_dict = {
            'items' : FeedItem.objects.select_related()[:3],
            'paginate_by' : 15,
            }
    return render_to_response('planet/index.html', planet_dict)

def show_item(request, item):
    post = get_object_or_404(FeedItem, pk = item)
    return render_to_response('planet/item.html', post)
