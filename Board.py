from Field import Field
import Game


class Board:
    def __init__(self, game):

        # Fields, 1 = White Empty piece, 2 = White Half piece, 3 = White Full piece
        #         4 = Black Empty piece, 5 = Black Half piece, 6 = Black Full piece
        self.a1 = Field(game, self, 4, 175, 520)  # 4
        self.a2 = Field(game, self, 4, 175, 440)  # 4
        self.a3 = Field(game, self, 4, 175, 360)  # 4
        self.a4 = Field(game, self, 4, 175, 280)  # 4
        self.a5 = Field(game, self, 1, 175, 200)  # 1
        self.b1 = Field(game, self, 1, 245, 560)  # 1
        self.b2 = Field(game, self, 5, 245, 480)  # 5
        self.b3 = Field(game, self, 5, 245, 400)  # 5
        self.b4 = Field(game, self, 5, 245, 320)  # 5
        self.b5 = Field(game, self, 2, 245, 235)  # 2
        self.b6 = Field(game, self, 1, 245, 155)  # 1
        self.c1 = Field(game, self, 1, 315, 600)  # 1
        self.c2 = Field(game, self, 2, 315, 520)  # 2
        self.c3 = Field(game, self, 6, 315, 440)  # 6
        self.c4 = Field(game, self, 6, 315, 360)  # 6
        self.c5 = Field(game, self, 3, 315, 275)  # 3
        self.c6 = Field(game, self, 2, 315, 195)  # 2
        self.c7 = Field(game, self, 1, 315, 115)  # 1
        self.d1 = Field(game, self, 1, 385, 640)  # 1
        self.d2 = Field(game, self, 2, 385, 565)  # 2
        self.d3 = Field(game, self, 3, 385, 480)  # 3
        self.d4 = Field(game, self, 4, 385, 400)  # 4
        self.d5 = Field(game, self, 1, 385, 320)  # 1
        self.d6 = Field(game, self, 3, 385, 235)  # 3
        self.d7 = Field(game, self, 2, 385, 155)  # 2
        self.d8 = Field(game, self, 1, 385, 75)  # 1
        self.e1 = Field(game, self, 1, 455, 680)  # 1
        self.e2 = Field(game, self, 2, 455, 600)  # 2
        self.e3 = Field(game, self, 3, 455, 520)  # 3
        self.e4 = Field(game, self, 1, 455, 440)  # 1
        self.e5 = Field(game, self, 4, 455, 275)  # 4
        self.e6 = Field(game, self, 6, 455, 195)  # 6
        self.e7 = Field(game, self, 5, 455, 115)  # 5
        self.e8 = Field(game, self, 4, 455, 35)  # 4
        self.f1 = Field(game, self, 4, 530, 640)  # 4
        self.f2 = Field(game, self, 5, 530, 565)  # 5
        self.f3 = Field(game, self, 6, 530, 485)  # 6
        self.f4 = Field(game, self, 4, 530, 400)  # 4
        self.f5 = Field(game, self, 1, 530, 315)  # 1
        self.f6 = Field(game, self, 6, 530, 235)  # 6
        self.f7 = Field(game, self, 5, 530, 155)  # 5
        self.f8 = Field(game, self, 4, 530, 70)  # 4
        self.g1 = Field(game, self, 4, 600, 600)  # 4
        self.g2 = Field(game, self, 5, 600, 520)  # 5
        self.g3 = Field(game, self, 6, 600, 440)  # 6
        self.g4 = Field(game, self, 3, 600, 360)  # 3
        self.g5 = Field(game, self, 3, 600, 275)  # 3
        self.g6 = Field(game, self, 5, 600, 195)  # 5
        self.g7 = Field(game, self, 4, 600, 110)  # 4
        self.h1 = Field(game, self, 4, 670, 560)  # 4
        self.h2 = Field(game, self, 5, 670, 480)  # 4
        self.h3 = Field(game, self, 2, 670, 400)  # 2
        self.h4 = Field(game, self, 2, 670, 315)  # 2
        self.h5 = Field(game, self, 2, 670, 235)  # 2
        self.h6 = Field(game, self, 4, 670, 155)  # 4
        self.i1 = Field(game, self, 4, 740, 520)  # 4
        self.i2 = Field(game, self, 1, 740, 440)  # 1
        self.i3 = Field(game, self, 1, 740, 360)  # 1
        self.i4 = Field(game, self, 1, 740, 275)  # 1
        self.i5 = Field(game, self, 1, 740, 195)  # 1

        # field dictionary = fd
        self.fd = {"e8": self.e8, "d8": self.d8, "f8": self.f8, "c7": self.c7, "e7": self.e7,
                   "g7": self.g7, "b6": self.b6, "d7": self.d7, "f7": self.f7, "h6": self.h6,
                   "a5": self.a5, "c6": self.c6, "e6": self.e6, "g6": self.g6, "i5": self.i5,
                   "b5": self.b5, "d6": self.d6, "f6": self.f6, "h5": self.h5, "a4": self.a4,
                   "c5": self.c5, "e5": self.e5, "g5": self.g5, "i4": self.i4, "b4": self.b4,
                   "d5": self.d5, "f5": self.f5, "h4": self.h4, "a3": self.a3, "c4": self.c4,
                   "g4": self.g4, "i3": self.i3, "b3": self.b3, "d4": self.d4, "f4": self.f4,
                   "h3": self.h3, "a2": self.a2, "c3": self.c3, "e4": self.e4, "g3": self.g3,
                   "i2": self.i2, "b2": self.b2, "d3": self.d3, "f3": self.f3, "h2": self.h2,
                   "a1": self.a1, "c2": self.c2, "e3": self.e3, "g2": self.g2, "i1": self.i1,
                   "b1": self.b1, "d2": self.d2, "f2": self.f2, "h1": self.h1, "c1": self.c1,
                   "e2": self.e2, "g1": self.g1, "d1": self.d1, "f1": self.f1, "e1": self.e1
                   }
        self.fd_keys = list(self.fd.keys())
        self.fd_values = list(self.fd.values())
        # So there will be no more bugs with the stacked images
        self.reversed_fd = dict(reversed(list(self.fd.items())))

        # Test Dictionary
        self.td = {"e8": self.e8, "d8": self.d8, "f8": self.f8, "c7": self.c7, "e7": self.e7,
                   "g7": self.g7, "b6": self.b6, "d7": self.d7, "f7": self.f7, "h6": self.h6,
                   "a5": self.a5, "c6": self.c6, "e6": self.e6, "g6": self.g6, "i5": self.i5,
                   "b5": self.b5, "d6": self.d6, "f6": self.f6, "h5": self.h5, "a4": self.a4,
                   "c5": self.c5, "e5": self.e5, "g5": self.g5, "i4": self.i4, "b4": self.b4,
                   "d5": self.d5, "f5": self.f5, "h4": self.h4, "a3": self.a3, "c4": self.c4,
                   "g4": self.g4, "i3": self.i3, "b3": self.b3, "d4": self.d4, "f4": self.f4,
                   "h3": self.h3, "a2": self.a2, "c3": self.c3, "e4": self.e4, "g3": self.g3,
                   "i2": self.i2, "b2": self.b2, "d3": self.d3, "f3": self.f3, "h2": self.h2,
                   "a1": self.a1, "c2": self.c2, "e3": self.e3, "g2": self.g2, "i1": self.i1,
                   "b1": self.b1, "d2": self.d2, "f2": self.f2, "h1": self.h1, "c1": self.c1,
                   "e2": self.e2, "g1": self.g1, "d1": self.d1, "f1": self.f1, "e1": self.e1
                   }

    def check_different_color(self, color, selected_piece, marked_piece):
        # Checks if the color of the selected piece (red) is not the same as the color of the marked piece (green)
        # 1 = Check selected piece is white and marked is blue
        if color == 1:
            return self.fd[marked_piece].gaming_piece != 1 \
                   and self.fd[marked_piece].gaming_piece != 2 \
                   and self.fd[marked_piece].gaming_piece != 3 \
                   and self.fd[selected_piece].gaming_piece != 4 \
                   and self.fd[selected_piece].gaming_piece != 5 \
                   and self.fd[selected_piece].gaming_piece != 6
        # 2 = Check selected piece is blue and marked is white
        elif color == 2:
            return self.fd[marked_piece].gaming_piece != 4 \
                   and self.fd[marked_piece].gaming_piece != 5 \
                   and self.fd[marked_piece].gaming_piece != 6 \
                   and self.fd[selected_piece].gaming_piece != 1 \
                   and self.fd[selected_piece].gaming_piece != 2 \
                   and self.fd[selected_piece].gaming_piece != 3

    def check_stack_lvl(self, selected_piece, marked_piece):
        return self.fd[selected_piece].stack_lvl >= self.fd[marked_piece].stack_lvl

    def check_same_color(self, color, selected_piece, marked_piece):
        # 1 = Check if color of selected and marked piece is white
        if color == 1:
            return self.fd[marked_piece]. gaming_piece != 4 \
                   and self.fd[marked_piece].gaming_piece != 5 \
                   and self.fd[marked_piece].gaming_piece != 6 \
                   and self.fd[selected_piece].gaming_piece != 4 \
                   and self.fd[selected_piece].gaming_piece != 5 \
                   and self.fd[selected_piece].gaming_piece != 6
        # 2 = Check if color of selected and marked piece is blue
        if color == 2:
            return self.fd[marked_piece].gaming_piece != 1 \
                   and self.fd[marked_piece].gaming_piece != 2 \
                   and self.fd[marked_piece].gaming_piece != 3 \
                   and self.fd[selected_piece].gaming_piece != 1 \
                   and self.fd[selected_piece].gaming_piece != 2 \
                   and self.fd[selected_piece].gaming_piece != 3

    def check_white(self, key):
        return self.fd[key].gaming_piece != 4 and self.fd[key].gaming_piece != 5 and self.fd[key].gaming_piece != 6
