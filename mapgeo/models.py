# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from djgeojson.fields import PointField

class MapObjects(models.Model):
	author_name = models.CharField('Имя писателя',max_length=30)
	century = models.IntegerField('Век')
	description = models.TextField('Описание')
	image = models.ImageField('Изображение',upload_to='/img/')
	geom = PointField()