def filter_form(form, queryset):
    if form.is_valid(): 
        name = form.cleaned_data.get('name', '').strip()
        if name:
            queryset = queryset.filter(name__icontains = name)

        date_from = form.cleaned_data.get('date_from','')
        if date_from:
            queryset = queryset.filter(date__gte = date_from)

        date_to = form.cleaned_data.get('date_to','')
        if date_to:
            queryset = queryset.filter(date__lte = date_to)

        price_from = form.cleaned_data.get('price_from','')
        if price_from:
            queryset = queryset.filter(price__gte = price_from)

        price_to = form.cleaned_data.get('price_to','')
        if price_to:
            queryset = queryset.filter(price__lte = price_to)

        price_sort = form.cleaned_data.get('price_sort', '')
        if price_sort == 'ASC':
            queryset = queryset.order_by('price')
        elif price_sort == 'DESC':
            queryset = queryset.order_by('-price')
    
    return queryset