from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import logout as auth_logout

# Create your views here.
from web import film
from web.film import logger
from web.film.models import Language, Actor, Category


@login_required(login_url="admin_login")
def language(request, template="film/language.html"):

    return render(request, template, {"language": Language.objects.all()})

@login_required(login_url="admin_login")
def category(request, template="film/category.html"):

    return render(request, template, {"category": Category.objects.all()})

@login_required(login_url="admin_login")
def actor(request, template="film/actor.html"):
    return render(request, template, {"actor": Actor.objects.all()})


# @login_required(login_url="admin_login")
# def demo_language(request, template="film/form_language.html"):
#
#     return render(request, template)


# add language return form and redirect list
@login_required(login_url="admin_login")
def add_language(request, template="film/form_language.html"):
    try:
        if request.method == "POST":
            language_name = request.POST.get("name").lstrip(" ").rstrip(" ")



            if not language_name:
                logger.warning("Language id={}  is not blank ".format(id))
                messages.add_message(request, messages.ERROR, "Enter valid data ")
                return redirect('add_language_list')
            if isalreadyLanguage(language_name):
                add_language_obj = Language.objects.create(
                    name=language_name
                )
                logger.info("new {} language insert successfully".format(language_name))
                messages.add_message(request, messages.SUCCESS, "Add new language success ")

                return redirect('language_list')
            logger.warning("Language {}  is alredy ".format(language_name))
            messages.add_message(request, messages.ERROR, "Language Already In List ")

            return redirect('add_language_list')
    except Exception as ex:
        logger.exception(ex.args)

    return render(request, template)

@login_required(login_url="admin_login")
def add_category(request, template="film/form_category.html"):
    try:
        if request.method == "POST":
            category_name = request.POST.get("name").lstrip(" ").rstrip(" ")



            if not category_name:
                logger.warning("category id={}  is not blank ".format(id))
                messages.add_message(request, messages.ERROR, "Enter valid data ")
                return redirect('add_category_list')
            if isalreadycategory(category_name):
                add_category_obj = Category.objects.create(
                    name=category_name
                )
                logger.info("new {} category insert successfully".format(category_name))
                messages.add_message(request, messages.SUCCESS, "Add new category success ")

                return redirect('category_list')
            logger.warning("Language {}  is alredy ".format(language_name))
            messages.add_message(request, messages.ERROR, "Language Already In List ")

            return redirect('add_category_list')
    except Exception as ex:
        logger.exception(ex.args)

    return render(request, template)



def isalreadyActor(first_name, last_name):
    return True


@login_required(login_url="admin_login")
def add_actor(request, template="film/form_actor.html"):
    try:
        if request.method == "POST":
            first_name = request.POST.get("first_name").lstrip(" ").rstrip(" ")
            last_name = request.POST.get("last_name").lstrip(" ").rstrip(" ")



            if not first_name or not last_name:
                logger.warning("actor is not blank ")
                messages.add_message(request, messages.ERROR, "Enter valid data ")
                return redirect('edit_actor')
            if isalreadyActor(first_name,last_name):
                add_language_obj = Actor.objects.create(
                    first_name=first_name,last_name=last_name
                )
                logger.info("new {} {} actor insert successfully".format(first_name,last_name))
                messages.add_message(request, messages.SUCCESS, "Add new Actor success ")

                return redirect('actor_list')
            logger.warning("Actor {} {} is alredy ".format(first_name,last_name))
            messages.add_message(request, messages.ERROR, "Actor Already In List ")

            return redirect('add_actor_list')
    except Exception as ex:
        logger.exception(ex.args)

    return render(request, template)










# Edit language ,rendar form with data-->submit-->redirect list
@login_required(login_url="admin_login")
def edit_language(request, id, template="film/form_language.html"): # ID 2
    try:
        if request.method == "POST":
            language_name = request.POST.get("name").lstrip(" ").rstrip(" ")
            print("name----",language_name)
            if not language_name:
                logger.warning("Language id={}  is not blank ".format(id))
                messages.add_message(request, messages.ERROR, "Language name not be blacked")
                return redirect('edit_language',id=id)
            else:
                print("updated::::::::::name:::::", language_name)
                status1 = Language.objects.filter(id=id)
                print(status1[0].name)

                status = isalreadyLanguage(language_name, id)  # FALSE
                print("Edit language status::::", status)
                if status:#True
                    Language.objects.filter(pk=id).update(name=language_name)
                    logger.info("Language id={} is Edit  success".format(id))
                    messages.add_message(request, messages.SUCCESS, "Edit language success ")
                    return redirect('language_list')
                # elif status1[0].name == language_name:
                #     messages.add_message(request, messages.ERROR, "Alrady in List Language ")
                #     return redirect('language_list')
                else:  ###False
                    logger.warning("Language id={}  is alredy ".format(id))
                    messages.add_message(request, messages.ERROR, "Alrady in List Language ")
                    return redirect('edit_language',id=id)
        obj_language = Language.objects.get(pk=id)
        logger.info("Language Edit successfully, Language ID is = {0}".format(id))
        return render(request, template, {"obj_language": obj_language})

    except Exception as ex:
        logger.exception(ex.args)
    return render(request,template)
@login_required(login_url="admin_login")
def edit_actor(request, id, template="film/form_actor.html"): # ID 2
    try:
        if request.method == "POST":
            first_name = request.POST.get("first_name").lstrip(" ").rstrip(" ")
            last_name = request.POST.get("last_name").lstrip(" ").rstrip(" ")
            if not first_name or not last_name:
                logger.warning("Actor id={}  is not blank ".format(id))
                messages.add_message(request, messages.ERROR, "Actor name not be blacked")
                return redirect('edit_actor')
            else:
                Actor.objects.filter(pk=id).update(first_name=first_name,last_name=last_name)
                logger.info("Actor id={}  is edited ".format(id))
                messages.add_message(request, messages.SUCCESS, "Actor name is edited ")
                return redirect('actor_list')
        obj_actor = Actor.objects.get(pk=id)
        logger.info("Actor Edit successfully, actor ID is = {0}".format(id))
        return render(request, template, {"obj_actor": obj_actor})

    except Exception as ex:
        logger.exception(ex.args)
    return render(request,template)



@login_required(login_url="admin_login")
def language_delete(request, id):
    try:
        Language.objects.get(pk=id).delete()
        logger.info("Language deleted successfully, Language ID is = {0}".format(id))
        messages.add_message(request, messages.SUCCESS, "Delete language success ")
    except Exception as ex:
        logger.exception(ex.args)
    return redirect("language_list")
@login_required(login_url="admin_login")
def actor_delete(request, id):
    try:
        Actor.objects.get(pk=id).delete()
        logger.info("Actor deleted successfully, Language ID is = {0}".format(id))
        messages.add_message(request, messages.SUCCESS, "Delete Actor successfully ")
    except Exception as ex:
        logger.exception(ex.args)
    return redirect("actor_list")


@login_required(login_url="admin_login")
def check_language(request):
    try:

        lname = request.POST.get("name")
        id = request.POST.get("id")
        if id:

            status = isalreadyLanguage(lname, id)
            if status:  # if data is already in DB
                return HttpResponse("true")
            return HttpResponse("false")


        print("languaghhbasd name ::::::::", lname)
        print("languaghhbasdy id ::::::::", id)
        # conditation for dublicate check
        status = isalreadyLanguage(lname)
        print("id       ", id)
        if status:
            return HttpResponse("true")

    except Exception as ex:
        logger.exception(ex.args)
    return HttpResponse("false")


def isalreadyLanguage(name, *args):
    try:
        if len(args) > 0:
            print("Code in if part")
            id = args[0]
            print("id---->", id)
            status = Language.objects.filter(~Q(id=id), name=name )  # print("asf")
            print("status----->", status)  # pass
            if status:  # validate exapt current filed
                print("if code: False")
                return False
            print("if code: True")
            return True
        else:
            status = Language.objects.filter(name=name)
            print("code in else part::")
            if status:  # if data is already in DB
                print("else code: False")
                return False
            print("else code: True")
            return True
    except Exception as e:
        logger.exception("exception ::::::::::::", e.args)
