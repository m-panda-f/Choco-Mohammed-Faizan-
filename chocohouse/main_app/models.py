from django.db import models

# Seasonal flavor model
class Flvr(models.Model):
    flvr_name = models.CharField(max_length=100)  # Flavor name
    szn = models.CharField(max_length=50)  # Season

    def __str__(self):
        return f"{self.flvr_name} ({self.szn})"

# Ingredient inventory model
class Ingr(models.Model):
    ingr_name = models.CharField(max_length=100)  # Ingredient name
    qty = models.IntegerField()  # Quantity

    def __str__(self):
        return f"{self.ingr_name} - {self.qty}"

# Customer feedback model
class Fdbk(models.Model):
    cust_name = models.CharField(max_length=100, blank=True, null=True)  # Customer name
    flvr_sugg = models.CharField(max_length=255)  # Flavor suggestion
    alrgy_warn = models.TextField(blank=True, null=True)  # Allergy concern

    def __str__(self):
        return f"Feedback by {self.cust_name or 'Anon'}"
