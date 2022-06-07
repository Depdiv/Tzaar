import pygame as py


class Field:

    def __init__(self, game, board, gaming_piece, x, y, stack_lvl=1):
        self.game = game
        self.board = board
        self.gaming_piece = gaming_piece
        self.stack_lvl = stack_lvl
        self.x = x
        self.y = y
        self.marked = False
        self.selected = False
        self.hb_size = 65  # The size of the hitbox -> (x + 65, y + 65)
        # White Empty Pieces
        self.we1_img = py.image.load("img/we1.png")
        self.we1_s_img = py.image.load("img/we1_s.png")
        self.we1_m_img = py.image.load("img/we1_m.png")
        self.we2_img = py.image.load("img/we2.png")
        self.we2_s_img = py.image.load("img/we2_s.png")
        self.we2_m_img = py.image.load("img/we2_m.png")
        self.we3_img = py.image.load("img/we3.png")
        self.we3_s_img = py.image.load("img/we3_s.png")
        self.we3_m_img = py.image.load("img/we3_m.png")
        self.we4_img = py.image.load("img/we4.png")
        self.we4_s_img = py.image.load("img/we4_s.png")
        self.we4_m_img = py.image.load("img/we4_m.png")
        self.we5_img = py.image.load("img/we5.png")
        self.we5_s_img = py.image.load("img/we5_s.png")
        self.we5_m_img = py.image.load("img/we5_m.png")
        # White Half Piecesimg/
        self.wh1_img = py.image.load("img/wh1.png")
        self.wh1_s_img = py.image.load("img/wh1_s.png")
        self.wh1_m_img = py.image.load("img/wh1_m.png")
        self.wh2_img = py.image.load("img/wh2.png")
        self.wh2_s_img = py.image.load("img/wh2_s.png")
        self.wh2_m_img = py.image.load("img/wh2_m.png")
        self.wh3_img = py.image.load("img/wh3.png")
        self.wh3_s_img = py.image.load("img/wh3_s.png")
        self.wh3_m_img = py.image.load("img/wh3_m.png")
        self.wh4_img = py.image.load("img/wh4.png")
        self.wh4_s_img = py.image.load("img/wh4_s.png")
        self.wh4_m_img = py.image.load("img/wh4_m.png")
        self.wh5_img = py.image.load("img/wh5.png")
        self.wh5_s_img = py.image.load("img/wh5_s.png")
        self.wh5_m_img = py.image.load("img/wh5_m.png")
        # White Full Piecesimg/
        self.wf1_img = py.image.load("img/wf1.png")
        self.wf1_s_img = py.image.load("img/wf1_s.png")
        self.wf1_m_img = py.image.load("img/wf1_m.png")
        self.wf2_img = py.image.load("img/wf2.png")
        self.wf2_s_img = py.image.load("img/wf2_s.png")
        self.wf2_m_img = py.image.load("img/wf2_m.png")
        self.wf3_img = py.image.load("img/wf3.png")
        self.wf3_s_img = py.image.load("img/wf3_s.png")
        self.wf3_m_img = py.image.load("img/wf3_m.png")
        self.wf4_img = py.image.load("img/wf4.png")
        self.wf4_s_img = py.image.load("img/wf4_s.png")
        self.wf4_m_img = py.image.load("img/wf4_m.png")
        self.wf5_img = py.image.load("img/wf5.png")
        self.wf5_s_img = py.image.load("img/wf5_s.png")
        self.wf5_m_img = py.image.load("img/wf5_m.png")
        # Blue Empty Piecesimg/
        self.be1_img = py.image.load("img/be1.png")
        self.be1_s_img = py.image.load("img/be1_s.png")
        self.be1_m_img = py.image.load("img/be1_m.png")
        self.be2_img = py.image.load("img/be2.png")
        self.be2_s_img = py.image.load("img/be2_s.png")
        self.be2_m_img = py.image.load("img/be2_m.png")
        self.be3_img = py.image.load("img/be3.png")
        self.be3_s_img = py.image.load("img/be3_s.png")
        self.be3_m_img = py.image.load("img/be3_m.png")
        self.be4_img = py.image.load("img/be4.png")
        self.be4_s_img = py.image.load("img/be4_s.png")
        self.be4_m_img = py.image.load("img/be4_m.png")
        self.be5_img = py.image.load("img/be5.png")
        self.be5_s_img = py.image.load("img/be5_s.png")
        self.be5_m_img = py.image.load("img/be5_m.png")
        self.be5_img = py.image.load("img/be5.png")
        self.be5_s_img = py.image.load("img/be5_s.png")
        self.be5_m_img = py.image.load("img/be5_m.png")

        # Blue Half Piecesimg/
        self.bh1_img = py.image.load("img/bh1.png")
        self.bh1_s_img = py.image.load("img/bh1_s.png")
        self.bh1_m_img = py.image.load("img/bh1_m.png")
        self.bh2_img = py.image.load("img/bh2.png")
        self.bh2_s_img = py.image.load("img/bh2_s.png")
        self.bh2_m_img = py.image.load("img/bh2_m.png")
        self.bh3_img = py.image.load("img/bh3.png")
        self.bh3_s_img = py.image.load("img/bh3_s.png")
        self.bh3_m_img = py.image.load("img/bh3_m.png")
        self.bh4_img = py.image.load("img/bh4.png")
        self.bh4_s_img = py.image.load("img/bh4_s.png")
        self.bh4_m_img = py.image.load("img/bh4_m.png")
        self.bh5_img = py.image.load("img/bh5.png")
        self.bh5_s_img = py.image.load("img/bh5_s.png")
        self.bh5_m_img = py.image.load("img/bh5_m.png")
        self.bh5_img = py.image.load("img/bh5.png")
        self.bh5_s_img = py.image.load("img/bh5_s.png")
        self.bh5_m_img = py.image.load("img/bh5_m.png")
        # Blue Full Piecesimg/
        self.bf1_img = py.image.load("img/bf1.png")
        self.bf1_s_img = py.image.load("img/bf1_s.png")
        self.bf1_m_img = py.image.load("img/bf1_m.png")
        self.bf2_img = py.image.load("img/bf2.png")
        self.bf2_s_img = py.image.load("img/bf2_s.png")
        self.bf2_m_img = py.image.load("img/bf2_m.png")
        self.bf3_img = py.image.load("img/bf3.png")
        self.bf3_s_img = py.image.load("img/bf3_s.png")
        self.bf3_m_img = py.image.load("img/bf3_m.png")
        self.bf4_img = py.image.load("img/bf4.png")
        self.bf4_s_img = py.image.load("img/bf4_s.png")
        self.bf4_m_img = py.image.load("img/bf4_m.png")
        self.bf5_img = py.image.load("img/bf5.png")
        self.bf5_s_img = py.image.load("img/bf5_s.png")
        self.bf5_m_img = py.image.load("img/bf5_m.png")
        self.bf5_img = py.image.load("img/bf5.png")
        self.bf5_s_img = py.image.load("img/bf5_s.png")
        self.bf5_m_img = py.image.load("img/bf5_m.png")

        # Piece image dictionary = pid
        self.pid = {"we1": self.we1_img, "wh1": self.wh1_img, "wf1": self.wf1_img,
                    "be1": self.be1_img, "bh1": self.bh1_img, "bf1": self.bf1_img,
                    "we2": self.we2_img, "wh2": self.wh2_img, "wf2": self.wf2_img,
                    "be2": self.be2_img, "bh2": self.bh2_img, "bf2": self.bf2_img,
                    "we3": self.we3_img, "wh3": self.wh3_img, "wf3": self.wf3_img,
                    "be3": self.be3_img, "bh3": self.bh3_img, "bf3": self.bf3_img,
                    "we4": self.we4_img, "wh4": self.wh4_img, "wf4": self.wf4_img,
                    "be4": self.be4_img, "bh4": self.bh4_img, "bf4": self.bf4_img,
                    "we5": self.we5_img, "wh5": self.wh5_img, "wf5": self.wf5_img,
                    "be5": self.be5_img, "bh5": self.bh5_img, "bf5": self.bf5_img
                    }
        self.pid_values = list(self.pid.values())

        # marked piece image dictionary = mpid
        self.mpid = {"we1": self.we1_m_img, "wh1": self.wh1_m_img, "wf1": self.wf1_m_img,
                     "be1": self.be1_m_img, "bh1": self.bh1_m_img, "bf1": self.bf1_m_img,
                     "we2": self.we2_m_img, "wh2": self.wh2_m_img, "wf2": self.wf2_m_img,
                     "be2": self.be2_m_img, "bh2": self.bh2_m_img, "bf2": self.bf2_m_img,
                     "we3": self.we3_m_img, "wh3": self.wh3_m_img, "wf3": self.wf3_m_img,
                     "be3": self.be3_m_img, "bh3": self.bh3_m_img, "bf3": self.bf3_m_img,
                     "we4": self.we4_m_img, "wh4": self.wh4_m_img, "wf4": self.wf4_m_img,
                     "be4": self.be4_m_img, "bh4": self.bh4_m_img, "bf4": self.bf4_m_img,
                     "we5": self.we5_m_img, "wh5": self.wh5_m_img, "wf5": self.wf5_m_img,
                     "be5": self.be5_m_img, "bh5": self.bh5_m_img, "bf5": self.bf5_m_img
                     }

        # mark possible moves with green color
        self.mpid_values = list(self.mpid.values())

        # selected piece image dictionary = spid
        self.spid = {"we1": self.we1_s_img, "wh1": self.wh1_s_img, "wf1": self.wf1_s_img,
                     "be1": self.be1_s_img, "bh1": self.bh1_s_img, "bf1": self.bf1_s_img,
                     "we2": self.we2_s_img, "wh2": self.wh2_s_img, "wf2": self.wf2_s_img,
                     "be2": self.be2_s_img, "bh2": self.bh2_s_img, "bf2": self.bf2_s_img,
                     "we3": self.we3_s_img, "wh3": self.wh3_s_img, "wf3": self.wf3_s_img,
                     "be3": self.be3_s_img, "bh3": self.bh3_s_img, "bf3": self.bf3_s_img,
                     "we4": self.we4_s_img, "wh4": self.wh4_s_img, "wf4": self.wf4_s_img,
                     "be4": self.be4_s_img, "bh4": self.bh4_s_img, "bf4": self.bf4_s_img,
                     "we5": self.we5_s_img, "wh5": self.wh5_s_img, "wf5": self.wf5_s_img,
                     "be5": self.be5_s_img, "bh5": self.bh5_s_img, "bf5": self.bf5_s_img
                     }
        self.spid_values = list(self.spid.values())

    # draw Fields content/stone and draw possible moves
    def update(self):
        # Starting position of the gaming pieces
        # Draws all pieces on the board and add a number if the stack is higher than 1
        stack_var = 6
        stack_y = 10
        for type_i in range(1, 7):
            # Stack level 1
            if self.gaming_piece == type_i and self.stack_lvl == 1:
                self.game.screen.blit(self.pid_values[type_i - 1], (self.x, self.y))
            # Stack level 2
            elif self.gaming_piece == type_i and self.stack_lvl == 2:
                self.game.screen.blit(self.pid_values[type_i - 1 + stack_var], (self.x, self.y - stack_y))
                # check if color is blue
                if self.gaming_piece != 1 and self.gaming_piece != 2 and self.gaming_piece != 3:
                    stack_font = py.font.Font("freesansbold.ttf", 25)
                    stack_text = stack_font.render(str(self.stack_lvl), True, (255, 255, 255))
                    self.game.screen.blit(stack_text, (self.x + 28, self.y + 27))
                # check if color is white
                else:
                    stack_font = py.font.Font("freesansbold.ttf", 25)
                    stack_text = stack_font.render(str(self.stack_lvl), True, (0, 0, 0))
                    self.game.screen.blit(stack_text, (self.x + 28, self.y + 27))
            # Stack level 3
            elif self.gaming_piece == type_i and self.stack_lvl == 3:
                self.game.screen.blit(self.pid_values[type_i - 1 + stack_var * (self.stack_lvl-1)],
                                      (self.x, self.y - stack_y))
                # check if color is blue
                if self.gaming_piece != 1 and self.gaming_piece != 2 and self.gaming_piece != 3:
                    stack_font = py.font.Font("freesansbold.ttf", 25)
                    stack_text = stack_font.render(str(self.stack_lvl), True, (255, 255, 255))
                    self.game.screen.blit(stack_text, (self.x + 28, self.y + 24))
                # check if color is white
                else:
                    stack_font = py.font.Font("freesansbold.ttf", 25)
                    stack_text = stack_font.render(str(self.stack_lvl), True, (0, 0, 0))
                    self.game.screen.blit(stack_text, (self.x + 28, self.y + 24))
            # Stack level 4
            elif self.gaming_piece == type_i and self.stack_lvl == 4:
                self.game.screen.blit(self.pid_values[type_i - 1 + stack_var * (self.stack_lvl-1)],
                                      (self.x, self.y - stack_y))
                # check if color is blue
                if self.gaming_piece != 1 and self.gaming_piece != 2 and self.gaming_piece != 3:
                    stack_font = py.font.Font("freesansbold.ttf", 25)
                    stack_text = stack_font.render(str(self.stack_lvl), True, (255, 255, 255))
                    self.game.screen.blit(stack_text, (self.x + 28, self.y + 19))
                # check if color is white
                else:
                    stack_font = py.font.Font("freesansbold.ttf", 25)
                    stack_text = stack_font.render(str(self.stack_lvl), True, (0, 0, 0))
                    self.game.screen.blit(stack_text, (self.x + 28, self.y + 19))
            # Stack level 5 or higher
            elif self.gaming_piece == type_i and self.stack_lvl >= 5:
                self.game.screen.blit(self.pid_values[type_i - 1 + stack_var * 4], (self.x, self.y - stack_y))
                # check if color is blue
                if self.gaming_piece != 1 and self.gaming_piece != 2 and self.gaming_piece != 3:
                    # check if stack level is lower than 10
                    if self.stack_lvl < 10:
                        stack_font = py.font.Font("freesansbold.ttf", 25)
                        stack_text = stack_font.render(str(self.stack_lvl), True, (255, 255, 255))
                        self.game.screen.blit(stack_text, (self.x + 28, self.y + 15))
                    # Stack level is 10 or higher
                    else:
                        stack_font = py.font.Font("freesansbold.ttf", 25)
                        stack_text = stack_font.render(str(self.stack_lvl), True, (255, 255, 255))
                        self.game.screen.blit(stack_text, (self.x + 20, self.y + 15))
                # check if color is white
                else:
                    # Stack level is lower than 10
                    if self.stack_lvl < 10:
                        stack_font = py.font.Font("freesansbold.ttf", 25)
                        stack_text = stack_font.render(str(self.stack_lvl), True, (0, 0, 0))
                        self.game.screen.blit(stack_text, (self.x + 28, self.y + 15))
                    # Stack level is 10 or higher
                    else:
                        stack_font = py.font.Font("freesansbold.ttf", 25)
                        stack_text = stack_font.render(str(self.stack_lvl), True, (0, 0, 0))
                        self.game.screen.blit(stack_text, (self.x + 20, self.y + 15))

        # Mark the selected piece with red color and add a number if the stack is higher than 1
        if self.selected is True:
            for type_i in range(1, 7):
                # Stack level 1
                if self.gaming_piece == type_i and self.stack_lvl == 1:
                    self.game.screen.blit(self.spid_values[type_i - 1], (self.x, self.y))
                # Stack level 2
                elif self.gaming_piece == type_i and self.stack_lvl == 2:
                    self.game.screen.blit(self.spid_values[type_i - 1 + stack_var], (self.x, self.y - stack_y))
                    # check if color is blue
                    if self.gaming_piece != 1 and self.gaming_piece != 2 and self.gaming_piece != 3:
                        stack_font = py.font.Font("freesansbold.ttf", 25)
                        stack_text = stack_font.render(str(self.stack_lvl), True, (255, 255, 255))
                        self.game.screen.blit(stack_text, (self.x + 28, self.y + 27))
                    # check if color is white
                    else:
                        stack_font = py.font.Font("freesansbold.ttf", 25)
                        stack_text = stack_font.render(str(self.stack_lvl), True, (0, 0, 0))
                        self.game.screen.blit(stack_text, (self.x + 28, self.y + 27))
                # Stack level 3
                elif self.gaming_piece == type_i and self.stack_lvl == 3:
                    self.game.screen.blit(self.spid_values[type_i - 1 + stack_var * (self.stack_lvl - 1)],
                                          (self.x, self.y - stack_y))
                    # check if color is blue
                    if self.gaming_piece != 1 and self.gaming_piece != 2 and self.gaming_piece != 3:
                        stack_font = py.font.Font("freesansbold.ttf", 25)
                        stack_text = stack_font.render(str(self.stack_lvl), True, (255, 255, 255))
                        self.game.screen.blit(stack_text, (self.x + 28, self.y + 24))
                    # check if color is white
                    else:
                        stack_font = py.font.Font("freesansbold.ttf", 25)
                        stack_text = stack_font.render(str(self.stack_lvl), True, (0, 0, 0))
                        self.game.screen.blit(stack_text, (self.x + 28, self.y + 24))
                # Stack level 4
                elif self.gaming_piece == type_i and self.stack_lvl == 4:
                    self.game.screen.blit(self.spid_values[type_i - 1 + stack_var * (self.stack_lvl - 1)],
                                          (self.x, self.y - stack_y))
                    # check if color is blue
                    if self.gaming_piece != 1 and self.gaming_piece != 2 and self.gaming_piece != 3:
                        stack_font = py.font.Font("freesansbold.ttf", 25)
                        stack_text = stack_font.render(str(self.stack_lvl), True, (255, 255, 255))
                        self.game.screen.blit(stack_text, (self.x + 28, self.y + 19))
                    # check if color is white
                    else:
                        stack_font = py.font.Font("freesansbold.ttf", 25)
                        stack_text = stack_font.render(str(self.stack_lvl), True, (0, 0, 0))
                        self.game.screen.blit(stack_text, (self.x + 28, self.y + 19))
                # Stack level 5 or higher
                elif self.gaming_piece == type_i and self.stack_lvl >= 5:
                    self.game.screen.blit(self.spid_values[type_i - 1 + stack_var * 4], (self.x, self.y - stack_y))
                    # check if color is blue
                    if self.gaming_piece != 1 and self.gaming_piece != 2 and self.gaming_piece != 3:
                        # check if stack level is lower than 10
                        if self.stack_lvl < 10:
                            stack_font = py.font.Font("freesansbold.ttf", 25)
                            stack_text = stack_font.render(str(self.stack_lvl), True, (255, 255, 255))
                            self.game.screen.blit(stack_text, (self.x + 28, self.y + 15))
                        # Stack level is 10 or higher
                        else:
                            stack_font = py.font.Font("freesansbold.ttf", 25)
                            stack_text = stack_font.render(str(self.stack_lvl), True, (255, 255, 255))
                            self.game.screen.blit(stack_text, (self.x + 20, self.y + 15))
                    # check if color is white
                    else:
                        # Stack level is lower than 10
                        if self.stack_lvl < 10:
                            stack_font = py.font.Font("freesansbold.ttf", 25)
                            stack_text = stack_font.render(str(self.stack_lvl), True, (0, 0, 0))
                            self.game.screen.blit(stack_text, (self.x + 28, self.y + 15))
                        # Stack level is 10 or higher
                        else:
                            stack_font = py.font.Font("freesansbold.ttf", 25)
                            stack_text = stack_font.render(str(self.stack_lvl), True, (0, 0, 0))
                            self.game.screen.blit(stack_text, (self.x + 20, self.y + 15))
        # Mark the marked pieces with green color and add a number if the stack is higher than 1
        if self.selected is False and self.marked is True:
            for type_i in range(1, 7):
                # Stack level 1
                if self.gaming_piece == type_i and self.stack_lvl == 1:
                    self.game.screen.blit(self.mpid_values[type_i - 1], (self.x, self.y))
                # Stack level 2
                elif self.gaming_piece == type_i and self.stack_lvl == 2:
                    self.game.screen.blit(self.mpid_values[type_i - 1 + stack_var], (self.x, self.y - stack_y))
                    # check if color is blue
                    if self.gaming_piece != 1 and self.gaming_piece != 2 and self.gaming_piece != 3:
                        stack_font = py.font.Font("freesansbold.ttf", 25)
                        stack_text = stack_font.render(str(self.stack_lvl), True, (255, 255, 255))
                        self.game.screen.blit(stack_text, (self.x + 28, self.y + 27))
                    # check if color is white
                    else:
                        stack_font = py.font.Font("freesansbold.ttf", 25)
                        stack_text = stack_font.render(str(self.stack_lvl), True, (0, 0, 0))
                        self.game.screen.blit(stack_text, (self.x + 28, self.y + 27))
                # Stack level 3
                elif self.gaming_piece == type_i and self.stack_lvl == 3:
                    self.game.screen.blit(self.mpid_values[type_i - 1 + stack_var * (self.stack_lvl - 1)],
                                          (self.x, self.y - stack_y))
                    # check if color is blue
                    if self.gaming_piece != 1 and self.gaming_piece != 2 and self.gaming_piece != 3:
                        stack_font = py.font.Font("freesansbold.ttf", 25)
                        stack_text = stack_font.render(str(self.stack_lvl), True, (255, 255, 255))
                        self.game.screen.blit(stack_text, (self.x + 28, self.y + 24))
                    # check if color is white
                    else:
                        stack_font = py.font.Font("freesansbold.ttf", 25)
                        stack_text = stack_font.render(str(self.stack_lvl), True, (0, 0, 0))
                        self.game.screen.blit(stack_text, (self.x + 28, self.y + 24))
                # Stack level 4
                elif self.gaming_piece == type_i and self.stack_lvl == 4:
                    self.game.screen.blit(self.mpid_values[type_i - 1 + stack_var * (self.stack_lvl - 1)],
                                          (self.x, self.y - stack_y))
                    # check if color is blue
                    if self.gaming_piece != 1 and self.gaming_piece != 2 and self.gaming_piece != 3:
                        stack_font = py.font.Font("freesansbold.ttf", 25)
                        stack_text = stack_font.render(str(self.stack_lvl), True, (255, 255, 255))
                        self.game.screen.blit(stack_text, (self.x + 28, self.y + 19))
                    # check if color is white
                    else:
                        stack_font = py.font.Font("freesansbold.ttf", 25)
                        stack_text = stack_font.render(str(self.stack_lvl), True, (0, 0, 0))
                        self.game.screen.blit(stack_text, (self.x + 28, self.y + 19))
                # Stack level 5 or higher
                elif self.gaming_piece == type_i and self.stack_lvl >= 5:
                    self.game.screen.blit(self.mpid_values[type_i - 1 + stack_var * 4], (self.x, self.y - stack_y))
                    # check if color is blue
                    if self.gaming_piece != 1 and self.gaming_piece != 2 and self.gaming_piece != 3:
                        # check if stack level is lower than 10
                        if self.stack_lvl < 10:
                            stack_font = py.font.Font("freesansbold.ttf", 25)
                            stack_text = stack_font.render(str(self.stack_lvl), True, (255, 255, 255))
                            self.game.screen.blit(stack_text, (self.x + 28, self.y + 15))
                        # Stack level is 10 or higher
                        else:
                            stack_font = py.font.Font("freesansbold.ttf", 25)
                            stack_text = stack_font.render(str(self.stack_lvl), True, (255, 255, 255))
                            self.game.screen.blit(stack_text, (self.x + 20, self.y + 15))
                    # check if color is white
                    else:
                        # Stack level is lower than 10
                        if self.stack_lvl < 10:
                            stack_font = py.font.Font("freesansbold.ttf", 25)
                            stack_text = stack_font.render(str(self.stack_lvl), True, (0, 0, 0))
                            self.game.screen.blit(stack_text, (self.x + 28, self.y + 15))
                        # Stack level is 10 or higher
                        else:
                            stack_font = py.font.Font("freesansbold.ttf", 25)
                            stack_text = stack_font.render(str(self.stack_lvl), True, (0, 0, 0))
                            self.game.screen.blit(stack_text, (self.x + 20, self.y + 15))
