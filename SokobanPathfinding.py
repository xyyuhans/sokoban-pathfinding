import sys


class SokobanPathfinding:

	_MAP_INPUTS = {	"free_space": ' ',
					"wall": "#",
					"goal": ".",
					"player": "@",
					"player_on_goal": "+",
					"box": "$",
					"box_on_goal": "*"}

	_SUCCESS = 1
	_FAIL = -1

	def __init__(self):
		self._start_row = 0
		self._start_col = 0
		
		# add variables for goal locations? or something like that?

		self._on_goal = False

		self._map = []

	def read_map(self, file_name) -> int:
		"""
		Function that reads in a map from a .txt file
		"""
		curr_row = 0
		curr_col = 0

		start_found = False
		on_goal = self._on_goal

		# open map file and read it
		with open(file_name, "r") as f:
			for line in f:
				# add a row to the map matrix
				self._map.append([])
				# read the row's columns
				for c in line:
					# determine if player is already in goal
					if not on_goal:
						if c == self._MAP_INPUTS["player_on_goal"]:
							self._on_goal = True
					if not start_found:
						# update starting position
						if c == self._MAP_INPUTS["player"]:
							self._row_cord = curr_row
							self._col_cord = curr_col
							start_found = True
					# ignore newlines
					if c == "\n":
						break
					else:
						# add column to the row
						self._map[curr_row].append(c)
						# move to the next column
						curr_col += 1
				# move to the next row
				curr_row += 1

		return self._SUCCESS

	def print_map(self) -> int:
		"""
		Function that prints the inputted map.
		"""
		for row in self._map:
			# print all values of each row in the map matrix
			print("".join(row))
		return self._SUCCESS


if __name__ == "__main__":
	sb = SokobanPathfinding()
	sb.read_map(sys.argv[1])
	sb.print_map()
