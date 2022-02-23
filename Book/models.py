from django.db import models

class Book(models.Model):
    GENRE_CHOICE = (
        ("Fiction", "Fiction"),
        ("Drama", "Drama"),
        ("Novella", "Novella"),
        ("Comedy", "Comedy"),
        ("Horror", "Horror"),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=60, choices=GENRE_CHOICE)
    updated_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=40)

    def __str__(self):
        return self.title

class BookFeedback(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    foreign_key = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.foreign_key.title
