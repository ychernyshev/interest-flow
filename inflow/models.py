from django.db import models


class DepositItemModel(models.Model):
    deposit_name = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=30)
    savings = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.deposit_name}, {self.bank_name}: {self.savings}'

    class Meta:
        verbose_name = 'add a deposit'
        verbose_name_plural = 'Deposits'