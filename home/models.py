from django.db import models
from django.template.defaultfilters import slugify

class Tag(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='home/', default='blank/blank.jpg')
    body = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)


    # Saving unique slug    
    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.headline)

            has_slug = Post.objects.filter(slug=slug).exists()
            count = 0
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()
                            
            self.slug = slug

        super().save(*args, **kwargs)


    def __str__(self):
        return self.headline
    

