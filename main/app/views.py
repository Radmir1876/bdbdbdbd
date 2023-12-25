from datetime import date
from django.shortcuts import render
from .models import Student, Course, Student2, Course2, Enrollmant, Person, Account

# Create your views here.

def index(request):
	# students = Student.objects.get(id=2).course.all()
	python = Course.objects.create(name='Физра')
	# student = python.student_set.get_or_create(name="Bob")
	# res = Student.objects.get(name='Bob').course.all()
	# st = Student.objects.get(id=3)
	# his = Course.objects.get(name='Физра')
	# his.student_set.add(st)
	# res = Student.objects.get(id=3).course.all()

	# django = Course2.objects.create(name="Django")
	# radmir = Student2.objects.create(name="Radmir")
	# res = Enrollmant(student=radmir, course=django, date=date.today(), mark=5)
	# res.save()

	# st = Student2.objects.get(id=2)
	# crs = Course2.objects.get(id=1)
	# res = st.course.all()
	# res = crs.student2_set.all()

	# s1mple = Person.objects.create(name='Sanya')
	# res = Account.objects.create(login='S1m', password='CSGOs1mple', user=s1mple)
	
	# res = Account.objects.get(user__id=1)
	# res.user.login = "S1mplE"
	# res.save()

	sam = Person.objects.create(name="sdgfds")
	acc = Account(login='erfggs', password="sdfgfsd")
	sam.account = acc
	sam.account.save()
	return render(request, 'index.html', {'student': sam})