# Candy Crush Super

This is a simple match-3 game inspired by Candy Crush, built with plain HTML, CSS, and JavaScript.

## How to Play

1.  **Open `index.html` in your web browser.**
2.  **Select a difficulty:**
    *   **Easy:** 5x5 grid, 3 colors, 500 score goal.
    *   **Hard:** 7x7 grid, 5 colors, 1000 score goal.
3.  **Swap adjacent candies** to create a line of 3 or more of the same color.
4.  Matched candies will be cleared, and new candies will fall from the top.
5.  Matching 4 or more candies creates a **Super Candy**.
6.  Matching a Super Candy will clear its entire row and column.
7.  Reach the target score to win the game!

## Setup

The game uses sound files that are not included in the repository. You can generate them using the provided Python script.

### Prerequisites

*   Python 3
*   `pip` (Python package installer)

### Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ssrtist/candy.git
    cd candy
    ```

2.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Generate the sound files:**
    ```bash
    python generate_sounds.py
    ```

4.  **Open `index.html` in your web browser to play the game.**

## Technologies Used

*   HTML
*   CSS
*   JavaScript
*   Python (`gTTS` library for sound generation)
