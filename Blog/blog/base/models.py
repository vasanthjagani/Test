from django.db import models
from django.utils.translation import gettext as _


class Post(models.Model):
    """
    Model to maintain the posts
    """
    title = models.CharField(blank=False, max_length=254, verbose_name=_("Title"), null=False)
    description = models.CharField(blank=False, max_length=800, verbose_name=_("Description"), null=False)
    publish_date = models.DateField(verbose_name=_("Date"), null=True, blank=True)
    author = models.CharField(blank=True, max_length=254, verbose_name=_("Author"), null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Model to maintain comments
    """
    post = models.ForeignKey(Post, verbose_name=_("Post"), on_delete=models.CASCADE, null=True, blank=False)
    text = models.CharField(blank=False, max_length=800, verbose_name=_("Comment"), null=False)
    author = models.CharField(blank=True, max_length=254, verbose_name=_("Author"), null=True)

    def __str__(self):
        return self.text


class Like(models.Model):
    """
    Model to maintain Likes
    """
    post = models.ForeignKey(Post, verbose_name=_("Post"), on_delete=models.CASCADE, null=True, blank=False)
    # text = models.CharField(blank=False, max_length=800, verbose_name=_("Comment"), null=False)
    author = models.CharField(blank=True, max_length=254, verbose_name=_("Author"), null=True)

    def __str__(self):
        return self.post.title if self.post else ''