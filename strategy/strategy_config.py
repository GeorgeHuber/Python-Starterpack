from strategy.starter_strategy import StarterStrategy
from strategy.strategy_knight_rush import Strategy_Knight_Rush
from strategy.strategy_knight_rush_but_better import Strategy_Knight_Rush_But_Better
from strategy.strategy_timid_knight import Timid_Knight
from strategy.strategy import Strategy
from strategy.strategy_knight_rush_but_even_better import Strategy_Knight_Rush_But_Even_Better

"""Return the strategy that your bot should use.

:param playerIndex: A player index that can be used if necessary.

:returns: A Strategy object.
"""
def get_strategy(player_index: int) -> Strategy:  
  
  return Strategy_Knight_Rush_But_Even_Better()