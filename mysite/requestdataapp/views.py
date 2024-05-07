from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .forms import UserBioForm, UploadFileForm

# Create your views here.
def process_get_view(request: HttpRequest) -> HttpResponse:
    a = request.GET.get('a', "")
    b = request.GET.get('b', "")
    result = a + b

    context = {
        "a": a,
        "b": b,
        "result": result
    }
    return render(request, "requestdataapp/request-query-params.html", context=context)


def user_form(request: HttpRequest) -> HttpResponse:
    context = {
        "form": UserBioForm()
    }
    return render(request, "requestdataapp/user-bio-form.html", context=context)


def handle_file_upload(request: HttpRequest) -> HttpResponse:
    form = UploadFileForm()
    if request.method == "POST" and request.FILES.get("myfile"):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # myfile = request.FILES.get("myfile")
            myfile = form.cleaned_data["file"]
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            print("saved file", filename)

    context = {
        "form": form,
    }

    return render(request, "requestdataapp/file-upload.html", context=context)