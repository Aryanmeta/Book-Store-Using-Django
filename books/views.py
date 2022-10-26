from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render

from .models import Book


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    template_name = 'books/book_list.html'
    context_object_name = 'books'


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'

def BookDetailView(request, pk):
    # get book object
    book = get_object_or_404(Book, pk=pk)
    # get book comments
    book_comment = book.comments.all()
    return render(request, 'books/book_detail.html', {'book': book, 'comments': book_comment})


class BookCreateView(generic.CreateView):
    model = Book
    fields = ('title', 'author', 'description', 'price', 'cover', )
    template_name = 'books/book_create.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ('title', 'author', 'description', 'price', 'cover', )
    template_name = 'books/book_update.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
