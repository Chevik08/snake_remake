from snake import snake_controls
import os
import copy


def simulation(game_hash: str):
    players_hash = []
    count = 0
    snake = [[[4, 3], [5, 3]], [[7, 8], [8, 8]]]
    names = os.listdir(path="./snake/resources/scripts")
    for i in names:
        if str(i) == game_hash:
            players = os.listdir(f"./snake/resources/scripts/{i}")
            for pl in players:
                players_hash.append(players[count][0:-3])
                with open(f"./snake/resources/scripts/{i}/{pl}", "r", encoding="utf-8") as file:
                    code = file.read()
                snake_controls.direction = 3
                snake_controls.predict = [0, 0, 0, 0]
                snake_controls.code = code
                snake_controls.snake_position = copy.deepcopy(snake[count])
                snake_controls.apples_arr = [[7, 2], [2, 2], [2, 7], [7, 7]]
                snake_controls.direction = 1
                snake_controls.height = 10
                snake_controls.weight = 10
                snake_controls.rad = 2
                snake_controls.server_info = []
                game_map = snake_controls.start_options(
                    snake_controls.apples_arr)
                snake_controls.map_1 = game_map
                snake_controls.wall = snake_controls.map_gen()
                snake_controls.game_hash = game_hash
                snake_controls.all_food, snake_controls.all_walls\
                    = snake_controls.ai_start(snake_controls.apples_arr,
                                              snake_controls.wall)
                snake_controls.final()
                count += 1
                print("-----------\n")


if __name__ == '__main__':
    simulation('123456789')
