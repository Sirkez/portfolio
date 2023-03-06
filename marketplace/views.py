from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, View, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Auction, Category 
from .forms import AuctionForm, AuctionFilterForm
from . import utils

from accounts.models import CustomUser


class AuctionCreateView(LoginRequiredMixin  ,CreateView):
    model = Auction
    form_class = AuctionForm
    template_name = 'marketplace/create.html'
    success_url = reverse_lazy('marketplace:index')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class MarketplaceListView(ListView):
    model = Auction
    paginate_by = 5
    template_name = 'marketplace/index.html'
    context_object_name = 'auctions'
    
    def get_context_data(self, object_list = None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(name__icontains = q)

        form = AuctionFilterForm(self.request.GET)
        queryset = utils.filter_form(form, queryset)

        return super().get_context_data(**kwargs,
                    categories = Category.objects.all(),
                    object_list = queryset,
                    form=form
                    )


class AuctionDetailView(DetailView):
    model = Auction
    template_name = 'marketplace/auction.html'
    context_object_name = 'auction'

    # Display Auction details
    def get_context_data(self, **kwargs):
        watchlist = None
        if self.request.user.is_authenticated:
            if Auction.objects.get(pk = self.kwargs['pk']) in CustomUser.objects.get(id = self.request.user.id).watchlist.all():
                watchlist = True
            else:
                watchlist = None
        return super().get_context_data(**kwargs,
                    category = Auction.objects.get(pk = self.kwargs['pk']).category,
                    watchlist = watchlist)
                                                

class CategoryListView(ListView):
    model = Auction
    template_name = 'marketplace/category.html'
    context_object_name = 'auctions'
    paginate_by = 5

    # Display auctions by category
    def get_context_data(self, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list
        category = self.kwargs['category']
        queryset = queryset.filter(category__name = category)
        form = AuctionFilterForm(self.request.GET)
        queryset = utils.filter_form(form, queryset)
        count = queryset.count()                                

        return super().get_context_data(
                    object_list = queryset,
                    form = form,
                    category = category,
                    count = count,
                    **kwargs)


class WatchlistView(LoginRequiredMixin, ListView):
    model = Auction
    template_name='marketplace/watchlist.html'
    paginate_by = 5
    context_object_name = 'watchlist'

    # Display watchlist    
    def get_context_data(self,  object_list=None, **kwargs):
        user_watchlist = CustomUser.objects.get(id = self.request.user.id).watchlist.all()
        return super().get_context_data(
                    object_list = user_watchlist,
                    count = user_watchlist.count(),
                    **kwargs)
    

    # Adding Auction to watchlist
    def post(self, request):
        user_watchlist = CustomUser.objects.get(id = self.request.user.id).watchlist
        id = self.request.POST.get('id')
        slug = Auction.objects.get(id = id).slug

        if Auction.objects.get(id = id) in user_watchlist.all():
            if self.request.POST.get('remove_watchlist'):
                user_watchlist.remove(id)
        else:
            if self.request.POST.get('add_watchlist'):
                user_watchlist.add(id)

        return redirect('marketplace:auction', id, slug)
    

class MyAuctionsListView(ListView):
    model = Auction
    template_name = 'marketplace/my_auctions.html'
    paginate_by = 5
    context_object_name = 'auctions'

    def get_context_data(self, object_list = None, **kwargs):
        object_list = Auction.objects.filter(created_by = self.request.user.id)

        return super().get_context_data(object_list = object_list, **kwargs)
    

class MyAuctionUpdateView(LoginRequiredMixin, UpdateView):
    model = Auction
    template_name = 'marketplace/update.html'
    context_object_name = 'auction'
    fields = ['name', 'category', 'price', 'photo', 'description']

    def dispatch(self, request, *args, **kwargs):
        # Making sure that only authors can update stories
        obj = self.get_object()
        if obj.created_by != self.request.user:
            return redirect('marketplace:index')
        return super(MyAuctionUpdateView, self).dispatch(request, *args, **kwargs)


class MyAuctionDeleteView(LoginRequiredMixin ,DeleteView):
    model = Auction
    template_name = 'marketplace/delete.html'
    context_object_name = 'auction'
    success_url = reverse_lazy('marketplace:my_auctions')

    def dispatch(self, request, *args, **kwargs):
        # Making sure that only authors can delete stories
        obj = self.get_object()
        if obj.created_by != self.request.user:
            return redirect('marketplace:index')
        return super(MyAuctionDeleteView, self).dispatch(request, *args, **kwargs)

