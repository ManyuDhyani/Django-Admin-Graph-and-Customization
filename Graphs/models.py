from django.db import models

MALE, FEMALE = range(2)
GENDER = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE')
)

CHINESE, SPANISH, ENGLISH, FRENCH, HINDI, ARABIC, RUSSIAN = range(7)
LANGUAGES = (
    (CHINESE, 'CHINESE'),
    (SPANISH, 'SPANISH'),
    (ENGLISH, 'ENGLISH'),
    (FRENCH, 'FRENCH'),
    (HINDI, 'HINDI'),
    (ARABIC, 'ARABIC'),
    (RUSSIAN, 'RUSSIAN'),
)

class Student(models.Model):
    full_name = models.CharField('Full Name', max_length=50)
    gender = models.PositiveSmallIntegerField('Gender', choices=GENDER, default=MALE)
    language = models.PositiveSmallIntegerField('Language', choices=LANGUAGES, default=ENGLISH)
    grades = models.CharField('Grades', max_length=2)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Student'


################# Pie Chart & Bar Chart Model#################

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name


################# Import Model#################
class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name