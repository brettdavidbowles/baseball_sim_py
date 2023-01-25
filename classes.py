class Player:
  def __init__(self, id, name, team, strength, speed, endurance, composure, reflexes, intellect, willpower):
    self.id = id
    self.name = name
    self.team = team
    self.attributes = {
      'strength': strength,
      'speed': speed,
      'endurance': endurance,
      'composure': composure,
      'reflexes': reflexes,
      'intellect': intellect,
      'willpower': willpower
    }