letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_point = {}
letter_to_point[" "] = 0

for i in range(len(letters)):
    letter_to_point[letters[i]] = points[i]

print(letter_to_point)



def score_word(word):
    point_total = 0
    for letter in range(len(word)):
        point_total += letter_to_point[word[letter]]
    print(point_total)
    return point_total

# test 1
score_word("BROWNIE")

player_to_words = {"player1" : ["BLUE", "TENNIS", "EXIT"], "wordNerd" : ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

for player in player_to_words:
    player_points = 0
    for word in player_to_words[player]:
        player_points += score_word(word)
    player_to_points[player] = player_points

print(player_to_points)
