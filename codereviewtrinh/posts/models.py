from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField(null=False)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return super().__str__()
    
    def upvote(self):
        self.upvotes += 1
        self.save()
        return self.upvotes
    
    def downvote(self):
        self.downvotes += 1
        self.save()
        return self.downvotes