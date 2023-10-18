from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


from app.tarifs.models import Tarif


class BasePrice(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Базовая стоимость')
    
    
    class Meta:
        verbose_name = 'Базовая стоимость'
        verbose_name_plural = 'Базовые стоимости'
    
        
    def __str__(self) -> str:
        return f'{self.value}' or ''
    
    
    def update_tarifs(self):
        tarifs = Tarif.objects.filter(content__price=self)
        for tarif in tarifs:
            tarif.price = self.value * tarif.content.coef
            tarif.save()
    
    
    def save(self, *args, **kwargs):
        old_base_price = BasePrice.objects.filter(id=self.id).first()
        if old_base_price and old_base_price.value != self.value:
            self.update_tarifs()
        return super().save(*args, **kwargs)
    
    
@receiver(post_save, sender=BasePrice)
def change_tarif_price(sender, instance, **kwargs):
    tariffs = Tarif.objects.filter(content__price=instance)
    for tariff in tariffs:
        tariff.price = instance.value * tariff.content.coef
        tariff.save()


class Content(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название контента')
    coef = models.DecimalField(max_digits=5, decimal_places=2, default=1, verbose_name='Коэф контента')
    price = models.ForeignKey(BasePrice, on_delete=models.CASCADE, related_name='contents', verbose_name='цена контента')
    
    class Meta:
        verbose_name = 'Тип Контента'
        verbose_name_plural = 'Типы Контента'
        
    def __str__(self) -> str:
        return self.name