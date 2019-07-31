from django.core.mail import send_mail
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Post
from .forms import PostForm, FeedForm


from django.views.generic import FormView, CreateView
from django.views import generic


class PostView(generic.ListView):
    template_name = 'blog/post_list.html'
    # context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostView, self).get_context_data(object_list=object_list, **kwargs)
        context["tst"] = 77778
        return context



# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now())
#     return render(request, 'blog/post_list.html', {'posts': posts})

class post_detail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

class PostNew(generic.CreateView):
    model = Post
    template_name = 'blog/post_edit.html'
    form_class = PostForm
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        return super(PostNew, self).form_valid(form)


# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})
class post_edit(generic.UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    form_class = PostForm
    def get_success_url(self):
         return reverse_lazy("post_detail", kwargs={"pk": self.kwargs["pk"]})
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.object = self.get_object()

    # def form_valid(self, form):
    #     self.object = form.save()
    #     data = {
    #         'form_is_valid': True,
    #         'id': form.instance.id,
    #         'title': form.instance.title,
    #         'text': form.instance.text
    #     }
    #
    #     return JsonResponse(data)
    #
    # def form_invalid(self, form):
    #     ct = self.get_context_data(form=form)
    #     form_html = render_to_string('blog/post_edit.html', context=ct, request=self.request)
    #     return JsonResponse({'html_form': form_html})

    # def get(self, request, *args, **kwargs):
    #     ct = self.get_context_data()
    #     form_html = render_to_string('blog/post_edit.html', context=ct, request=request)
    #     return JsonResponse({'html_form': form_html})


#
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})

class FeedbackNew(FormView):
    template_name = 'blog/feed_edit.html'
    form_class = FeedForm
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        send_mail(
            'Feedback',
            form.cleaned_data["feedback"],
            form.cleaned_data["email"],
            [form.cleaned_data["email"]],
            fail_silently=False,
        )
        # print(form.errors)
        return super(FeedbackNew, self).form_valid(form)

# def feedback_new(request):
#     if request.method == "POST":
#         form = FeedForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             messages.info(request, 'Your Feedback has been changed successfully!')
#             return redirect('post_list')
#
#     else:
#         form = FeedForm()
#     return render(request, 'blog/feed_edit.html', {'form': form})
