from django.db import models


class User(models.Model):
    cpf = models.CharField(primary_key=True, null=False, blank=False, serialize=True, max_length=11,
                           help_text='Primary key.')
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    fullname = models.CharField(max_length=50, null=False, blank=False)
    birthday = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'users'


class Adress(models.Model):
    cep = models.CharField(max_length=8, null=False, blank=False)  # zip code
    street = models.CharField(max_length=50, null=False, blank=False)
    house_number = models.CharField(max_length=6, null=False, blank=False)
    state = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=20, null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, help_text='Primary key.')

    def __str__(self):
        return self.cep

    class Meta:
        db_table = 'adress'


class GenericModelForSwaggerFilds(models.Model):
    """Generic class to construct custom body schemas for swagger documentation."""
    user_id = models.CharField(max_length=255,
                               help_text='This has to be the primarykey (ex.: username) you difined in your table!')
    field = models.CharField(max_length=255, help_text='The field you want to retrive of your table.')

    class Meta:
        managed = False
