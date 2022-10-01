from strategy.starter_strategy import StarterStrategy
from strategy.strategy_knight_rush import Strategy_Knight_Rush
from strategy.strategy import Strategy

"""Return the strategy that your bot should use.

:param playerIndex: A player index that can be used if necessary.

:returns: A Strategy object.
"""
def get_strategy(player_index: int) -> Strategy:  
  
  return Strategy_Knight_Rush()