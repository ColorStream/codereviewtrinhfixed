from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField(null=False)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.text

    # These were just for ease, but then I never got around to getting to use them anyway. 
    # Not the best for something you'd want users to only like/dislike once, but would work in a pinch.
    def upvote(self):
        self.upvotes += 1
        self.save()
        return self.upvotes
    
    def downvote(self):
        self.downvotes += 1
        self.save()
        return self.downvotes
