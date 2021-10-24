from django.db import models

# Create your models here.
class Todolist(models.Model):
	# ถ้ามีการเปลี่ยนแปร ต้องทำคำสั่ง 2 คำสั่งใหม่
	# 1. pyrhon manage.py makemigration --> ทำการสร้างไฟล์ใหม่
	# 2. pyrhon manage.py migrate --> สร้างฐานข้อมูล 
	title = models.CharField(max_length=100) # max_length=100 --> อยากเก็บตัวอักษรกี่ตัว
	detail = models.TextField(null=True, blank=True) # null=True --> เราสามารถจัดเก็บเป็นค่าว่างได้, blank=True --> ไม่จำเป็นต้องกรอกก็ได้	

	def __str__(self):
		return self.title # เปลี่ยน ชื่อ Todolist object ให้แสดง ชื่อ title แทน