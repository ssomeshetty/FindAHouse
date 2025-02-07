from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from .forms import ListingForm

# View for listing all real estate listings
def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listing_list.html', {'listings': listings})

# View for showing a single listing's details
def listing_retreve(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listing_detail.html', {'listing': listing})

# View for creating a new listing
def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listing_list')
    else:
        form = ListingForm()
    return render(request, 'listing_add.html', {'form': form})

# View for editing an existing listing
def listing_update(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing_retreve', pk=listing.pk)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listing_edit.html', {'form': form, 'listing': listing})
