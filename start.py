from Repository.Repository import SentenceRepository
from UI.UI import ScrambleController

if __name__ == "__main__":
    repo = SentenceRepository("input.txt")
    controller = ScrambleController(repo)
    controller.start()
