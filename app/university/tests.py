from django.test import TestCase

from university.models import Student


class StudentTest(TestCase):
    def testStudent(self):
        student = Student(name='Mike')
        self.assertEquals(student.name, 'Mike')
