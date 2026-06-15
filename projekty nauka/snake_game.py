import sys
import random

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor, QFont, QKeyEvent
from PyQt5.QtCore import Qt, QTimer, QRect

CELL = 20
WIDTH = 25
HEIGHT = 20
SPEED = 100  # ms


class SnakeWidget(QWidget):
    def __init__(self, score_label):
        super().__init__()
        self.score_label = score_label
        self.setFixedSize(WIDTH * CELL, HEIGHT * CELL)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.game_loop)

        self.reset()

    def reset(self):
        self.snake = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.food = self.new_food()
        self.score = 0
        self.game_over = False
        self.update_score_label()
        self.timer.start(SPEED)
        self.update()

    def new_food(self):
        while True:
            pos = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
            if pos not in self.snake:
                return pos

    def update_score_label(self):
        self.score_label.setText(f"Wynik: {self.score}")

    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        dx, dy = self.direction

        if key in (Qt.Key.Key_Up, Qt.Key.Key_W) and dy != 1:
            self.next_direction = (0, -1)
        elif key in (Qt.Key.Key_Down, Qt.Key.Key_S) and dy != -1:
            self.next_direction = (0, 1)
        elif key in (Qt.Key.Key_Left, Qt.Key.Key_A) and dx != 1:
            self.next_direction = (-1, 0)
        elif key in (Qt.Key.Key_Right, Qt.Key.Key_D) and dx != -1:
            self.next_direction = (1, 0)
        elif key == Qt.Key.Key_Space and self.game_over:
            self.reset()

    def game_loop(self):
        if not self.game_over:
            self.move()
        self.update()

    def move(self):
        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        if (
            new_head[0] < 0
            or new_head[0] >= WIDTH
            or new_head[1] < 0
            or new_head[1] >= HEIGHT
            or new_head in self.snake
        ):
            self.game_over = True
            self.timer.stop()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.update_score_label()
            self.food = self.new_food()
        else:
            self.snake.pop()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor("black"))

        # Snake
        painter.setBrush(QColor("green"))
        painter.setPen(QColor("darkGreen"))
        for x, y in self.snake:
            painter.drawRect(QRect(x * CELL, y * CELL, CELL, CELL))

        # Food
        painter.setBrush(QColor("red"))
        painter.setPen(QColor("red"))
        fx, fy = self.food
        painter.drawEllipse(QRect(fx * CELL, fy * CELL, CELL, CELL))

        # Game over overlay
        if self.game_over:
            painter.setPen(QColor("white"))
            painter.setFont(QFont("Arial", 16))
            painter.drawText(
                self.rect(),
                Qt.AlignmentFlag.AlignCenter,
                "GAME OVER\nNacisnij SPACJE aby zagrac ponownie",
            )


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snake")

        central = QWidget()
        layout = QVBoxLayout(central)

        self.score_label = QLabel("Wynik: 0")
        self.score_label.setStyleSheet("color: white; font-size: 14px; padding: 4px;")
        layout.addWidget(self.score_label)

        self.game = SnakeWidget(self.score_label)
        layout.addWidget(self.game)

        central.setStyleSheet("background-color: #222;")
        self.setCentralWidget(central)
        self.game.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())