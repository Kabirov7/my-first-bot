# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class KinoAfisha(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=70, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    producer = models.CharField(max_length=70, blank=True, null=True)
    link = models.CharField(max_length=130, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kino_afisha'


class Netflix(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=70, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    producer = models.CharField(max_length=70, blank=True, null=True)
    link = models.CharField(max_length=130, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'netflix'


class Serials(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=70, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    producer = models.CharField(max_length=70, blank=True, null=True)
    link = models.CharField(max_length=130, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serials'
