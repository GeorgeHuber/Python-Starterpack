from random import Random
from game.game_state import GameState
import game.character_class

from game.item import Item

from game.position import Position
from strategy.strategy import Strategy

class StrategyTwo(Strategy):
    def strategy_initialize(self, my_player_index: int):
        return game.character_class.CharacterClass.KNIGHT

    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        my_player = game_state.player_state_list[my_player_index]
        current_position = my_player.position
        current_x = current_position.x
        current_y = current_position.y
        speed_remaining = my_player.stat_set.speed
        while(speed_remaining >= 0 and not self.in_center(current_x,current_y)):
            if(current_x < 4):
                current_x += 1
            elif(current_x > 5):
               current_x -= 1
            elif(current_y > 5):
                current_y -= 1
            elif(current_y < 4):
                current_y += 1
            speed_remaining -= 1
        return Position(current_x, current_y)


    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        player_state_list = game_state.player_state_list
        my_player = player_state_list[my_player_index]
        my_range = my_player.stat_set.range
        for i in range(0, 3):
            if i != my_player_index:
                other_player = player_state_list[i]
                distance = self.get_range_distance(my_player.position, other_player.position)
                if distance <= my_range:
                    return i
        return 0


    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:
        return Item.NONE

    def use_action_decision(self, game_state: GameState, my_player_index: int) -> bool:
        return False

    def in_center(self, x, y) -> bool:
        return (x == 4 or x == 5) and (y == 4 or y == 5)

    def get_range_distance(self, pos1, pos2) -> int:
        return max(abs(pos1.x - pos2.x), abs(pos1.y - pos2.y))