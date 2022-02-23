from django.shortcuts import render
from . import models, forms
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import reverse, redirect
from django.views import generic



class BooksListView(generic.ListView):
    template_name = "books_list.html"
    queryset = models.Books.objects.all()

    def get_queryset(self):
        return self.queryset


# def get_books_all(request):
#     books = models.Books.objects.all()
#     return render(request, "books_list.html", {"books": books})


class BooksDetailView(generic.DetailView):
    template_name = "books_detail.html"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=books_id)


# def get_books_detail(request, id
#     book = get_object_or_404(models.Books, id=id)
#     comment_id = models.BookComments.objects.filter(books_id=id)
#     return render(request, "books_detail.html", {"book": book, 'comment': comment_id})):


class BooksCreateView(generic.CreateView):
    template_name = "add_books.html"
    form_class = forms.Books_all
    queryset = models.Books.objects.all()
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BooksCreateView, self).form_valid(form=form)


# def all_books(request):
#     method = request.method
#     if method == "POST":
#         form = forms.Books_all(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("books:books_list"))
#             # return HttpResponse("Books Created Successfully")
#     else:
#         form = forms.Books_all()
#     return render(request, "add_books.html", {"form": form})


class BooksUpdateView(generic.UpdateView):
    template_name = "books_update.html"
    form_class = forms.Books_all
    success_url = "/books/"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=books_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BooksUpdateView, self).form_valid(form=form)


# def put_books_update(request, id):
#     book_id = get_object_or_404(models.Books, id=id)
#     if request.method == "POST":
#         form = forms.Books_all(instance=book_id,
#                                data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("books:books_list"))
#     else:
#         form = forms.Books_all(instance=book_id)
#     return render(request, "books_update.html", {"form": form,
#                                                  "book": book_id})

class BooksDeleteView(generic.DeleteView):
    template_name = "confirm_delete_book.html"
    success_url = "/books/"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=books_id)


# def book_delete(request, id):
#     book_id = get_object_or_404(models.Books, id=id)
#     book_id.delete()
#     # return HttpResponse("Book Deleted")
#     return redirect(reverse("books:books_list"))




