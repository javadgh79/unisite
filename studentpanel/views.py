from django.shortcuts import render

def studentpanel_view(request):
    return render(request, "studentpanel.html", {})
