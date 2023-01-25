from random import random

def find_attributes_and_apply_weights(player, attribute_weight_dicts):
  relevant_attribute_weighted_values = []
  for attribute in attribute_weight_dicts:
    weighted_attribute = attribute['weight'] * player.attributes[attribute['name']]
    relevant_attribute_weighted_values.append(weighted_attribute)
  return sum(relevant_attribute_weighted_values) / 100

def random_pitch_count(is_strikeout, is_walk):
  strikes_random = random()
  balls_random = random()
  if is_walk:
    ball_count = 4
  elif balls_random < .25:
    ball_count = 0
  elif balls_random < .5:
    ball_count = 1
  elif balls_random < .75:
    ball_count = 2
  else:
    ball_count = 3

  if is_strikeout:
    strike_count = 3
  elif strikes_random < .1:
    strike_count = 0
  elif strikes_random < .5:
    strike_count = 1
  else:
    strike_count = 2

  return {
    'strikes': strike_count,
    'balls': ball_count
  }
