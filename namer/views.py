from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Matrix, YEARS, GENDERS
import cPickle
import numpy as np

gender_ref = {"Male": "M",
              "Female": "F",
              "Both": "N"}


def find_matrix(year, gender):
    m = Matrix.objects.filter(year=year, gender=gender_ref[gender])

    return m[0]


def letter(n):
    if n == 26:
        return "."
    else:
        return chr(n + 97)


def good_style(word):
    if len(word) > 10 or len(word) < 3:
        return False

    word = word.lower()
    ct = 0
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            ct += 1
        else:
            ct = 0
        if ct == 2:
            return False

    vowels = False
    ct = 0
    for letter in word:
        ct += 1
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            vowels = True
            ct = 0
        if ct == 4:
            return False

    if vowels == False:
        return False
    return True


def chain(model, pi):
    st = ""
    current = np.random.choice(len(pi), p=pi)
    nextl = np.random.choice(len(model[current]), p=model[current])
    st += letter(current).upper()

    while nextl != 26:
        nextl = np.random.choice(len(model[current]), p=model[current])
        if nextl != 26:
            current = nextl
            st += letter(nextl)
    return st


def find_name(m):
    model = cPickle.loads(str(m.probability_matrix))
    pi = cPickle.loads(str(m.pi))
    while True:
        rname = chain(model, pi)
        if (good_style(rname)):
            break
    return rname


def index(request):
    year = request.POST.get('year', 0)
    gender = request.POST.get('gender', 'z')
    data = {'years': YEARS,
            'selected_year': 2014,
            'genders': GENDERS,
            'selected_gender': gender}
    if year != 0 and gender != 'z':
        m = find_matrix(year, gender)
        data['name'] = find_name(m)
        data['selected_year'] = int(year)
        data['selected_gender'] = gender
        return render(request, 'namer/index.html', data)
    else:
        return render(request, 'namer/index.html', data)
