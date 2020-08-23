from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import price_choices, bedroom_choices,state_choices

# Create your views here.
from .models import Listing
from .models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)  #- for descending
    paginator = Paginator(listings, 6) #paginatioin
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):

    listing = get_object_or_404(Listing,pk=listing_id)

    context={
        'listing': listing
    }
    return render(request, 'listings/listing.html',context)


def search(request):

    query_listings = Listing.objects.order_by('-list_date')


    context = {
        'state_choices':state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings':query_listings
    }
    return render(request, 'listings/search.html',context)
