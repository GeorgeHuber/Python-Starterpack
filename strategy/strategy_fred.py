from random import Random, choice
from game.game_state import GameState
import game.character_class

from game.item import Item
from game.player_state import PlayerState

from game.position import Position
from strategy.strategy import Strategy

import logging

class Strategy_Fred(Strategy):
    start_positions = [(0, 0), (9, 0), (9, 9), (0, 9)]
    center_positions = [(4,4),(4,5),(5,5),(5,4)]
    def strategy_initialize(self, my_player_index: int):
        return game.character_class.CharacterClass.KNIGHT

    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        my_player = game_state.player_state_list[my_player_index]
        current_position = my_player.position
        speed_remaining = my_player.stat_set.speed
        home = Position(self.start_positions[my_player_index][0],self.start_positions[my_player_index][1])
        def walking_distance(one, two):
            return abs(one.x-two.x)+abs(one.y-two.y)
        def is_valid_square(p: Position) -> bool:
            return p.x<10 and p.y<10
        def get_max_square(my_player, function):
            max_squares = [home]
            max_weight = function(home.x,home.y)
            for y in range(10):
                for x in range(10):
                    if(walking_distance(Position(x,y),my_player.position)<=my_player.stat_set.speed):
                        val = function(x,y)
                        if val==max_weight:
                            max_squares.append(Position(x,y))
                        if val>max_weight:
                            max_weight = val
                            max_squares = [Position(x,y)]
            return choice(max_squares)
        
        def function (x,y):
            weight = 0
            #0 to 9 
            center_adjust = (9-walking_distance(Position(4.5,4.5),Position(x,y)))
            weight+=center_adjust
            if (x,y) in self.center_positions:
                weight+=2
            return weight

        return get_max_square(my_player, function)


    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        player_state_list = game_state.player_state_list
        my_player = player_state_list[my_player_index]
        my_range = my_player.stat_set.range #+my_player.item.value.stat_set.range
        logging.info(my_range)
        lowest_health_index = -1 #index of player with the lowest health
        for i in range(0, 4):
            if i != my_player_index:
                other_player = player_state_list[i]
                distance = self.get_range_distance(my_player.position, other_player.position)
                if distance <= my_range:
                    if  lowest_health_index==-1 or other_player.health < player_state_list[lowest_health_index].health:
                        lowest_health_index = i
        if (lowest_health_index == -1):
            return my_player_index
        return lowest_health_index


    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:
        my_player = game_state.player_state_list[my_player_index]
        my_position = my_player.position
        if (my_position.x, my_position.y) == self.start_positions[my_player_index] and my_player.gold >= Item.HUNTER_SCOPE.value.cost:
            return Item.HUNTER_SCOPE
        return Item.NONE

    def use_action_decision(self, game_state: GameState, my_player_index: int) -> bool:
        return False

    def in_center(self, pos) -> bool:
        return (pos.x == 4 or pos.x == 5) and (pos.y == 4 or pos.y == 5)

    def get_range_distance(self, pos1, pos2) -> int:
        return max(abs(pos1.x - pos2.x), abs(pos1.y - pos2.y))

    # if we are currently in range of opponent and can move out of range to one of 2 safe squares
    def can_escape_range(self, my_player, other_player):
        current_distance = self.get_range_distance(my_player.position, other_player.position)
        new_distance = current_distance + 2 #hard coded for knight rn
        return new_distance > other_player.stat_set.range