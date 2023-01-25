from classes import Player
from constants import BATTING_AVERAGE_ATTRIBUTES, WHIP_ATTRIBUTES, SLUGGING_PERCENTAGE_ATTRIBUTES
from utility_functions import find_attributes_and_apply_weights, random_pitch_count
from random import random

brett = Player(1, 'Brett', 'Red Sox', 50, 50, 50, 50, 50, 50, 5)

def atBat(batter, pitcher, atBats, runnersOn):
  random = random()
  # fix all of this shit, just translating to python right now
  batter_advantage = find_attributes_and_apply_weights(batter, BATTING_AVERAGE_ATTRIBUTES)
  pitcher_advantage = find_attributes_and_apply_weights(pitcher, WHIP_ATTRIBUTES)
  # need pitcher fatique function
  hit_calculation = random - batter_advantage + pitcher_advantage
  if hit_calculation < .2:
    pitch_count = random_pitch_count(False, False)
    slugging_random = random()
    slugging_probability = slugging_random * find_attributes_and_apply_weights(batter, SLUGGING_PERCENTAGE_ATTRIBUTES)
    if slugging_probability > .8:
      outcome = 'homerun'
    if slugging_probability > .65:
      outcome = 'triple'
    if slugging_probability > .5:
      outcome = 'double'
    else:
      outcome = 'single'
  else:
    pitch_count = random_pitch_count(True, False)
    outcome = 'strikeout'
  if outcome != 'strikeout':
    newRunnersOn =
    # this is where i left off, need to add base running function next
print(find_attributes_and_apply_weights(brett, BATTING_AVERAGE_ATTRIBUTES))