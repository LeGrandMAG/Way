from django.shortcuts import render
from main.models import User

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .src import utility,database
from django.contrib.auth import authenticate, login
import json
from django.conf import settings
from sentry_sdk import capture_exception
from .models import Professor, Rating
# Create your views here.

def DisplayRating(request):
    rating = Rating.objects.all()

    
    context = { 'rating': rating}
    return render(request, 'rateMyProf/rating.html', context)





def index(request) :
    context = {}

    newContext = request.session.get('redirect_context', {})
    context.update(newContext)
    request.session['redirect_context'] = {}

    context["subjects"] = []
    context["prof"] = []
    for sub in database.getSubjectList() :
        context["subjects"].append(str(sub))

    for prof in database.getProfList() :
        context["prof"].append(str(prof))

    if request.user.is_authenticated:
        context["loggedIn"] = "true"

    else :
        context["loggedIn"] = "false"
    print(context)
    return render(request, 'webview/index.html', context)




def addRating(request) :
    data = json.loads(request.body)
    print(data)
    errorMsg = "Some internal error occurred, Please try again"
    subDataList  = data["subject"].split("-")
    subject, Sstatus = database.getSubjectFromCode(subDataList[0].strip())
    profDataList = data["prof"].split("-")
    prof, Pstatus = database.getProfessor(profDataList[0].strip(), settings.FACULTY_DEPARTMENT_DICT_REVERSE[profDataList[1].strip()])
    tagsList = []
    if data["tags"] is not "" :
        #Getting values of tags
        for tag in json.loads(data["tags"]) :
            tagsList.append(tag["value"])
    if Sstatus and Pstatus :
        try :
            attendance = int(data.get("attendance", 0))
            taMarks = int(data.get("taMarks", 0))
            grades = int(data.get("grades", 0))
            timing = int(data.get("timing", 0))
            msg, status = database.addNewrating(subject,prof,request.user,attendance, taMarks, grades, timing, tagsList)
            if status :
                return JsonResponse({"swalStatus" : "success", "msg" : "Rating successfully submitted"}, status=200)
            else :
                errorMsg = msg
        except Exception as e :
            errorMsg = "Some unknown error occurred. Please try again later"
            capture_exception(e)
    else :
        errorMsg = "Invalid subject or professor, Please try again"
    return JsonResponse({"msg" : errorMsg, "swalStatus" : "error"}, status=400)
    # subList = database.getSubjectList()


def getRating(request) :
    data = json.loads(request.body)
    errorMsg = "Some internal error occurred. Please try again later."
    print(data)
    try :
        subDataList = data["subject"].split("-")
        subject, Sstatus = database.getSubjectFromCode(subDataList[0].strip())
        profDataList = data["prof"].split("-")
        prof, Pstatus = database.getProfessor(profDataList[0].strip(),
                                              settings.FACULTY_DEPARTMENT_DICT_REVERSE[profDataList[1].strip()])
        if Sstatus and Pstatus :
            rateObj, status = database.getFinaRating(subject, prof)
            if status :
                return JsonResponse({"attendance" : rateObj.attendance*20, "ta" :rateObj.ta*20, "grade" : rateObj.grade*20 , "time" : rateObj.timing*20, "tags" : ",".join(json.loads(rateObj.tags))}, status=200)
            else :
                errorMsg = rateObj
        else :
            errorMsg = "Invalid Subject or Professor"
    except IndexError as e :
        errorMsg = "Please select both subject and professor"
        capture_exception(e)
    except Exception as e :
        capture_exception(e)

    return JsonResponse({"msg": errorMsg, "swalStatus": "error"}, status=400)