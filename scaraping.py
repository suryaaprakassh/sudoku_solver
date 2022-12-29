from bs4 import BeautifulSoup
import requests


def getBoard():
    board = []
    j = 0
    temp = []
    url = "https://websudoku.com/"
    doc = requests.get(url)
    soup = BeautifulSoup(doc.text, "html.parser")
    data = soup.find("frame")
    question_url = data["src"]
    sudoku_page_raw = requests.get(question_url)
    sudoku_page = BeautifulSoup(sudoku_page_raw.text, "html.parser")
    sudoku_table = sudoku_page.select("#puzzle_grid td input")
    for i in sudoku_table:
        j += 1
        temp.append(int(i.get("value", 0)))
        if j == 9:
            j = 0
            board.append(temp.copy())
            temp = []
    return board


def main():
    print("import scraping to use this module")


if __name__ == "__main__":
    main()
