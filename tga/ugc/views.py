from django.shortcuts import render
from django.db.models import Max

# Create your views here.
import random
from .models import KinoAfisha, Serials, Netflix

class Conclusion():
    def __init__(self):
        self.table_name = ''
        self.count =''

    def change_const(self):
        self.table_name = 'film'
        self.count = ''

    # def init_random_value(self):
    #     self.change_const()
    #     if self.table_name == 'film':
    #         self.all_result = KinoAfisha.objects.all()
    #     elif self.table_name == 'netflix':
    #         self.all_result = Netflix.objects.all()
    #     elif self.table_name == 'serials':
    #         self.all_result = Serials.objects.all()
    #     self.max = self.all_result.last().id
    #     self.filmsID = []
    #     for self.n in range(5):
    #         self.n = random.randint(0, self.max)
    #         self.filmsID.append(self.n)
    #     return self.filmsID

    def output(self):
        self.change_const()
        if self.table_name == 'film':
            self.all_result = KinoAfisha.objects.all()
        elif self.table_name == 'netflix':
            self.all_result = Netflix.objects.all()
        elif self.table_name == 'serials':
            self.all_result = Serials.objects.all()
        self.max = self.all_result.last().id
        self.b = []
        for self.i in range(5):
            self.n = random.randint(0, self.max)
            self.content = (
                f'🗓 <b>Title:</b> {self.all_result.filter(pk=self.n).first().title} 🗓\n'
                f'🪐 <b>Description:</b> {self.all_result.filter(pk=self.n).first().description} 🪐\n'
                f'👾 <b>Producer:</b> {self.all_result.filter(pk=self.n).first().producer} 👾\n'
                f'📽 <b>Link:</b> {self.all_result.filter(pk=self.n).first().link} 📽\n')
            return self.content