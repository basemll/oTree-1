# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

# Codice del giocatore
class Cod(Page):
	form_model = models.Player
	form_fields = ['codice']

	def is_displayed(self):
		return self.subsession.round_number == 1


# Visualizzazione del ruolo
class Ruolo(Page):
	pass


# Visualizzazione IStruzioni
class Instruction(Page):
	pass
	# form_model = models.Player
	# form_fields = ['quest_answer1','quest_answer2','quest_answer3']
	
	# def error_message(self, values):
	# 	if (values["quest_answer1"] != Constants.quest_correct1 or values["quest_answer2"] != Constants.quest_correct2 or values["quest_answer3"] != Constants.quest_correct3):
	# 		return 'La tua risposta non è corretta'

# Esecuzione del compito per il receiver
class Task(Page):
	form_model = models.Player
	form_fields = ['slider1','slider2','slider3','slider4','slider5','slider6','slider7','slider8','slider9','slider10','slider11','slider12','slider13','slider14','slider15','slider16','slider17','slider18','slider19','slider20','slider21','slider22','slider23','slider24','slider25','slider26','slider27','slider28','slider29','slider30']
	timeout_seconds = 300
	
	def is_displayed(self):
		return (self.subsession.round_number == 1)# and self.player.id_in_group == 2)

	def before_next_page(self):
		if self.timeout_happened:
			post_dict = self.request.POST
			self.player.slider1 = int(post_dict['slider1'])
			self.player.slider2 = int(post_dict['slider2'])
			self.player.slider3 = int(post_dict['slider3'])
			self.player.slider4 = int(post_dict['slider4'])
			self.player.slider5 = int(post_dict['slider5'])
			self.player.slider6 = int(post_dict['slider6'])
			self.player.slider7 = int(post_dict['slider7'])
			self.player.slider8 = int(post_dict['slider8'])
			self.player.slider9 = int(post_dict['slider9'])
			self.player.slider10 = int(post_dict['slider10'])
			self.player.slider11 = int(post_dict['slider11'])
			self.player.slider12 = int(post_dict['slider12'])
			self.player.slider13 = int(post_dict['slider13'])
			self.player.slider14 = int(post_dict['slider14'])
			self.player.slider15 = int(post_dict['slider15'])
			self.player.slider16 = int(post_dict['slider16'])
			self.player.slider17 = int(post_dict['slider17'])
			self.player.slider18 = int(post_dict['slider18'])
			self.player.slider19 = int(post_dict['slider19'])
			self.player.slider20 = int(post_dict['slider20'])
			self.player.slider20 = int(post_dict['slider21'])
			self.player.slider20 = int(post_dict['slider22'])
			self.player.slider20 = int(post_dict['slider23'])
			self.player.slider20 = int(post_dict['slider24'])
			self.player.slider20 = int(post_dict['slider25'])
			self.player.slider20 = int(post_dict['slider26'])
			self.player.slider20 = int(post_dict['slider27'])
			self.player.slider20 = int(post_dict['slider28'])
			self.player.slider20 = int(post_dict['slider29'])
			self.player.slider20 = int(post_dict['slider30'])
		self.group.setTask()


# Proposer attende che il receiver termini il compito (non usato)
class WaitTask(WaitPage):
	body_text = 'Please wait'
	wait_for_all_groups = True 
	def after_all_players_arrive(self):		
		self.group.setTask()



# Il receiver a seconda di quante slider ha eseguito, chiede al proposer il suo claim
class Claim(Page):
	form_model = models.Group
	form_fields = ['receiver_claim']
	
	def receiver_claim_choices(self):
		if self.group.task_correct < 10:
			valori = [1]
		elif self.group.task_correct < 20:
			valori = [1,2]
		elif self.group.task_correct < 30:
			valori = [1,2,4]
		else:
			valori = [1,2,4,5]
		return valori

	def is_displayed(self):
		return (self.subsession.round_number == 1 and self.player.id_in_group == 2)
			

# Attesa prima delle proposte e accettazione 
class ResultsWaitPage(WaitPage):
	wait_for_all_groups = True 
		
# Proposta del proposer con strategy method
class Proposal(Page):
	form_model = models.Group
	form_fields = ['proposal']
	
	def vars_for_template(self):
		return {'prop': 10 - self.group.receiver_claim}

	def is_displayed(self):
		return (self.player.id_in_group == 1)

	def proposal_choices(self):
		valori = [1,2,4,5]
		return valori

# Accettazione del receiver con strategy method
class Accept(Page):
	form_model = models.Group
	form_fields = ['accept']
	
	def is_displayed(self):
		return (self.player.id_in_group == 2)

# Attesa e calcolo del guadagno        
class PayWaitPage(WaitPage):
	def after_all_players_arrive(self):
		self.group.setPayoff()

# Visualizzazione del guadagno
class Guadagno(Page):
    pass


# Questionario anagrafico
class QuestDem(Page):
	form_model = models.Player
	form_fields = ['eta','facolta','sex']

	def is_displayed(self):
		return self.subsession.round_number == Constants.num_rounds


page_sequence = [
	Cod,
	Instruction,
	Ruolo,
    Task,
    WaitTask,
    Claim,
    ResultsWaitPage,
    Proposal,
    ResultsWaitPage,
    Accept,
    PayWaitPage,
    Guadagno,
    QuestDem
]
