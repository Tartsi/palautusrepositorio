class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.temp_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def __handle_tie_situation(self, score: int):

        if score == 0:
            return "Love-All"
        elif score == 1:
            return "Fifteen-All"
        elif score == 2:
            return "Thirty-All"
        else:
            return "Deuce"

    def __handle_tiebreak_situation(self, score_difference: int):

        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def __handle_normal_game_status(self, score_str: str):

        if self.temp_score == 0:
            return score_str + "Love"
        elif self.temp_score == 1:
            return score_str + "Fifteen"
        elif self.temp_score == 2:
            return score_str + "Thirty"
        elif self.temp_score == 3:
            return score_str + "Forty"

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            score = self.__handle_tie_situation(self.player1_score)
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.__handle_tiebreak_situation(
                self.player1_score-self.player2_score)
        else:
            for i in range(1, 3):
                if i == 1:
                    self.temp_score = self.player1_score
                    score = self.__handle_normal_game_status(score)
                else:
                    score = score + "-"
                    self.temp_score = self.player2_score
                    score = self.__handle_normal_game_status(score)

        return score
