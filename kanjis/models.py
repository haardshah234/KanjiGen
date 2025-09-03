from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Kanji(models.Model):
    character = models.CharField(max_length=1,null=False,unique=True)
    pron1 = models.CharField(null=False)
    mean1 = models.CharField(null=False)
    pron2 = models.CharField(null=True)
    mean2 = models.CharField(null=True)
    jlpt = models.IntegerField(null=False,validators=[MinValueValidator(1),MaxValueValidator(5)])
    rkmath = models.CharField(max_length=2,null=True)
    jaltap = models.IntegerField(null=True,validators=[MinValueValidator(1),MaxValueValidator(34)])
    somatome = models.IntegerField()

    def __str__(self):
        if self.pron2 and self.mean2:
            return f"{self.id}: {self.character}, {self.pron1}({self.mean1}) or {self.pron2}({self.mean2}), N{self.jlpt}, RK-{self.rkmath}, Ch-{self.jaltap}, Somatome-{self.somatome}"
        else:
            return f"{self.id}: {self.character}, {self.pron1}({self.mean1}), N{self.jlpt}, RK-{self.rkmath}, Ch-{self.jaltap}, Somatome-{self.somatome}"