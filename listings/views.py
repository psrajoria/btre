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

    query_list = Listing.objects.order_by('-list_date')

    #keywords for search
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(description__icontains=keywords)

    #city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact=city)
    

    #state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_list = query_list.filter(state__iexact=state)


    #bedroom
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_list = query_list.filter(bedrooms__lte=bedrooms)

    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_list = query_list.filter(price__lte=price)

    context = {
        'state_choices':state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings':query_list,
        'values' : request.GET
    }
    return render(request, 'listings/search.html',context)
