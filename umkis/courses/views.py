from django.shortcuts import render

from .models import Course

# Create your views here.
def test(request):

    first_course = Course.objects.first()

    return render(
        request,
        'test.html',
        context={
            'course': first_course,
        }
    )
