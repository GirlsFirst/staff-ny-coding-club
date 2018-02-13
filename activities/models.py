from django.db import models

class Activity(models.Model): 
	
	Activity_Type_Choices = (
		('MZ', 'Moment of Zen'),
		('IB', 'Icebreaker'),
		('BR', 'Brainstorm'),
		('DC', 'Discussion'),
		('TB', 'Teambuilding'),
		)


	Space_Type_Choices= (
		('R', "Room"),
		('V', "Virtual"),
		)


	activity_name = models.CharField(max_length = 100)
	activity_type = models.CharField (
		max_length =2, 
		choices= Activity_Type_Choices, 
		default='Icebreaker')
	num_people = models.IntegerField()
	space_type = models.CharField(
		max_length=2, 
		choices = Space_Type_Choices, 
		default= 'Room') 
	## rating =
	activity_desc = models.TextField(max_length = 1000)
	variations = models.TextField(max_length = 250)
