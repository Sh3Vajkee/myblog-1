from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'id']
    ordering = ['pub_date']
    list_filter = ['pub_date']
    inlines = [CommentInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
