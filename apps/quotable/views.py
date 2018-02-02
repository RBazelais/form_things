from django.shortcuts import render, reverse, redirect
from ..login.models import User
from .models import Quote

# Create your views here.
def landing(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'session_user': user,
        'all_users' : User.objects.all(),
        'all_quotes': Quote.objects.all(),
        'user_made_quotes' : len(User.objects.filter(id=request.session['user_id']))
    }
    # all_users = User.objects.all() # all users in database
    return render(request, 'dashboard/userview.html', context)

def process_quote(request):
    if request.method == 'POST':
        errors = Quote.objects.quote_validator(request.POST)
        if len(errors):
            return redirect('/dashboard') 
        else:
            poster = User.objects.get(id=request.session['user_id'])
            new_quote = Quote.objects.createQuote(
                quote_poster=poster, 
                quote_author=request.POST['quote_author'],
                message=request.POST['message']
            )
            return redirect('/dashboard')
        return redirect('/')
    

