# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'ceel'

doc = """
proposal make the effort then ultimatum game
"""


class Constants(BaseConstants):
    name_in_url = 'inverse_task_ultimautum'
    players_per_group = 2
    num_rounds = 1
    endowment = 10


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for player in self.get_players():
            player.correct_slider1 = random.randint(0,250)
            player.correct_slider2 = random.randint(0,250)
            player.correct_slider3 = random.randint(0,250)
            player.correct_slider4 = random.randint(0,250)
            player.correct_slider5 = random.randint(0,250)
            player.correct_slider6 = random.randint(0,250)
            player.correct_slider7 = random.randint(0,250)
            player.correct_slider8 = random.randint(0,250)
            player.correct_slider9 = random.randint(0,250)
            player.correct_slider10 = random.randint(0,250)
            player.correct_slider11 = random.randint(0,250)
            player.correct_slider12 = random.randint(0,250)
            player.correct_slider13 = random.randint(0,250)
            player.correct_slider14 = random.randint(0,250)
            player.correct_slider15 = random.randint(0,250)
            player.correct_slider16 = random.randint(0,250)
            player.correct_slider17 = random.randint(0,250)
            player.correct_slider18 = random.randint(0,250)
            player.correct_slider19 = random.randint(0,250)
            player.correct_slider20 = random.randint(0,250)
            player.correct_slider21 = random.randint(0,250)
            player.correct_slider22 = random.randint(0,250)
            player.correct_slider23 = random.randint(0,250)
            player.correct_slider24 = random.randint(0,250)
            player.correct_slider25 = random.randint(0,250)
            player.correct_slider26 = random.randint(0,250)
            player.correct_slider27 = random.randint(0,250)
            player.correct_slider28 = random.randint(0,250)
            player.correct_slider29 = random.randint(0,250)
            player.correct_slider30 = random.randint(0,250)
            print ('Player Slider 1 Correct',player.correct_slider1)


class Group(BaseGroup):
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    proposal = models.CurrencyField(doc = """ Proposal """ )    
    accept = models.CurrencyField(choices = [(1,'Yes'),(0,'No')], doc = """ Accetp/Refuse """ )
    receiver_claim = models.CurrencyField()
    task_correct = models.IntegerField()
    

    # Conta quanti slider sono corretti
    def setTask(self):
        self.receiver = self.get_player_by_role('R')
        self.proposer = self.get_player_by_role('P')
        self.task_correct = 0
        if self.proposer.slider1 == self.proposer.correct_slider1:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider2 == self.proposer.correct_slider2:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider3 == self.proposer.correct_slider3:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider4 == self.proposer.correct_slider4:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider5 == self.proposer.correct_slider5:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider6 == self.proposer.correct_slider6:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider7 == self.proposer.correct_slider7:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider8 == self.proposer.correct_slider8:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider9 == self.proposer.correct_slider9:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider10 == self.proposer.correct_slider10:
            self.task_correct = self.task_correct + 1

        if self.proposer.slider11 == self.proposer.correct_slider11:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider12 == self.proposer.correct_slider12:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider13 == self.proposer.correct_slider13:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider14 == self.proposer.correct_slider14:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider15 == self.proposer.correct_slider15:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider16 == self.proposer.correct_slider16:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider17 == self.proposer.correct_slider17:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider18 == self.proposer.correct_slider18:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider19 == self.proposer.correct_slider19:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider20 == self.proposer.correct_slider20:
            self.task_correct = self.task_correct + 1

        if self.proposer.slider21 == self.proposer.correct_slider21:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider22 == self.proposer.correct_slider22:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider23 == self.proposer.correct_slider23:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider24 == self.proposer.correct_slider24:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider25 == self.proposer.correct_slider25:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider26 == self.proposer.correct_slider26:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider27 == self.proposer.correct_slider27:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider28 == self.proposer.correct_slider28:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider29 == self.proposer.correct_slider29:
            self.task_correct = self.task_correct + 1
        if self.proposer.slider30 == self.proposer.correct_slider30:
            self.task_correct = self.task_correct + 1

        print ('slider 1 = ', self.proposer.slider1,' correct ',self.proposer.correct_slider1)

        print ('****************** CORRECT CLAIM ===== ', self.task_correct)


    def setPayoff(self):
        self.receiver = self.get_player_by_role('R')
        self.proposer = self.get_player_by_role('P')
        
        # print 'Accettazione ', self.receiver.accept_0, self.receiver.accept_1,' Real Proposta ', self.receiver.real_proposta, ' Real Accettazione ',self.receiver.real_accettazione
        self.receiver.payoff = 0
        self.proposer.payoff = 0
        if self.accept == 1:
            self.receiver.payoff = self.proposal
            self.proposer.payoff = Constants.endowment - self.proposal
        print ('PAYOFF P R ',self.proposer.payoff,self.receiver.payoff)
        



class Player(BasePlayer):
    codice = models.CharField(doc=""" Codice del giocatore """)

    quest_answer1 = models.IntegerField(choices = range(0,Constants.endowment + 1,1))
    quest_answer2 = models.IntegerField(choices = range(0,Constants.endowment + 1,1))
    quest_answer3 = models.IntegerField(choices = range(0,Constants.endowment + 1,1))  

    eta = models.IntegerField(choices = range(18,60,1),doc = """ Eta anagrafica """)
    facolta = models.CharField(widget=widgets.RadioSelectHorizontal(),choices=['Economics', 'Law', 'Matematics', 'Letters','Engeneering','Phisics','Other','Worker'],doc = """ Facolta di appartenenza """)  
    sex = models.IntegerField(choices = [(1,'Male'),(2,'Female')], doc = """ sex """ )

    slider1 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider2 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider3 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider4 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider5 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider6 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider7 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider8 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider9 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider10 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider11 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider12 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider13 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider14 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider15 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider16 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider17 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider18 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider19 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider20 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider21 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider22 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider23 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider24 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider25 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider26 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider27 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider28 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider29 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))
    slider30 = models.IntegerField(min=0,max=250,widget=widgets.SliderInput(attrs={'step':1}))

    correct_slider1 = models.IntegerField(doc=""" risposte corrette slider """)
    correct_slider2 = models.IntegerField()
    correct_slider3 = models.IntegerField()
    correct_slider4 = models.IntegerField()
    correct_slider5 = models.IntegerField()
    correct_slider6 = models.IntegerField()
    correct_slider7 = models.IntegerField()
    correct_slider8 = models.IntegerField()
    correct_slider9 = models.IntegerField()
    correct_slider10 = models.IntegerField()
    correct_slider11 = models.IntegerField()
    correct_slider12 = models.IntegerField()
    correct_slider13 = models.IntegerField()
    correct_slider14 = models.IntegerField()
    correct_slider15 = models.IntegerField()
    correct_slider16 = models.IntegerField()
    correct_slider17 = models.IntegerField()
    correct_slider18 = models.IntegerField()
    correct_slider19 = models.IntegerField()
    correct_slider20 = models.IntegerField()
    correct_slider21 = models.IntegerField()
    correct_slider22 = models.IntegerField()
    correct_slider23 = models.IntegerField()
    correct_slider24 = models.IntegerField()
    correct_slider25 = models.IntegerField()
    correct_slider26 = models.IntegerField()
    correct_slider27 = models.IntegerField()
    correct_slider28 = models.IntegerField()
    correct_slider29 = models.IntegerField()
    correct_slider30 = models.IntegerField()

    

    
    
    

    def role(self):
        if self.id_in_group == 1:
            return 'P'
        else:
            return 'R'
