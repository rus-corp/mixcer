from django.db import models
from decimal import Decimal
from app.users.models import CustomUser
from app.content.models import Content




class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='')
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='orders', verbose_name='')
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        
    def __str__(self) -> str:
        return f'{self.pk} - {self.user.email}'
        
        
        
    
class OrderContent(models.Model):
    FILE_TYPE_CHOICES = (
        ('JPG', 'JPG'),
        ('WEBP', 'WEBP'),
        ('PNG', 'PNG'),
        ('GIF', 'GIF')
    )
    SCREEN_RESOLUTION_CHOICES = (
        ('400x300', '400x300'),
        ('600x450', '600x450'),
        ('800x600', '800x600'),
        ('1200x900', '1200x900'),
        ('1600x1200', '1600x1200'),
    )
    FON_CHOICES = (
        ('WHITE', 'WHITE'),
        ('BLACK', 'BLACK'),
        ('TRANSPARENT', 'TRANSPARENT')
    )    
    SCENARIO_CHOICES = (
        ('VERTICAL', 'VERTICAL'),
        ('HORIZONTAL', 'HORIZONTAL'),
        ('SPIRAL', 'SPIRAL')
    )
    TABLE_ROTATION_CHOICES = (
        ('360', '360'),
        ('720', '720')
    )
    SHOT_COUNT_CHOICES = (
        ('4', '4'),
        ('8', '8'),
        ('12', '12'),
        ('16', '16'),
        ('18', '18'),
        ('24', '24'),
        ('36', '36'),
    )
    fyle_type = models.CharField(max_length=4, choices=FILE_TYPE_CHOICES, verbose_name='тип файла', null=True, blank=True, default='JPG')
    screen_resolution = models.CharField(max_length=9, choices=SCREEN_RESOLUTION_CHOICES, verbose_name='разрешение экрана', blank=True, null=True, default='800x600')
    fon = models.CharField(max_length=11, choices=FON_CHOICES, verbose_name='фон', null=True, blank=True, default='TRANSPARENT')
    scenario = models.CharField(max_length=10, choices=SCENARIO_CHOICES, verbose_name='сценарий съемки', blank=True, null=True, default='HORIZONTAL')
    table_rotation = models.CharField(max_length=3, choices=TABLE_ROTATION_CHOICES ,verbose_name='поворот стола', blank=True, null=True, default='360')    
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='стоимость заказа', blank=True)
    shot_count = models.CharField(max_length=2, choices=SHOT_COUNT_CHOICES, verbose_name='кол-во кадров', blank=True, null=True, default='8')

    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='заказ', related_name='ordercontent')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name='контент', related_name='ordercontent')
    
    
    class Meta:
        verbose_name = 'Контент заказа'
        verbose_name_plural = 'Контенты заказов'
    
    def save(self, *args, **kwargs):
        self.price = self.content.price.value * Decimal(self.shot_count)
        super(OrderContent, self).save(**kwargs)

    def __str__(self) -> str:
        return f'{self.order.pk} - {self.content.name}'
    
    

    

    
    
    
# class SpecialContentParam(models.Model):
#     SCENARIO_CHOICES = (
#         ('VERTICAL', 'VERTICAL'),
#         ('HORIZONTAL', 'HORIZONTAL'),
#         ('SPIRAL', 'SPIRAL')
#     )
#     TABLE_ROTATION_CHOICES = (
#         ('360', '360'),
#         ('720', '720')
#     )
#     scenario = models.CharField(max_length=10, choices=SCENARIO_CHOICES, verbose_name='сценарий съемки', blank=True, null=True, default='HORIZONTAL')
#     table_rotation = models.CharField(max_length=3, choices=TABLE_ROTATION_CHOICES ,verbose_name='поворот стола', blank=True, null=True, default='360')
#     ordercontent = models.ForeignKey(OrderContent, on_delete=models.PROTECT, related_name='special_params')
    
#     class Meta:
#         verbose_name = 'Спец параметр'
#         verbose_name_plural = 'Спец параметры'
        
#     def __str__(self) -> str:
#         return self.id