from django.shortcuts import render, redirect
from .models import Article, ArticleSeries
from django.contrib import messages
from .decorators import user_is_superuser
from .forms import SeriesCreateForm, ArticleCreateForm, SeriesUpdateForm, ArticleUpdateForm
from django.core.paginator import Paginator

# Create your views here.
def homepage(request):
    matching_series = ArticleSeries.objects.all()
    
    return render(
        request=request,
        template_name='main/home.html',
        context={
            "objects": matching_series,
            "type": "series"
            }
        )

def series(request, series: str):
    matching_series = Article.objects.filter(series__slug=series).all()
    
    return render(
        request=request,
        template_name='main/home.html',
        context={
            "objects": matching_series,
            "type": "article"
            }
        )

def article(request, series: str, article: str):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()
    
    return render(
        request=request,
        template_name='main/article.html',
        context={"object": matching_article}
        )


def master_article(request):
    matching_article = Article.objects.all()
    
    paginator   = Paginator(matching_article, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)
    
    return render(
        request=request,
        template_name='main/master_article.html',
        context={
            "objects"       : matching_article,
            "type"          : "article",
            'side_active'   : 'article',
            'page_obj'   : page_obj,
            }
        )



def master_series(request):
    matching_series = ArticleSeries.objects.all()
    
    paginator   = Paginator(matching_series, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)
    
    return render(
        request=request,
        template_name='main/master_series.html',
        context={
            "objects": matching_series,
            "type": "series",
            'side_active'   : 'series',
            'page_obj'   : page_obj,
            }
        )


@user_is_superuser
def new_series(request):

    matching_series = ArticleSeries.objects.all()

    if request.method == "POST":
        form = SeriesCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Di Ubah")
            return redirect("artic:series-create")
        else:
            messages.error(request, "Data Gagal Di Ubah")
            form = SeriesCreateForm()

    else:
        form = SeriesCreateForm()

    return render(
        request=request,
        template_name='main/new_series.html',
        context={
            "object": "Series",
            'side_active'   : 'series',
            "allobjects": matching_series,
            "form": form
            }
        )

@user_is_superuser
def new_post(request):
    if request.method == "POST":
        form = ArticleCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, "Data Berhasil Di Ubah")
            return redirect("artic:master_article")
            # return redirect(f"{form.cleaned_data['series'].slug}/{form.cleaned_data.get('article_slug')}")
        else:
            messages.error(request, "Data Gagal Di Ubah")

    else:
         form = ArticleCreateForm()

    return render(
        request=request,
        template_name='main/new_article.html',
        context={
            "object": "Article",
            "side_active": "article",
            "form": form
            }
        )

@user_is_superuser
def series_update(request, series):
    matching_series = ArticleSeries.objects.filter(slug=series).first()
    all_series = ArticleSeries.objects.all()

    if request.method == "POST":
        form = SeriesUpdateForm(request.POST, request.FILES, instance=matching_series)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Di Ubah")
            return redirect('artic:series-create')
        else:
            messages.error(request, "Data Gagal Di Ubah")
            form = SeriesUpdateForm(instance=matching_series)
    
    else:
        form = SeriesUpdateForm(instance=matching_series)

    return render(
        request=request,
        template_name='main/new_series.html',
        context={
            "object": "Series",
            'side_active'   : 'series',
            "allobjects": all_series,
            "form": form
            }
        )

@user_is_superuser
def series_delete(request, series):
    matching_series = ArticleSeries.objects.filter(slug=series).first()
    matching_series.delete()
    return redirect('artic:series-create')
    
    # return redirect('artic:series-create')
        # return render(
            # request=request,
            # template_name='main/new_series.html',
            # context={
            #     "object": matching_series,
            #     "type": "Series"
            #     }
            # )

@user_is_superuser
def article_update(request, series, article):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()

    if request.method == "POST":
        form = ArticleUpdateForm(request.POST, request.FILES, instance=matching_article)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Di Ubah")
            return redirect("artic:master_article")
            # return redirect(f'/{matching_article.slug}')
        else:
            messages.error(request, "Data Gagal Di Ubah")
    
    else:
        form = ArticleUpdateForm(instance=matching_article)

        return render(
            request=request,
            template_name='main/new_article.html',
            context={
                "object": "Article",
                "side_active": "article",
                "form": form
                }
            )

@user_is_superuser
def article_delete(request, series, article):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()

    matching_article.delete()

    return redirect("artic:master_article")
    # if request.method == "POST":
    #     matching_article.delete()
    #     return redirect('/')
    # else:
    #     return render(
    #         request=request,
    #         template_name='main/confirm_delete.html',
    #         context={
    #             "object": matching_article,
    #             "type": "article"
    #             }
    #         )