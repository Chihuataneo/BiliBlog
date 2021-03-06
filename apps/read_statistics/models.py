from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.fields import exceptions
from django.utils import timezone


class ReadNumExpandMethod(object):
	def get_read_num(self):
		try:
			# get_for_model中的参数，传入的是需要连接的对象
			# 例如ReadNum要想与Blog连接，那么self就是Blog
			# 在这儿，因为Blog继承了ReadNumExpandMethod，所以写的是self
			ct = ContentType.objects.get_for_model(self)
			# 传入ct和Blog的id，通过ContentType得到相应的ReadNum对象
			readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
			# 返回阅读量
			return readnum.read_num
		except exceptions.ObjectDoesNotExist:
			# 如果出错，则返回0
			return 0


class ReadNum(models.Model):
	# 每篇博客的阅读量
	read_num = models.IntegerField('阅读总数', default=0)

	# 与ContentType建立外键关系
	# 固定写法
	content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	object_id = models.PositiveIntegerField('博客ID')
	content_object = GenericForeignKey('content_type', 'object_id')

	class Meta:
		verbose_name = '阅读总数'
		verbose_name_plural = verbose_name


class ReadDetail(models.Model):
	date = models.DateField('日期', default=timezone.now)
	# 每天中，每篇博客的阅读量，跟ReadNum还是不同的
	read_num = models.IntegerField('某天阅读数', default=0)

	# 与ContentType建立外键关系
	# 固定写法
	content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	object_id = models.PositiveIntegerField('博客ID')
	content_object = GenericForeignKey('content_type', 'object_id')

	class Meta:
		verbose_name = '日期阅读数'
		verbose_name_plural = verbose_name
