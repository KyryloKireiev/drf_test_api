# Generated by Django 4.1.3 on 2022-11-29 09:36

from django.db import migrations


def create_categories(apps, scheme_migrations):
    Caterogy = apps.get_model("articles", "Category")
    categories = []
    names = ("Boats", "Fish", "Houses")

    for name in names:
        categories.append(Caterogy(name=name))

    Caterogy.objects.bulk_create(categories)


def delete_categories(apps, scheme_migrations):
    Caterogy = apps.get_model("articles", "Category")
    Caterogy.objects.delete()


def create_articles(apps, scheme_migrations):
    Article = apps.get_model("articles", "Article")
    articles = []

    for number in range(10, 20):
        articles.append(Article(title=f"New article {number} article",
                                content=f"New content {number}",
                                cat_id=1,
                                user_id=1))

    Article.objects.bulk_create(articles)


def delete_articles(apps, scheme_migrations):
    Article = apps.get_model("articles", "Article")
    Article.objects.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_create_users'),
    ]

    operations = [
        migrations.RunPython(create_categories, delete_categories),
        migrations.RunPython(create_articles, delete_articles),
    ]
