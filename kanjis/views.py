from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
import random

# Create your views here.
def lander(request):
    return render(request, "kanjis/lander.html")

def data(request):
    mydata = Kanji.objects.all()

    if request.method == "POST":
        character = request.POST.get('character')
        pron1 = request.POST.get('pron1')
        mean1 = request.POST.get('mean1')
        pron2 = request.POST.get('pron2')
        mean2 = request.POST.get('mean2')
        jlpt = request.POST.get('jlpt')
        rkmath = request.POST.get('rkmath')
        jaltap = request.POST.get('jaltap')
        somatome = request.POST.get('somatome')

        if character == None or pron1 == None or mean1 == None or jlpt == None:
            return redirect("data")
        
        newKanji = Kanji(character=character, pron1=pron1, mean1=mean1, pron2=pron2, mean2=mean2, jlpt=jlpt, rkmath=rkmath, jaltap=jaltap, somatome=somatome)
        newKanji.save()
        return redirect("data")
    return render(request, "kanjis/data.html", {"data" : mydata,})

def quiz(request):
    if 'remaining_kanjis' not in request.session or not request.session['remaining_kanjis']:
        all_kanjis = list(Kanji.objects.values_list('character',flat=True))
        random.shuffle(all_kanjis)
        request.session['remaining_kanjis'] = all_kanjis
        request.session.modified = True

    kanji_characters = request.session['remaining_kanjis']
    current_kanji_character = kanji_characters.pop(0)
    request.session['remaining_kanjis'] = kanji_characters
    request.session.modified = True

    current_kanji = Kanji.objects.get(character=current_kanji_character)

    if request.method == "POST":
        return redirect('quiz')
    return render(request, "kanjis/quiz.html", {"data" : current_kanji,})

def get_kanji(request):
    category = request.GET.get("category","n5")
    kanjis = list(Kanji.objects.filter())