from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse, Http404
from django.template.context_processors import csrf
from django.template.loader import get_template

from .forms import CommentForm
from django.urls import reverse

from .models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.core.paginator import Paginator


# Create your views here.
def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is %s view</body></html>" % view
    return HttpResponse(html)


def template_two(request):
    view = "template_two"
    template = get_template('myview.html')
    html = template.render({"name": view})
    return HttpResponse(html)


def template_three_simple(request):
    view = "template_three"
    return render_to_response('myview.html', {"name": view})


def articles(request, page_number=1):
    all_articles = Article.objects.all().order_by("-date")
    current_page = Paginator(all_articles, 2)
    return render_to_response('articles.html',
                              {"articles": current_page.page(page_number),
                               "username": auth.get_user(request).username})


def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)


def add_like(request, article_id):
    response = redirect(reverse('article_app:articles'))
    if article_id in request.COOKIES:
        return response
    try:
        article = Article.objects.get(id=article_id)
        article.likes += 1
        article.save()
        response = redirect(reverse('article_app:articles'))
        response.set_cookie(article_id, "test")
    except ObjectDoesNotExist:
        raise Http404
    return response


def add_comment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            try:
                comment.article = Article.objects.get(id=article_id)
            except ObjectDoesNotExist:
                raise Http404
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect(reverse('article_app:article', args=[article_id]))

