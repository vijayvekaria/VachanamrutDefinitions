# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Word(models.Model):
	word = models.CharField(max_length=200)
	status = models.BooleanField()

class Definition(models.Model):
	definition = models.TextField()
	word = models.ForeignKey(Word)
	deleted = models.BooleanField()
