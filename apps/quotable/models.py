from __future__ import unicode_literals
from django.db import models
from ..login.models import User

# What does your model to be able to do
# now test it - test your objects
# SAVE INFORMATION TO DATABASE

class QuoteManager(models.Manager):
    def quote_validator(self, postdata):
        errors = []
        if len(postdata) < 1:
            errors.append("Invalid form") 	
        if len(errors) > 0:
            return errors
        else:
            pass


    def create_quote(self, postdata, poster):
        new_quote = Quote.objects.create(
            quote_poster = poster,
            quote_author = postdata['quote_author'],
            message = postdata['message']
        )

        pass
        

class Quote(models.Model):
    user_favs = models.ManyToManyField(User, related_name="fav_quotes")
    quote_poster = models.ForeignKey(User, related_name="made_quotes")
    quote_author = models.CharField(max_length=255) 
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager() 

    # #make validator
    #     poster = User.objects.get(id=quote_poster)
    #     author = request.POST['quote_author']
    #     message = request.POST['message']

    #     print "*******"
    #     print "inside quote manager about to create a quote"
    #     print "*******"
    #     # actually validate the quote

    #     existingQuote = Quote.objects.filter(quote_poster=poster, quote_author=author, message=message)

    #     if len(existingQuote) > 0:
    #         existingQuote[0].count += 1
    #         existingQuote[0].save()
    #     else:
    #         user = User.objects.get(id=quote_poster)
    #         new_quote = Quote.objects.create(quote_poster=poster, quote_author=author, message=message)
    #     return new_quote