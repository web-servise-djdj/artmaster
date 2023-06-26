from django.db import models

# Create your models here.

class Frame(models.Model):
    Wood = "Деревянный"
    Plastic = "Пластиковый"
    Alumin = "Алюминий"

    CHOICE_GROUP = {
        (Wood , "Деревянный"),
        (Plastic ,"Пластиковый"),
        (Alumin ,"Алюминий")
    }

    articul = models.CharField(max_length=30 )
    width = models.CharField(max_length=10, )
    idarticul = models.CharField(max_length=10)
    type = models.CharField(max_length=20, choices=CHOICE_GROUP, default=Wood)
    confirm =  models.BooleanField()
    img = models.ImageField(default='no_image.jpg')

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        verbose_name = "Багет"
        verbose_name_plural = "Багеты" 