from django.db import models


class Order(models.Model):
    subtotal = models.DecimalField(max_digits=16, decimal_places=2)
    total = models.DecimalField(max_digits=16, decimal_places=2)
    shipping = models.DecimalField(max_digits=16, decimal_places=2)
    user = models.ForeignKey(
        'account.Account',
        related_name='orders',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.user.email} - {self.total}"


class WishList(models.Model):
    user = models.ForeignKey(
        'account.Account',
        related_name='wish_list',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product = models.ManyToManyField(
        'product.Product',
        related_name='wish_list'
    )

    class Meta:
        verbose_name = 'Wish list'
        verbose_name_plural = 'Wish list'

    def __str__(self):
        return f"{self.user.email}"
