from django.db import models

# Create your models here.

GENDER = (
    ("M","Male"),
    ("F","Female"),
    ("O","Other"),
)

CLASSLIST = (
    ("LKG","LKG"),
    ("UKG","UKG"),
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
    ("9","9"),
    ("10","10"),
)

class Classes(models.Model):
    className = models.CharField(max_length=200,choices=CLASSLIST)

    def __str__(self):
        return self.className
    

class Student(models.Model):
    full_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    address = models.TextField()
    gender = models.CharField(max_length=200,choices=GENDER)
    nationality = models.CharField(max_length=200,choices=(("INDIAN","INDIAN"),("OTHER","OTHER")))
    city = models.CharField(max_length=30,choices=(("PURNEA","PURNEA"),("BHAGALPUR","BHAGALPUR")))
    state = (models.CharField(max_length=200))
    pin_code = models.IntegerField()
    contact = models.CharField(max_length=25)
    image = models.ImageField(upload_to="students/",null=True,blank=True)
    dob = models.DateField()
    className = models.OneToOneField("Classes",on_delete=models.CASCADE)


    def __str__(self):
        return self.full_name
    
    

