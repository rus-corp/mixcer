from django.db import models



from app.users.models import CustomUser

    
class Tarif(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название тарифа')
    desc = models.TextField(max_length=900, verbose_name='Описание тарифа')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, verbose_name='базовая стоиость * на коэф контента')
    shot_count = models.IntegerField(verbose_name='Количество кадров (шт)')
    discount = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    
    content = models.ForeignKey(to='content.Content', on_delete=models.CASCADE, related_name='tarifs')
    
    user = models.ManyToManyField(CustomUser, through='UserTarif')

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'
    
    def __str__(self) -> str:
        return self.name
    
    def get_content(self):
        return self.content.name
     
    def get_total_price(self):
        return int(self.price * self.shot_count * self.discount)
    
    get_total_price.short_description = ('Стоимость тарифа')
    get_content.short_description = ('Тип Контента')
    
    
    
class UserTarif(models.Model):
    tarif = models.ForeignKey(Tarif, on_delete=models.PROTECT, related_name='user_tarifs')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_tarifs')
    shot_remains = models.IntegerField(verbose_name='Остаток кадров')
    
    class Meta:
        verbose_name = 'Тариф пользователя'
        verbose_name_plural = 'Тарифы Пользователей'
        
        
    def get_shot_remains(self):
        self.shot_remains = self.tarif.shot_count
        
    def __str__(self) -> str:
        return f'{self.user.email} - {self.tarif.name}'