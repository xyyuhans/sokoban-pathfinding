import sys


class SokobanPathfinding:

    _MAP_INPUTS = {
        "free_space": " ",
        "wall": "#",
        "goal": ".",
        "player": "@",
        "player_on_goal": "+",
        "box": "$",
        "box_on_goal": "*",
    }

    def __init__(self):
        self._map = []
        self._position = [0, 0]
        self._answer = []
        self._end = False

    def read_map(self, file_name):
        """
        Function that reads in a map from a .txt file
        """
        with open(file_name) as f:
            lines = f.readlines()
        for line in lines:
            line = line.replace("$", "#")
            self._map.append(line[:-1])

    def find_player(self):
        for idx, i in enumerate(self._map):
            if self._MAP_INPUTS["player"] in i:
                self._position[0] = idx
                self._position[1] = i.index(self._MAP_INPUTS["player"])

    def print_map(self):
        """
        Function that prints the inputted map.
        """
        for row in self._map:
            # print all values of each row in the map matrix
            print(row)

    def edit_map(self, position, value):
        s = list(self._map[position[0]])
        s[position[1]] = value
        self._map[position[0]] = "".join(s)

    def player_move(self, direction):
        self.edit_map(self._position, self._MAP_INPUTS["free_space"])
        next_position = self._position
        if direction == "u":
            next_position[0] -= 1
        elif direction == "d":
            next_position[0] += 1
        elif direction == "l":
            next_position[1] -= 1
        elif direction == "r":
            next_position[1] += 1

        if self._map[next_position[0]][next_position[1]] == self._MAP_INPUTS["goal"]:
            self._end = True
        else:
            self.edit_map(next_position, self._MAP_INPUTS["player"])

    def next_map(self):
        while self._end == False:
            if (
                self._map[self._position[0] - 1][self._position[1]]
                != self._MAP_INPUTS["wall"]
            ):
                self.player_move("u")
                self._answer.append("u")
            elif (
                self._map[self._position[0]][self._position[1] + 1]
                != self._MAP_INPUTS["wall"]
            ):
                self.player_move("r")
                self._answer.append("r")
            elif (
                self._map[self._position[0] + 1][self._position[1]]
                != self._MAP_INPUTS["wall"]
            ):
                self.player_move("d")
                self._answer.append("d")
            elif (
                self._map[self._position[0]][self._position[1] - 1]
                != self._MAP_INPUTS["wall"]
            ):
                self.player_move("l")
                self._answer.append("l")
            self.print_map()
        print(self._answer)


if __name__ == "__main__":
    sb = SokobanPathfinding()
    sb.read_map(sys.argv[1])
    sb.print_map()
    sb.find_player()
    sb.next_map()
