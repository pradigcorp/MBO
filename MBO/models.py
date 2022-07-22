from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class GOAL22(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    GOAL22A1 = models.TextField(blank=True)
    GOAL22B1 = models.TextField(blank=True)
    GOAL22C1 = models.TextField(blank=True)
    GOAL22D1 = models.TextField(blank=True)
    GOAL22E1 = models.TextField(blank=True)
    GOAL22F1 = models.TextField(blank=True)
    GOAL22G1 = models.TextField(blank=True)

    GOAL22AP = models.IntegerField(default=0)
    GOAL22BP = models.IntegerField(default=0)
    GOAL22CP = models.IntegerField(default=0)
    GOAL22DP = models.IntegerField(default=0)
    GOAL22EP = models.IntegerField(default=0)
    GOAL22FP = models.IntegerField(default=0)
    GOAL22GP = models.IntegerField(default=0)

    GOAL22A2 = models.TextField(blank=True)
    GOAL22B2 = models.TextField(blank=True)
    GOAL22C2 = models.TextField(blank=True)
    GOAL22D2 = models.TextField(blank=True)
    GOAL22E2 = models.TextField(blank=True)
    GOAL22F2 = models.TextField(blank=True)
    GOAL22G2 = models.TextField(blank=True)

    GOAL22A3 = models.TextField(blank=True)
    GOAL22B3 = models.TextField(blank=True)
    GOAL22C3 = models.TextField(blank=True)
    GOAL22D3 = models.TextField(blank=True)
    GOAL22E3 = models.TextField(blank=True)
    GOAL22F3 = models.TextField(blank=True)
    GOAL22G3 = models.TextField(blank=True)

    GOAL22AR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL22BR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL22CR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL22DR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL22ER = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL22FR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL22GR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

    GOAL22Q1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    GOAL22Q2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    GOAL22Q3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)

    GOAL22Q1A = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    GOAL22Q2A = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    GOAL22Q3A = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)

    GOAL22Q1Y = models.IntegerField(default=0)
    GOAL22Q2Y = models.IntegerField(default=0)
    GOAL22Q3Y = models.IntegerField(default=0)

    GOAL22Q1M = models.IntegerField(default=0)
    GOAL22Q2M = models.IntegerField(default=0)
    GOAL22Q3M = models.IntegerField(default=0)

    GOAL22Q1D = models.IntegerField(default=0)
    GOAL22Q2D = models.IntegerField(default=0)
    GOAL22Q3D = models.IntegerField(default=0)

    GOAL23A1 = models.TextField(blank=True)
    GOAL23B1 = models.TextField(blank=True)
    GOAL23C1 = models.TextField(blank=True)
    GOAL23D1 = models.TextField(blank=True)
    GOAL23E1 = models.TextField(blank=True)
    GOAL23F1 = models.TextField(blank=True)
    GOAL23G1 = models.TextField(blank=True)

    GOAL23AP = models.IntegerField(default=0)
    GOAL23BP = models.IntegerField(default=0)
    GOAL23CP = models.IntegerField(default=0)
    GOAL23DP = models.IntegerField(default=0)
    GOAL23EP = models.IntegerField(default=0)
    GOAL23FP = models.IntegerField(default=0)
    GOAL23GP = models.IntegerField(default=0)

    GOAL23A2 = models.TextField(blank=True)
    GOAL23B2 = models.TextField(blank=True)
    GOAL23C2 = models.TextField(blank=True)
    GOAL23D2 = models.TextField(blank=True)
    GOAL23E2 = models.TextField(blank=True)
    GOAL23F2 = models.TextField(blank=True)
    GOAL23G2 = models.TextField(blank=True)

    GOAL23A3 = models.TextField(blank=True)
    GOAL23B3 = models.TextField(blank=True)
    GOAL23C3 = models.TextField(blank=True)
    GOAL23D3 = models.TextField(blank=True)
    GOAL23E3 = models.TextField(blank=True)
    GOAL23F3 = models.TextField(blank=True)
    GOAL23G3 = models.TextField(blank=True)

    GOAL23AR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL23BR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL23CR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL23DR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL23ER = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL23FR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL23GR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

    GOAL23Q1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    GOAL23Q2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    GOAL23Q3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)

    GOAL23Q1A = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    GOAL23Q2A = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    GOAL23Q3A = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)

    GOAL23Q1Y = models.IntegerField(default=0)
    GOAL23Q2Y = models.IntegerField(default=0)
    GOAL23Q3Y = models.IntegerField(default=0)

    GOAL23Q1M = models.IntegerField(default=0)
    GOAL23Q2M = models.IntegerField(default=0)
    GOAL23Q3M = models.IntegerField(default=0)

    GOAL23Q1D = models.IntegerField(default=0)
    GOAL23Q2D = models.IntegerField(default=0)
    GOAL23Q3D = models.IntegerField(default=0)





    GOAL24A1 = models.TextField(blank=True)
    GOAL24B1 = models.TextField(blank=True)
    GOAL24C1 = models.TextField(blank=True)
    GOAL24D1 = models.TextField(blank=True)
    GOAL24E1 = models.TextField(blank=True)
    GOAL24F1 = models.TextField(blank=True)
    GOAL24G1 = models.TextField(blank=True)

    GOAL24AP = models.IntegerField(default=0)
    GOAL24BP = models.IntegerField(default=0)
    GOAL24CP = models.IntegerField(default=0)
    GOAL24DP = models.IntegerField(default=0)
    GOAL24EP = models.IntegerField(default=0)
    GOAL24FP = models.IntegerField(default=0)
    GOAL24GP = models.IntegerField(default=0)

    GOAL24A2 = models.TextField(blank=True)
    GOAL24B2 = models.TextField(blank=True)
    GOAL24C2 = models.TextField(blank=True)
    GOAL24D2 = models.TextField(blank=True)
    GOAL24E2 = models.TextField(blank=True)
    GOAL24F2 = models.TextField(blank=True)
    GOAL24G2 = models.TextField(blank=True)

    GOAL24A3 = models.TextField(blank=True)
    GOAL24B3 = models.TextField(blank=True)
    GOAL24C3 = models.TextField(blank=True)
    GOAL24D3 = models.TextField(blank=True)
    GOAL24E3 = models.TextField(blank=True)
    GOAL24F3 = models.TextField(blank=True)
    GOAL24G3 = models.TextField(blank=True)

    GOAL24AR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL24BR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL24CR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL24DR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL24ER = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL24FR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    GOAL24GR = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

    GOAL24Q1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    GOAL24Q2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    GOAL24Q3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)

    GOAL24Q1A = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    GOAL24Q2A = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    GOAL24Q3A = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)

    GOAL24Q1Y = models.IntegerField(default=0)
    GOAL24Q2Y = models.IntegerField(default=0)
    GOAL24Q3Y = models.IntegerField(default=0)

    GOAL24Q1M = models.IntegerField(default=0)
    GOAL24Q2M = models.IntegerField(default=0)
    GOAL24Q3M = models.IntegerField(default=0)

    GOAL24Q1D = models.IntegerField(default=0)
    GOAL24Q2D = models.IntegerField(default=0)
    GOAL24Q3D = models.IntegerField(default=0)



    def __str__(self):
        return self.user.username


# Create your models here.
