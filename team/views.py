from django.shortcuts import render

# Create your views here.

def team(request):
    """ A view to go to team.html """

    return render(request, 'team/team.html')
