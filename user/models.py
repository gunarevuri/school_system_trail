from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

status_field = ['actice','inactive']
enroll_status = ['enrolled','not_enrolled']
class_subjects = ['maths','science','social','phisics']

class user(models.Model):
	user_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=255, blank=False)
	last_name = models.CharField(max_length=255, blank=False)
	phone_number = PhoneNumberField(blank=False)
	status = models.CharField(choices=[(x,x) for x in status_field], max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} {} and {}'.format(self.user_id,self.first_name,self.last_name)


class School(models.Model):
	school_id = models.AutoField(primary_key = True)
	school_name = models.CharField(max_length=255)
	user_id = models.ForeignKey(user, on_delete=models.CASCADE)
	state_id = models.IntegerField()
	city_id = models.IntegerField()
	contact_number = PhoneNumberField(blank=True)
	photo = models.ImageField(upload_to ='files_images/school_photo/',max_length=250,height_field=None,width_field=None)
	rural = models.BooleanField()
	district = models.CharField(max_length=255)
	block = models.CharField(max_length=255)
	cluster = models.CharField(max_length=255)
	village = models.CharField(max_length=255)
	zipcode = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'school_id {} and school_name{}'.format(self.school_id, self.school_name)

class userPersona(models.Model):
	user_id = models.ForeignKey(user, on_delete=models.CASCADE)
	# user_persona = models.CharField(choices=[(x,x) for x in user_persona_field])
	status = models.CharField(choices=[(x,x) for x in status_field], max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Parent(models.Model):
	user_id = models.ForeignKey(user, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} {}'.format(self.user_id.first_name,self.user_id.last_name)

class Student(models.Model):
	student_id = models.AutoField(primary_key = True)
	student_name = models.CharField(max_length=50)
	school_id = models.ForeignKey(School, on_delete=models.CASCADE)
	parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE)
	roll_number = models.IntegerField()
	gender = models.CharField(choices=[('M','Male'),('F','Female'),('not interested','not interested')], max_length=100)
	status = models.CharField(choices=[(x,x) for x in status_field],max_length=50)
	year_of_birth= models.IntegerField()
	photo = models.ImageField(upload_to ='files_images/student_photo/',max_length=250,height_field=None,width_field=None)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.student_name


class Teacher(models.Model):
	teacher_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(user, on_delete=models.CASCADE)
	school_id = models.ForeignKey(School, on_delete=models.CASCADE)
	gender = models.CharField(choices=[('M','Male'),('F','Female'),('not interested','not interested')], max_length=100)
	year_of_birth= models.IntegerField()
	photo = models.ImageField(upload_to ='files_images/teacher_photo/',max_length=250,height_field=None,width_field=None)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)




class State(models.Model):
	state_id = models.AutoField(primary_key = True)
	state_name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Class(models.Model):
	class_id = models.AutoField( primary_key = True)
	grade = models.IntegerField()
	section = models.CharField(max_length=255)
	school_id = models.ForeignKey(School, on_delete=models.CASCADE)
	academic_year = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'class Grade {} and Section {}'.format(self.grade, self.section)

class ClassSubjects(models.Model):
	class_subject_id = models.AutoField(primary_key=True)
	class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
	subject = models.CharField(choices=[(x,x) for x in class_subjects], max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return ' class Grade {}'.format(self.class_id.grade)

class Homework(models.Model):
	homework_id = models.AutoField(primary_key = True)
	class_subject_id = models.ForeignKey(ClassSubjects, on_delete = models.CASCADE)
	teacher_id = models.ForeignKey(Teacher, on_delete = models.CASCADE)
	due_data = models.DateTimeField()
	marks_total = models.DecimalField(max_digits=5,decimal_places=2)
	released_status = models.CharField(choices=[(x,x) for x in status_field], max_length=50)
	released_on = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Submissions(models.Model):
	submission_id = models.AutoField(primary_key = True)
	homework_id = models.ForeignKey(Homework, on_delete = models.CASCADE)
	student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
	submitted_data = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)	


class ClassEnrollment(models.Model):
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
	class_id = models.ForeignKey(Class, on_delete=models.CASCADE )
	enrollment_status = models.CharField(choices=[(x,x) for x in enroll_status], max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = (('student_id', 'class_id'),)









