
def root_categories(request):
    return {
        'root_categories': Category.objects.filter(parent__isnull=True).order_by('priority'),
    }