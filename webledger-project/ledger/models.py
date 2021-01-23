from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete

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
    new_balance = models.IntegerField(editable=False)
    dr_cr = models.CharField("Dr/Cr",max_length=2,default='nil',editable=False)
    invoice = models.ImageField("Invoice",upload_to=None, blank=True)
    dealer = models.ForeignKey(Dealer,verbose_name="Dealer", null=True, on_delete=models.SET_NULL)
    balance = models.IntegerField(editable=False,default=0)
    dealer_ledger_number = models.IntegerField(editable=False,default=0)
    @property
    def cur_bal_calculator(self):
        prev = BrandNew.objects.get(dealer = self.dealer)
        return prev.balance + self.debit-self.credit

    @property
    def assign_dealer_ledger_number(self):
        prev = BrandNew.objects.get(dealer = self.dealer)
        return prev.ledger_number + 1

    @property
    def assign_dr_cr(self):
        if(self.new_balance<0):
            return "Cr"
        else:
            return "Dr"

    @property
    def assign_positive_balance(self):
        return abs(self.new_balance)

    collect_by = models.ForeignKey(Collected_by,verbose_name="Collected By", blank=True, null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
          self.new_balance = self.cur_bal_calculator
          self.dealer_ledger_number = self.assign_dealer_ledger_number
          self.balance = self.assign_positive_balance
          self.dr_cr = self.assign_dr_cr
          super(Ledger, self).save(*args, **kwargs)



    class Meta:
        db_table= "led"

class ViewDealer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    dealer = models.ManyToManyField(Dealer, related_name="dealer")

    class Meta:
        verbose_name_plural = "Dealer Permission Area"

class RoadExpense(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    fooding = models.PositiveIntegerField(blank=True, default=0)
    fuel = models.PositiveIntegerField(blank=True, default=0)
    misc = models.TextField(blank=True)



class BrandNew(models.Model):
    dealer = models.ForeignKey(Dealer,on_delete=models.CASCADE)
    #dr_cr = models.CharField("Dr/Cr",max_length=10, default='', choices=(('Dr','Dr'),('Cr','Cr'),))

    balance = models.IntegerField(default=0)
    ledger_number = models.IntegerField(default=0)

def bal_one(sender, instance, **kwargs):
    if kwargs['created']:
        a = BrandNew(dealer = instance,balance = 0,ledger_number=0)
        a.save()


def update_bal_one(sender,instance,**kwargs):
    if kwargs['created']:

        a = BrandNew.objects.get(dealer = instance.dealer)

        a.delete()
        m = BrandNew(dealer = instance.dealer,balance = instance.new_balance,ledger_number = instance.dealer_ledger_number)
        m.save()
    if  not kwargs['created']:
        m = BrandNew.objects.get(dealer = instance.dealer)
        latest_ledger_number = instance.dealer_ledger_number
        cur_ledger_number = latest_ledger_number -1
        while(cur_ledger_number!=1):
            try:
                obj = Ledger.objects.get(dealer_ledger_number = cur_ledger_number)
            except:

                break
            cur_ledger_number-=1

        if cur_ledger_number == 1:
            prev = 0
        else:
            prev = Ledger.objects.get(dealer_ledger_number = cur_ledger_number-1)
            prev = prev.new_balance
        i = cur_ledger_number
        debit = instance.debit
        credit = instance.credit
        new_balance = prev + debit - credit
        BN = BrandNew.objects.get(dealer = instance.dealer)
        BN.delete()
        BN.ledger_number = i-1
        BN.dealer = instance.dealer
        BN.balance = prev
        BN.save()
        led = Ledger(dealer = instance.dealer,debit = instance.debit,credit = instance.credit)
        led.save()
        BN = BrandNew.objects.get(dealer = instance.dealer)
        BN.delete()
        BN.dealer = instance.dealer
        BN.balance = new_balance
        BN.ledger_number = i
        BN.save()
        i = i+1

        prev = new_balance
        while(i!=latest_ledger_number):
            
            old = Ledger.objects.get(dealer_ledger_number = i)
            #new = Ledger(dealer_ledger_number=i,debit=old.debit,credit=old.credit,collect_by=old.collect_by,dealer=instance.dealer,paymode=old.pay)
            old.delete()
            b = BrandNew.objects.get(dealer = instance.dealer)
            b.delete()
            b.dealer = instance.dealer
            b.ledger_number = i-1
            b.balance = prev
            b.save()
            old.paymode = 'Cheque'
            old.dealer_ledger_number = i
            old.save()
            prev = old.new_balance
            i = i+1
        Ledger.objects.get(dealer_ledger_number = latest_ledger_number).delete()





post_save.connect(bal_one,sender = Dealer)
post_save.connect(update_bal_one,sender = Ledger)
