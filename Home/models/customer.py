from django.db import models


class Customer(models.Model):
    Hospital_Name = models.CharField(max_length=500, default=None, null=True)
    Hospital_Location = models.CharField(max_length=500, default=None, null=True)
    Hospital_City = models.CharField(max_length=500, default=None, null=True)
    Hospital_Id = models.CharField(max_length=500, default=None, null=True)
    Hospital_Number = models.CharField(max_length=500, default=None, null=True)
    Hospital_Email = models.CharField(max_length=500, default=None, null=True)
    Hospital_Password = models.CharField(max_length=500, default=None, null=True)
    UserType = models.CharField(max_length=500, default=None, null=True)

    @staticmethod
    def get_by_hospitalName(Hospital_Name):
        try:
            return Customer.objects.get(Hospital_Name = Hospital_Name)
        except:
            return False

    def __str__(self):
        return self.Hospital_Name

