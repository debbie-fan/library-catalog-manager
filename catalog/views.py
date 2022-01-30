from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Available genres (name = 'Science Fiction')
    num_genres_scifi = Genre.objects.filter(name__iexact='Science Fiction').count()
    num_genres_fantasy = Genre.objects.filter(name__iexact='fantasy').count()

    # The 'all()' is implied by default
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres_scifi' : num_genres_scifi,
        'num_genres_fantasy' : num_genres_fantasy,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)