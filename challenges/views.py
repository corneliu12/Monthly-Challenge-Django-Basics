from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Eat meat every day!",
    "february": "Walk 20 min each day!",
    "march": "Learn Django always",
    "april": "Walk again",
    "may": "Study always",
    "june": "Watch TV",
    "july": "4th of July"
}

# Create your views here.


def monthly_challenge_by_number(request, month):

    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponse("This month is not supported!")

    return HttpResponse(challenge_text)
