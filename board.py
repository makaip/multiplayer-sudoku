import puzzle_loader as pl
import copy


class Board:
    def __init__(self):
        self.pencil_board: list[str] = ["" for _ in range(81)]
        self.board, self.correct_board = pl.get_random_puzzle()
        self.original_board = copy.deepcopy(self.board)
        
        print(f"Generated board: {self.board}, Correct board: {self.correct_board}")
    
    def update_from_request(self, request) -> None:
        """
        Update the board from a request. Mutates the current board. Assumes the request is already sanitized (i.e.,
        correct data types, correct keys, etc.)
        
        :param request: A request, containing the loc and value keys
        """

        self.pencil_board[request["loc"]] = ""
        self.board[request["loc"]] = request["value"]

    def pencil_mark(self, message: dict) -> None:
        """
        Pencil mark a location on the board. Mutates the pencil_marks list. Assumes the message is already sanitized.

        :param message: A message containing the loc and value keys
        """

        self.pencil_board[message["loc"]] = message["value"]

    def get_init_data(self):
        """
        Get the initialization data for a client
        :return: The initial board, the correct board, and the pencil marks
        """

        return {
            "originalBoard": copy.deepcopy(self.original_board),
            "correctBoard": copy.deepcopy(self.correct_board),
            "currentBoard": copy.deepcopy(self.board),
            "pencilBoard": copy.deepcopy(self.pencil_board)
        }
    