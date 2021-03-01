from django.contrib import messages
from django.shortcuts import redirect, reverse
from movies import models as movie_models
from . import forms


def create_review(request, movie):
    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        movie = movie_models.Movie.objects.get_or_none(pk=movie)
        if not movie:
            return redirect(reverse("core:home"))
        if form.is_valid():
            review = form.save()
            review.movie = movie
            review.user = request.user
            review.save()
            messages.success(request, "Movie reviewed")
            return redirect(reverse("movies:detail", kwargs={"pk": movie.pk}))
