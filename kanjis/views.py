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
    all_kanjis = list(Kanji.objects.all().values_list("id",flat=True))
    if not all_kanjis:
        current_kanji = None
        message = "No Kanjis in this category. Click to go back."
        return render(request, "kanjis/quiz.html", {"data" : current_kanji, "message": message,})
    
    bag_key = f'bag'
    bag = request.session.get(bag_key, all_kanjis.copy())
    bag_empty = False
    if not bag:
        bag = all_kanjis.copy()
        bag_empty = True

    last_key = f"last"
    last_id = request.session.get(last_key)

    if not last_id:
        current_kanji_id = random.choice(bag)
        bag.remove(current_kanji_id)
        request.session[bag_key] = bag
        request.session[last_key] = current_kanji_id
    else:
        current_kanji_id = last_id
    current_kanji = Kanji.objects.get(id=current_kanji_id)
    message = ""
    if request.method == "POST":
        request.session[last_key] = None
        return redirect('quiz')
    return render(request, "kanjis/quiz.html", {"data" : current_kanji, "message": message, "bag_empty": bag_empty,})

def quiz_jlpt(request, jlptlevel):
    all_kanjis = list(Kanji.objects.filter(jlpt=jlptlevel).values_list("id",flat=True))
    if not all_kanjis:
        current_kanji = None
        message = "No Kanjis in this category. Click to go back."
        return render(request, "kanjis/quiz.html", {"data" : current_kanji, "message": message,})
    
    bag_key = f'bag_{jlptlevel}'
    bag = request.session.get(bag_key, all_kanjis.copy())
    bag_empty = False
    if not bag:
        bag = all_kanjis.copy()
        bag_empty = True

    last_key = f"last_{jlptlevel}"
    last_id = request.session.get(last_key)

    if not last_id:
        current_kanji_id = random.choice(bag)
        bag.remove(current_kanji_id)
        request.session[bag_key] = bag
        request.session[last_key] = current_kanji_id
    else:
        current_kanji_id = last_id
    current_kanji = Kanji.objects.get(id=current_kanji_id)
    message = ""
    if request.method == "POST":
        request.session[last_key] = None
        return redirect('quiz_jaltap',jlptlevel=jlptlevel)
    return render(request, "kanjis/quiz.html", {"data" : current_kanji, "message": message, "bag_empty": bag_empty,})

def quiz_rkmath(request, course):
    course = str(course).upper()
    all_kanjis = list(Kanji.objects.filter(rkmath=course).values_list("id",flat=True))
    if not all_kanjis:
        current_kanji = None
        message = "No Kanjis in this category. Click to go back."
        return render(request, "kanjis/quiz.html", {"data" : current_kanji, "message": message,})
    
    bag_key = f'bag_{course}'
    bag = request.session.get(bag_key, all_kanjis.copy())
    bag_empty = False
    if not bag:
        bag = all_kanjis.copy()
        bag_empty = True

    last_key = f"last_{course}"
    last_id = request.session.get(last_key)

    if not last_id:
        current_kanji_id = random.choice(bag)
        bag.remove(current_kanji_id)
        request.session[bag_key] = bag
        request.session[last_key] = current_kanji_id
    else:
        current_kanji_id = last_id
    current_kanji = Kanji.objects.get(id=current_kanji_id)
    message = ""
    if request.method == "POST":
        request.session[last_key] = None
        return redirect('quiz_jaltap',course=course)
    return render(request, "kanjis/quiz.html", {"data" : current_kanji, "message": message, "bag_empty": bag_empty,})

def quiz_jaltap(request, chapter):
    all_kanjis = list(Kanji.objects.filter(jaltap=chapter).values_list("id",flat=True))
    if not all_kanjis:
        current_kanji = None
        message = "No Kanjis in this category. Click to go back."
        return render(request, "kanjis/quiz.html", {"data" : current_kanji, "message": message,})
    
    bag_key = f'bag_{chapter}'
    bag = request.session.get(bag_key, all_kanjis.copy())
    bag_empty = False
    if not bag:
        bag = all_kanjis.copy()
        bag_empty = True

    last_key = f"last_{chapter}"
    last_id = request.session.get(last_key)

    if not last_id:
        current_kanji_id = random.choice(bag)
        bag.remove(current_kanji_id)
        request.session[bag_key] = bag
        request.session[last_key] = current_kanji_id
    else:
        current_kanji_id = last_id
    current_kanji = Kanji.objects.get(id=current_kanji_id)
    message = ""
    if request.method == "POST":
        request.session[last_key] = None
        return redirect('quiz_jaltap',chapter=chapter)
    return render(request, "kanjis/quiz.html", {"data" : current_kanji, "message": message,"bag_empty": bag_empty,})

def quiz_somatome(request, jlptlevel, chapter):
    all_kanjis = list(Kanji.objects.filter(jlpt=jlptlevel, somatome=chapter).values_list("id",flat=True))
    if not all_kanjis:
        current_kanji = None
        message = "No Kanjis in this category. Click to go back."
        return render(request, "kanjis/quiz.html", {"data" : current_kanji, "message": message,})
    
    bag_key = f'bag_{jlptlevel}_{chapter}'
    bag = request.session.get(bag_key, all_kanjis.copy())
    bag_empty = False
    if not bag:
        bag = all_kanjis.copy()
        bag_empty = True

    last_key = f"last_{jlptlevel}_{chapter}"
    last_id = request.session.get(last_key)

    if not last_id:
        current_kanji_id = random.choice(bag)
        bag.remove(current_kanji_id)
        request.session[bag_key] = bag
        request.session[last_key] = current_kanji_id
    else:
        current_kanji_id = last_id
    current_kanji = Kanji.objects.get(id=current_kanji_id)
    message = ""
    if request.method == "POST":
        request.session[last_key] = None
        return redirect('quiz_somatome',jlptlevel=jlptlevel, chapter=chapter)
    return render(request, "kanjis/quiz.html", {"data" : current_kanji, "message": message, "bag_empty":bag_empty,})