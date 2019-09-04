import random

result_list = [
    (['{:^6}{:^8}{:^10}{:^16}{:^18}{:^10}'.format("Game", "Word", "Status", "Bad Guesses", "Missed Letters", "Score")]),
    '--------------------------------------------------------------------']

'''Declare the dictionary which holds the frequency distribution information
about english alphabets'''
frequency_dist = {'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.23, 'g': 2.20, 'h': 6.09,
                  'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93, 'q': 0.1,
                  'r': 5.99, 's': 6.33, 't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97, 'z': 0.07}
word_list = []
file = open("four_letters.txt", 'r')
for line in file:
    for word in line.split():
        word_list.append(word)


class game1:
    def __init__(self):
        self.start_game = True
        self.game_number = 0
        self.game_status = ""
        self.total_game_score = 0
        self.total_letter_guesses = 0
        self.bad_guess_number = 0
        self.missed_letters = 4
        self.game_score = 0
        self.continue_game = True
        self.exact_4letters = True
        self.exact_1letter = True
        self.update_guess = ''
        self.current_guess = '----'
        self.current_ans = random.choice(word_list)

    def word(self, current_ans, continue_game, game_status, current_guess):
        self.exact_4letters = True
        print('please guess the whole word')

        while self.exact_4letters:
            guess_word = input().lower()
            if len(guess_word) == 4:
                self.exact_4letters = False
                if self.current_ans == guess_word:
                    print('ohh congrats..you guessed correct one--great')
                    self.continue_game = False
                    self.game_status = 'success'
                    for i in range(4):
                        self.game_score += frequency_dist[self.current_ans[i]]
                        print('game score is incremented for',i,'letter bcz its not guessed yet: ', self.game_score)
                        if self.current_ans[i] == self.current_guess[i]:
                            self.game_score -= frequency_dist[self.current_guess[i]]
                            print('sorry...game score is decremented because',i,' letter is already guessed: ', self.game_score)
                    print('the final game score: ', self.game_score)
                else:
                    print('sorry..you entered wrong word..better luck next time')
                    self.continue_game = False
                    self.game_status = 'last'
                    for i in range(4):
                        self.game_score += frequency_dist[self.current_ans[i]]
                    self.game_score -= self.game_score * 1.1
                    print('opps..wrong guess will cost you 10% total score of the current word..sorry: ', self.game_score)
            else:
                print('please enter only 4 letters my dear')

    def letter1(self, total_letter_guesses, current_ans, current_guess, missed_letters, continue_game, game_status,
                bad_guess_number):
        self.update_guess = ''
        print('please guess by single letter')
        self.exact_1letter = True
        self.total_letter_guesses += 1
        while self.exact_1letter:
            guess_letter = input().lower()
            if len(guess_letter) == 1:
                self.exact_1letter = False
                if guess_letter in self.current_ans and guess_letter not in self.current_guess:
                    print('congrats.. you pick correct letter')
                    for i in range(4):
                        if guess_letter == self.current_ans[i]:
                            self.update_guess = self.update_guess + guess_letter
                            self.missed_letters -= 1
                        else:
                            self.update_guess = self.update_guess + self.current_guess[i]
                    print('no of missed letters after this round: ', self.missed_letters)
                    self.current_guess = self.update_guess
                    print(self.current_guess)
                    if self.current_ans == self.current_guess:
                        print('ohh.. congrats you guessed all 4 letters exactly')
                        self.continue_game = False
                        self.game_status = 'success'
                        for i in range(4):
                            self.game_score += frequency_dist[self.current_ans[i]]
                        print('actual game score: ', self.game_score)
                        self.game_score -= self.total_letter_guesses
                        print('sorry..but game score reduced by total no. of guesses required(',self.total_letter_guesses,')for this game: ', self.game_score)
                elif guess_letter in self.current_ans and guess_letter in self.current_guess:
                    print('this letter has already chosen--please choose another letter')
                else:
                    print('sorry you made a wrong guess--try again')
                    self.bad_guess_number += 1
            else:
                print('please guess by only letter')

    def tellme(self, game_status, continue_game, current_ans, current_guess):
        print('dear you last the game the correct ans is : ' + current_ans)
        self.game_status = 'gave up'
        self.continue_game = False
        for i in range(4):
            self.game_score -= frequency_dist[self.current_ans[i]]
            print('game score is decremented in ', i,' round: ', self.game_score)
            if self.current_ans[i] == self.current_guess[i]:
                self.game_score += frequency_dist[self.current_guess[i]]
                print('game score is incremented because of', i, 'letter already guessed: ', self.game_score)
        print('But you will get score for already guessed letters: ', self.game_score)

    def quit(self, continue_game, start_game, total_game_score):
        print('Do you want to exit from the game')
        print('YES or NO')
        ans = input().lower()
        if ans == 'yes':
            self.continue_game = False
            self.start_game = False
            for i in result_list:
                print(i)
            print('total game score=', self.total_game_score)
        else:
            print('continue the game')

    def main(self):
        self.start_game = True
        self.game_number = 0
        self.game_status = ""
        self.total_game_score = 0
        # current_ans = "anal"
        print('**The great guessing game**')
        print('g - for guessing the whole word')
        print('l - for guess letter by letter')
        print('t - for know the answer')
        print('q - for quiting the game')

        while self.start_game:
            self.current_ans = random.choice(word_list)
            print(self.current_ans)
            self.current_guess = "----"
            print(self.current_guess)
            self.game_number += 1
            self.total_letter_guesses = 0
            self.bad_guess_number = 0
            self.missed_letters = 4
            self.game_score = 0
            print(self.game_number)
            self.continue_game = True
            while self.continue_game:
                print('choose the current guess option')
                guess_option = input().lower()
                if guess_option == 'g':
                    self.word(self.current_ans, self.continue_game, self.game_status, self.current_guess)

                elif guess_option == 'l':
                    self.letter1(self.total_letter_guesses, self.current_ans, self.current_guess, self.missed_letters,
                                 self.continue_game,
                                 self.game_status, self.bad_guess_number)

                elif guess_option == 't':
                    self.tellme(self.game_status, self.continue_game, self.current_ans, self.current_guess)

                elif guess_option == 'q':
                    self.quit(self.continue_game, self.start_game, self.total_game_score)

                else:
                    print('invalid input')
            #print("game_status: ", self.game_status)
            #print('number of bad guess attempts : ', self.bad_guess_number)
            result_list.append(([
                '{:^6}{:^8}{:^10}{:^16}{:^18}{:^10}'.format(self.game_number, self.current_ans, self.game_status,
                                                            self.bad_guess_number,
                                                            self.missed_letters, self.game_score)]))
            self.total_game_score += self.game_score


o1 = game1()
o1.main()