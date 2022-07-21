from django.shortcuts import render


posts = [
    {
        'author': 'Anna',
        'title': 'Blog Post 1',
        'content': 'My first post',
        'date_posted': 'July 21, 2022'
    },
    {
        'author': 'Elon Musk',
        'title': 'Blog Post 2',
        'content': 'Second post',
        'date_posted': 'July 18, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
