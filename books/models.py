from django.db import models
from user.models import UserInfo

# Create your models here.
class BooksInfoManager(models.Manager):
    def get_art_music(self):
        return super(BooksInfoManager, self).get_queryset().filter(type='art_music',isDelete=False)
    def get_science_engineering(self):
        return super(BooksInfoManager, self).get_queryset().filter(type='science_engineering',isDelete=False)
    def get_biology_medicine(self):
        return super(BooksInfoManager, self).get_queryset().filter(type='biology_medicine',isDelete=False)
    def get_financial_business(self):
        return super(BooksInfoManager, self).get_queryset().filter(type='financial_business',isDelete=False)
    def get_literature_social(self):
        return super(BooksInfoManager, self).get_queryset().filter(type='literature_social',isDelete=False)
    def get_other(self):
        return super(BooksInfoManager, self).get_queryset().filter(type='other',isDelete=False)
    def get_title(self, title):
        return super(BooksInfoManager, self).get_queryset().filter(title=title,isDelete=False)
    def create_book(self, title, type, picture, price, address, description, user):
        book = self.create(title=title, type=type, picture=picture, price=price, address=address, description=description,user=user, isDelete=False)
        return book

class BooksInfo(models.Model):
    title = models.CharField(max_length=50)  #名称
    type = models.CharField(max_length=50)  # 类型
    picture = models.ImageField(upload_to='books')  #图片
    price = models.DecimalField(max_digits=10,decimal_places=2) #价格
    isDelete = models.BooleanField(default=False)  #删除
    address = models.CharField(max_length=100, default='', blank=True)  #交易地点
    description = models.CharField(max_length=300, default='', blank=True) #描述
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE) #商家Id
    books = BooksInfoManager()
    def __str__(self):
        return self.title