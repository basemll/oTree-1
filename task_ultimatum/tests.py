# -*- coding: utf-8 -*-
from __future__ import division

import random

from otree.common import Currency as c, currency_range

from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
   
	def play_round(self):
		self.submit(views.Cod,{'codice':'test'})
		self.submit(views.Instruction)
		self.submit(views.Ruolo)
		if self.player.id_in_group == 2 or self.player.id_in_group == 1:
			self.submit(views.Task,{'slider1':1,'slider2':1,'slider3':1,'slider4':1,'slider5':1,'slider6':1,'slider7':1,'slider8':1,'slider9':1,'slider10':1,'slider11':1,'slider12':1,'slider13':1,'slider14':1,'slider15':1,'slider16':1,'slider17':1,'slider18':1,'slider19':1,'slider20':1,'slider21':1,'slider22':1,'slider23':1,'slider24':1,'slider25':1,'slider26':1,'slider27':1,'slider28':1,'slider29':1,'slider30':1})
		if self.player.id_in_group == 2:
			self.submit(views.Claim,{'receiver_claim':1})
		if self.player.id_in_group == 1:
			self.submit(views.Proposal,{'proposal':1})
		if self.player.id_in_group == 2:
			self.submit(views.Accept,{'accept':random.randint(0,1)})
		self.submit(views.Guadagno)

	def validate_play(self):
		pass
