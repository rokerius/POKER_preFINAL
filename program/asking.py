

class Replies(object):
    def __init__(self):
        self.answer = None
        self.app_players = 0
        self.app_sb = 0
        self.app_bb = 0
        self.app_startchips = 0

    def ask_start_info(self):
        self.app_players = input("Введите игроков через пробел:").split()
        self.app_startchips = int(input("Стартовое колличество фишек:"))
        self.app_sb = int(input("Малый блайнд:"))

    def end_ask(self):
        ans = input("Заново?")
        if ans.lower() == "да" or ans.lower() == "yes":
            return True
        return False

    def ask_responce(self):
        ans = input("Ваше действие?")
        return ans

    def ask_ri(self):
        return int(input("Сколько ставим?"))





