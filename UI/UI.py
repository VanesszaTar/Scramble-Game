from domain.domain import ScrambleGame

class ScrambleController:
    def __init__(self, repo):
        self.repo = repo

    def start(self):
        sentence = self.repo.getRandomSentence()
        game = ScrambleGame(sentence)

        print("Welcome to SCRAMBLE!")
        print("Original sentence scrambled:")
        print(" ".join(game.scrambled))
        print("Score:", game.score)
        print("--------------------------------")

        while True:
            print("\nCurrent:", " ".join(game.scrambled))
            print("Score:", game.score)

            if game.score <= 0:
                print("\nYou lost! Score reached 0.")
                print("Correct sentence was:", " ".join(game.original))
                return

            if game.is_solved():
                print("\n🎉 You WON! 🎉")
                print("Solved:", " ".join(game.scrambled))
                print("Your final score:", game.score)
                return

            command = input("> ").strip().lower()

            if command == "quit":
                print("Goodbye!")
                return

            if command == "undo":
                game.undo()
                continue

            if command.startswith("swap"):
                parts = command.split()
                if len(parts) != 5:
                    print("Format: swap <word> <letter> <word> <letter>")
                    continue

                _, w1, l1, w2, l2 = parts

                try:
                    wi1 = int(w1) - 1
                    li1 = int(l1) - 1
                    wi2 = int(w2) - 1
                    li2 = int(l2) - 1
                except ValueError:
                    print("Indices must be numbers.")
                    continue

                game.swap(wi1, li1, wi2, li2)
                continue

            print("Unknown command. Use swap / undo / quit.")