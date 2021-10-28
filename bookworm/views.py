from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 9
    

class DetailView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True, parent__isnull=True).order_by("created_on")
        replies = post.comments.filter(approved=True, parent__isnull=False).order_by("created_on")
        score = post.score

        return render(
            request,
            "detail_view.html",
            {
                "post": post,
                "comments": comments,
                "replies": replies,
                "commented": False,
                "comment_form": CommentForm(),
                "score": score,
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True, parent__isnull=True).order_by("created_on")
        replies = post.comments.filter(approved=True, parent__isnull=False).order_by("created_on")

        initial_data = { 
            "object_id": post.id
        }
        comment_form = CommentForm(request.POST or None, initial=initial_data)
        if comment_form.is_valid():
            obj_id = comment_form.cleaned_data.get('object_id')
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            parent_obj = None
            try:
                parent_id = int(request.POST.get("parent_id"))
            except:
                parent_id = None

            if parent_id:
                parent_qs = Comment.objects.filter(parent__id=parent_id)
                if parent_qs.exists() and parent__qs.count() == 1:
                    parent_obj = parent_qs.first()
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "detail_view.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "parent": parent_obj,
                "id": obj_id,
            },
        )