from django.db import models


ORDER_STATUSES = (
    (0, 'BASKET'),
    (1, 'CHECKOUT'),
    (2, 'DONE')
)

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=255)
    child = models.ManyToManyField(
        'self',
        blank=True
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True
    )
    is_parent = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Brand(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class ProductType(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Product type'
        verbose_name_plural = 'Product types'


class Size(BaseModel):
    product_type = models.ForeignKey(
        ProductType,
        related_name='sizes',
        on_delete=models.PROTECT,
        null=True
    )
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'


class Color(BaseModel):
    product_type = models.ForeignKey(
        ProductType,
        related_name='colors',
        on_delete=models.PROTECT,
        null=True
    )
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'
    

class Product(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products'
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='products',
        null=True
    )
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.PROTECT,
        related_name='products'
    )
    image = models.ImageField(
        upload_to='products',
        null=True
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductItem(BaseModel):
    user = models.ForeignKey(
        'account.Account',
        related_name='order_items',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.PROTECT,
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.PROTECT,
    )
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(
        'order.Order', 
        on_delete=models.SET_NULL,
        related_name='items',
        null=True,
        blank=True,
    )
    status = models.IntegerField(
        choices=ORDER_STATUSES,
        default=0
    )

    def __str__(self) -> str:
        return self.product.name
    
    @property
    def get_total_price(self):
        return self.quantity * self.product.price
    
    class Meta:
        verbose_name = 'Product item'
        verbose_name_plural = 'Product items'
        default_related_name = 'product_items'
