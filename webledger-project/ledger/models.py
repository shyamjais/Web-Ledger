from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Dealer(models.Model):
    name = models.CharField(unique=True, max_length=200)
    mob_num = models.IntegerField(unique=True, blank=True, null=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Collected_by(models.Model):
    name = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "Money Collected By"

    def __str__(self):
        return self.name


class Ledger(models.Model):
    date = models.DateTimeField("Date",auto_now_add=True)
    particulars = models.CharField("Particulars",max_length=100,blank=True)
    debit = models.PositiveIntegerField("Debit",blank=True, default=0)
    credit = models.PositiveIntegerField("Credit",blank=True, default=0)
    paymode = models.CharField("Payment Mode",max_length=10, choices=(('Cash','Cash'),
                                                       ('Cheque','Cheque'),))
    dr_cr = models.CharField("Dr/Cr",max_length=10, default='', choices=(('Dr','Dr'),
                                                                 ('Cr','Cr'),))
    invoice = models.ImageField("Invoice",upload_to=None, blank=True)
    dealer = models.ForeignKey(Dealer,verbose_name="Dealer", null=True, on_delete=models.SET_NULL)
    balance = models.PositiveIntegerField(default=0)
    collect_by = models.ForeignKey(Collected_by,verbose_name="Collected By", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.dealer.name, self.date)



class ViewDealer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    dealer = models.ManyToManyField(Dealer, related_name="dealer")

    class Meta:
        verbose_name_plural = "Dealer Permission Area"

class RoadExpense(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fooding = models.PositiveIntegerField(blank=True, default=0)
    fuel = models.PositiveIntegerField(blank=True, default=0)
    misc = models.TextField()
