from django.db import models

# Create your models here.

# 准备书籍列表信息的模型类
class BookInfo(models.Model):
    '''
    创建字段以及对应的字段类型
    '''
    name = models.CharField(max_length=20, verbose_name='名称')
    pub_date = models.DateField(verbose_name='发布日期', null=True)
    readcount = models.IntegerField(verbose_name='阅读量', default=0)
    commentcount = models.IntegerField(verbose_name='评论量', default=0)
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        # 指定数据库表名
        db_table = 'bookinfo'
        # 在admin站点中显示的表的名称
        verbose_name = '图书'

    def __str__(self):
        '''定义每个数据对象的显示信息'''
        return self.name


# 准备人物列表信息的模型累
class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name
