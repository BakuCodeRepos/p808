from django.db import models


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Haqqımızda'
        verbose_name_plural = 'Haqqımızda'


class AboutPoint(models.Model):
    about = models.ForeignKey(
        'about.About',
        on_delete=models.CASCADE,
        related_name='points'
    )
    text = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = 'Haqqımızda punktu'
        verbose_name_plural = 'Haqqımızda punktları'
