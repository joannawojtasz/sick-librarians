from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 9

class DetailView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True, reply__isnull=True).order_by("created_on")

        return render(
            request,
            "detail_view.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                # "comment_form": CommentForm()
            },
        )
    