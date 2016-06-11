# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import MaxValueValidator
from django.db import models
from djgeojson.fields import PointField

class MapObjects(models.Model):
	author_name = models.CharField('Имя писателя',max_length=30)
	century = models.IntegerField('Век',
		validators = [MaxValueValidator(25)]
		)
	description = models.TextField('Описание')
	image = models.ImageField('Изображение',upload_to='img/',blank=True)
	geom = PointField('Место на карте', blank=True)

	def __unicode__(self):		 # __unicode__ on Python 2
		return self.author_name


	@property
	def popupContent(self):		# return data for JS
	    return '<img src="{}" width="200" height="200" /><p><{}</p>'.format(
	    	self.image.url,
	    	self.description)