from random import Random
from game.game_state import GameState
import game.character_class

from game.item import Item
from game.player_state import PlayerState

from game.position import Position
from strategy.strategy import Strategy

import logging

class Strategy_Knight_Rush(Strategy):
    start_positions = [(0, 0), (9, 0), (9, 9), (0, 9)]

    def strategy_initialize(self, my_player_index: int):
        return game.character_class.CharacterClass.KNIGHT

    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        my_player = game_state.player_state_list[my_player_index]
        current_position = my_player.position
        speed_remaining = my_player.stat_set.speed

        #logging.info((current_position.x, current_position.y) == self.start_positions[my_player_index])
        #logging.info(my_player.gold >= Item.HUNTING_SCOPE.value.cost)
        #logging.info("\n")
        if (current_position.x, current_position.y) == self.start_positions[my_player_index] and my_player.gold >= Item.HUNTER_SCOPE.value.cost and my_player.item == Item.NONE:
            return current_position

        while(speed_remaining >= 0 and not self.in_center(current_position)):
            if current_position.x < 4:
                current_position.x += 1
            elif current_position.x > 5:
                current_position.x -= 1
            elif current_position.y > 5:
                current_position.y -= 1
            elif current_position.y < 4:
                current_position.y += 1
            speed_remaining -= 1
        return current_position


    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        player_state_list = game_state.player_state_list
        my_player = player_state_list[my_player_index]
        my_range = my_player.stat_set.range #+my_player.item.value.stat_set.range
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
        #logging.info((my_position.x, my_position.y) == self.start_positions[my_player_index])
        #logging.info(my_player >= Item.HUNTING_SCOPE.value.cost)
        #logging.info("\n")
        if (my_position.x, my_position.y) == self.start_positions[my_player_index] and my_player.gold >= Item.HUNTER_SCOPE.value.cost:
            return Item.HUNTER_SCOPE
        return Item.NONE

    def use_action_decision(self, game_state: GameState, my_player_index: int) -> bool:
        return False

    def in_center(self, pos) -> bool:
        return (pos.x == 4 or pos.x == 5) and (pos.y == 4 or pos.y == 5)

    def get_range_distance(self, pos1, pos2) -> int:
        return max(abs(pos1.x - pos2.x), abs(pos1.y - pos2.y))