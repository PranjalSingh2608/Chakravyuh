from django.shortcuts import render
from django.http import HttpResponse
import environ
import os
def display_image(request, pk):
    correct_answer = os.environ.get('CLUE_KEY')
    print(correct_answer)
    try:
        user_answer = int(pk)
        print(user_answer)
        if user_answer == correct_answer:
            url = os.environ.get('SECRET_KEY')
            image_url = url
            return render(request, 'photo.html', {'image_url': image_url})
        else:
            return HttpResponse("Wrong answer. Please try again.")

    except ValueError:
        return HttpResponse("Invalid input. Please enter a valid integer.")
