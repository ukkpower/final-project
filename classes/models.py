from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
      
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class GymClass(models.Model):

    class Meta:
        verbose_name_plural = 'GymClasses'

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    level = models.CharField(max_length=254)
    duration = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    period = models.CharField(max_length=254)
    students = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    trainer = models.ManyToManyField('Trainer')

    def __str__(self):
        return self.name


class Trainer(models.Model):

    name = models.CharField(max_length=254)
    bio = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Timetable(models.Model):

    gym_class = models.ForeignKey('GymClass', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    date = models.CharField(max_length=12)
    time_slot = models.CharField(max_length=12)
    trainer = models.ForeignKey('Trainer', on_delete=models.CASCADE)

    def __str__(self):
        return self.gym_class.name
