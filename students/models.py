from django.db import models


class SmsBaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Created Time')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='Updated Time')


    class Meta:
        abstract = True

class Teacher(SmsBaseModel):
	staff_first_name = models.CharField(max_length=100,null=True,blank=True)
	staff_last_name = models.CharField(max_length=100,null=True,blank=True)
	
	def __str__(self):
         return self.staff_first_name+" "+self.staff_last_name


class Students(SmsBaseModel):

	GENDER_CHOICE = [
        ('1','Male'),('2','Female'),('3','Other')
    ]
	student_first_name = models.CharField(max_length=100,null=True,blank=True)
	student_last_name = models.CharField(max_length=100,null=True,blank=True)
	age =  models.PositiveIntegerField(default=0)
	gender = models.CharField(max_length=30,choices=GENDER_CHOICE,null=True,blank=True)
	reporting_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	
	def __str__(self):
		
		return self.student_first_name+" "+self.student_last_name


class Subjects(SmsBaseModel):
	subject_name = models.CharField(max_length=100)

	def __str__(self):
         return self.subject_name

class Marks(SmsBaseModel):
	TERM_CHOICE = [
		('1','One'),('2','Two'),('3','Three')
	]
	student = models.ForeignKey(Students, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
	term = models.CharField(max_length=10,choices=TERM_CHOICE,null=True,blank=True)
	mark = models.FloatField(default=0.0,null=True, blank=True)
	
	# class Meta:
	#     unique_together = (('term', 'student','subject'),)
	#     ordering = ('student', )

	def __str__(self):
         return self.student.student_first_name +" "+ student_last_name

	



