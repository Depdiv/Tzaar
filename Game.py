import pygame as py
import modules.tzaar_logic as tzl
import Field
from Board import Board


class Game:
    # Constructor | setting up all global variables in the Game object
    def __init__(self, x, y):
        # init pygame
        py.init()
        py.display.set_caption("Tzaar")
        self.screen = py.display.set_mode((x, y))
        self.background_img = py.image.load("img/Spielfeld.png")
        self.clock = py.time.Clock()
        self.clock.tick(60)

        # mouse positions
        self.mx = 0
        self.my = 0
        
        # some boolean variables
        self.running = True
        self.left_m_clicked = False
        self.selected_piece = None  # if nothing selected [None] | if selected e.g.["a1"]
        self.marked_pieces = []  # tracks all marked fields
        # Mouse Position
        self.m_loc = ()
        
        # init a Board Object
        self.board = Board(self)

        # Hitbox size
        self.hb_size = 65

        # Player Variables
        # Player ID
        self.p_white = 0
        self.p_blue = 1

        # turn counter to check if it's the first or second half turn. 0 means it is the very first turn.
        self.turn_count = 0

        # Which player is first?
        self.players_turn = self.p_white

# HELPER FUNCTION
    # returns the fieldname of the clicked mouse position | if no field found return None 
    # param: mouse_pos = clicked mouse position
    def mouse_to_field(self, mouse_pos):
        for key in self.board.fd_keys:
            if self.board.fd[key].x <= mouse_pos[0] <= self.board.fd[key].x + self.hb_size and \
                    self.board.fd[key].y <= mouse_pos[1] <= self.board.fd[key].y + self.hb_size:
                return key
        return None

    def mark_pieces(self, key):
        # Mark all the allowed moves of the selected piece with green color
        for row_key in tzl.rows:
            row_list = tzl.rows[row_key]
            for piece in row_list:
                # Searching for all rows which have the selected piece in it.
                if piece == key:
                    # Separating all rows so there are now two lists per row.
                    before_selected = row_list[:row_list.index(piece) + 1]
                    after_selected = row_list[row_list.index(piece):]
                    after_selected.reverse()

                    for check_piece in before_selected:
                        checklist = before_selected[before_selected.index(check_piece)
                                                    + 1:before_selected.index(piece)]
                        checklist.reverse()
                        if len(checklist) == 0 and self.board.fd[check_piece].selected != \
                                self.board.fd[piece].selected:
                            # Check if it is the very first turn or the 1st half turn
                            if self.turn_count < 2:
                                if self.board.check_different_color(1, check_piece, piece) \
                                        and self.board.check_stack_lvl(piece, check_piece):
                                    self.board.fd[check_piece].marked = True
                                    self.marked_pieces.append(check_piece)  # append to marked pieces
                                elif self.board.check_different_color(2, check_piece, piece) \
                                        and self.board.check_stack_lvl(piece, check_piece):
                                    self.board.fd[check_piece].marked = True
                                    self.marked_pieces.append(check_piece)  # append to marked pieces
                            # Check if it is the 2nd half turn
                            else:
                                for i in range(1, 3):
                                    if self.board.check_different_color(i, check_piece, piece) \
                                            and self.board.check_stack_lvl(piece, check_piece):
                                        self.board.fd[check_piece].marked = True
                                        self.marked_pieces.append(check_piece)  # append to marked pieces
                                for i in range(1, 3):
                                    if self.board.check_same_color(i, piece, check_piece):
                                        self.board.fd[check_piece].marked = True
                                        self.marked_pieces.append(check_piece)  # append to marked pieces
                                else:
                                    pass

                        else:
                            for pieces_in_between in checklist:
                                if self.board.fd[pieces_in_between].gaming_piece != 0:
                                    break
                                elif self.board.fd[pieces_in_between].gaming_piece == 0:
                                    continue
                            else:
                                if len(checklist) != 0:
                                    # Check if it is the very first turn or the 1st half turn
                                    if self.turn_count < 2:
                                        if self.board.check_different_color(1, check_piece, piece) \
                                                and self.board.check_stack_lvl(piece, check_piece):
                                            self.board.fd[check_piece].marked = True
                                            self.marked_pieces.append(check_piece)  # append to marked pieces
                                        elif self.board.check_different_color(2, check_piece, piece) \
                                                and self.board.check_stack_lvl(piece, check_piece):
                                            self.board.fd[check_piece].marked = True
                                            self.marked_pieces.append(check_piece)  # append to marked pieces
                                    # Check if it is the 2nd half turn
                                    else:
                                        for i in range(1, 3):
                                            if self.board.check_different_color(i, check_piece, piece) \
                                                    and self.board.check_stack_lvl(piece, check_piece):
                                                self.board.fd[check_piece].marked = True
                                                self.marked_pieces.append(check_piece)  # append to marked pieces
                                        for i in range(1, 3):
                                            if self.board.check_same_color(i, piece, check_piece):
                                                self.board.fd[check_piece].marked = True
                                                self.marked_pieces.append(check_piece)  # append to marked pieces
                                        else:
                                            pass

                    for check_piece2 in after_selected:
                        checklist2 = after_selected[after_selected.index(check_piece2)
                                                    + 1: after_selected.index(piece)]
                        checklist2.reverse()
                        if len(checklist2) == 0 and self.board.fd[check_piece2].selected != \
                                self.board.fd[piece].selected:
                            # Check if it is the very first turn or the 1st half turn
                            if self.turn_count < 2:
                                if self.board.check_different_color(1, check_piece2, piece) \
                                        and self.board.check_stack_lvl(piece, check_piece2):
                                    self.board.fd[check_piece2].marked = True
                                    self.marked_pieces.append(check_piece2)  # append to marked pieces
                                elif self.board.check_different_color(2, check_piece2, piece) \
                                        and self.board.check_stack_lvl(piece, check_piece2):
                                    self.board.fd[check_piece2].marked = True
                                    self.marked_pieces.append(check_piece2)  # append to marked pieces
                            # Check if it is the 2nd half turn
                            else:
                                for i in range(1, 3):
                                    if self.board.check_different_color(i, check_piece2, piece) \
                                            and self.board.check_stack_lvl(piece, check_piece2):
                                        self.board.fd[check_piece2].marked = True
                                        self.marked_pieces.append(check_piece2)  # append to marked pieces
                                for i in range(1, 3):
                                    if self.board.check_same_color(i, piece, check_piece2):
                                        self.board.fd[check_piece2].marked = True
                                        self.marked_pieces.append(check_piece2)  # append to marked pieces
                                else:
                                    pass

                        else:
                            for pieces_in_between in checklist2:
                                if self.board.fd[pieces_in_between].gaming_piece != 0:
                                    self.board.fd[check_piece2].marked = False
                                    break
                                elif self.board.fd[pieces_in_between].gaming_piece == 0:
                                    continue
                            else:
                                if len(checklist2) != 0:
                                    # Check if it is the very first turn or the 1st half turn
                                    if self.turn_count < 2:
                                        if self.board.check_different_color(1, check_piece2, piece) \
                                                and self.board.check_stack_lvl(piece, check_piece2):
                                            self.board.fd[check_piece2].marked = True
                                            self.marked_pieces.append(check_piece2)  # append to marked pieces
                                        elif self.board.check_different_color(2, check_piece2, piece) \
                                                and self.board.check_stack_lvl(piece, check_piece2):
                                            self.board.fd[check_piece2].marked = True
                                            self.marked_pieces.append(check_piece2)  # append to marked pieces
                                    # Check if it is the 2nd half turn
                                    else:
                                        for i in range(1, 3):
                                            if self.board.check_different_color(i, check_piece2, piece) \
                                                    and self.board.check_stack_lvl(piece, check_piece2):
                                                self.board.fd[check_piece2].marked = True
                                                self.marked_pieces.append(check_piece2)  # append to marked pieces
                                        for i in range(1, 3):
                                            if self.board.check_same_color(i, piece, check_piece2):
                                                self.board.fd[check_piece2].marked = True
                                                self.marked_pieces.append(check_piece2)  # append to marked pieces

                                        else:
                                            pass
        return True

# CORE FUNCTIONS FOR TAKING TURNS
    # selects a field and marks all possible moves | returns if succeed True else False 
    # param: key = clicked field 
    def select_field(self, key):
        # Selected Piece will be marked with red color
        if key is not None and self.board.fd[key].gaming_piece != 0:
            if self.players_turn == self.p_white and self.board.check_white(key) is True:
                self.board.fd[key].selected = True
                self.selected_piece = key
                # Mark all pieces which are allowed to move to with green color
                self.mark_pieces(key)
            elif self.players_turn == self.p_white and self.board.check_white(key) is False:
                pass
            elif self.players_turn == self.p_blue and self.board.check_white(key) is False:
                self.board.fd[key].selected = True
                self.selected_piece = key
                # Mark all pieces which are allowed to move to with green color
                self.mark_pieces(key)
            else:
                pass

        return False

        # checks if move is valid and does the move | returns if succeed True else False
        # param: key = clicked field

    def capture(self, key):
        if key is not None and self.board.fd[key].marked is True and self.board.fd[key].gaming_piece != 0:  # checks if the selected field is marked
            for i in range(1, 3):
                if self.board.check_different_color(i, self.selected_piece, key):
                    self.board.fd[key].gaming_piece = self.board.fd[
                        self.selected_piece].gaming_piece  # sets the SELECTED gamepiece on the MARKED field
                    self.board.fd[key].stack_lvl = self.board.fd[self.selected_piece].stack_lvl  # The field you are moving to gets the same stack lvl
                    self.board.fd[self.selected_piece].gaming_piece = 0  # Removes the stone from the SELECTED field
                    self.board.fd[self.selected_piece].selected = False  # UNSELECTS the field
                    self.selected_piece = None  # sets global variable to None because we successfully moved the selected stone to a field
                    for marked_piece in self.marked_pieces:  # undo markings for marked pieces
                        self.board.fd[marked_piece].marked = False
                    self.marked_pieces.clear()  # remove all pieces from the marked list
                    return True

        return False
    # checks if move is valid and does the move | returns if succeed True else False
    # param: key = clicked field

    def stack_up(self, key):
        if key is not None and self.board.fd[key].marked is True and \
                self.board.fd[key].gaming_piece != 0:  # checks if the selected field is marked
            for i in range(1, 3):
                if self.board.check_same_color(i, self.selected_piece, key):
                    self.board.fd[key].gaming_piece = self.board.fd[
                        self.selected_piece].gaming_piece  # sets the SELECTED gamepiece on the MARKED field
                    self.board.fd[key].stack_lvl += self.board.fd[
                        self.selected_piece].stack_lvl  # Summate the stack lvl of the selected piece and the marked piece up
                    self.board.fd[self.selected_piece].gaming_piece = 0  # Removes the stone from the SELECTED field
                    self.board.fd[self.selected_piece].selected = False  # UNSELECTS the field
                    self.selected_piece = None  # sets global variable to None because we successfully moved the selected stone to a field
                    for marked_piece in self.marked_pieces:  # undo markings for marked pieces
                        self.board.fd[marked_piece].marked = False
                    self.marked_pieces.clear()  # remove all pieces from the marked list
                    return True

        return False

    # checks if move is valid and does the move | returns if succeed True else False
    # param: key = clicked field
# TURN FUNCTIONS  
    # first half turn | returns if succeed True else False  
    # u have to fuck an enemy stone
    def half_turn1(self):

        succeed = False  # track if all functions finished execution

        key = self.mouse_to_field(self.m_loc)  # Gets the current clicked field

        if self.selected_piece is None:  # If no piece is selected
            if self.select_field(key):
                pass

        else:  # if a piece is selected
            if self.capture(key):
                succeed = True  # Set only true if half turn is finished

        return succeed 

    # second half turn | returns if succeed True else False 
    # choose between 1.fuck the enemy 2.stack up any piece/stack 3.pass the turn
    def half_turn2(self):
        succeed = False  # track if all functions finished execution

        key = self.mouse_to_field(self.m_loc)  # Gets the current clicked field

        if self.selected_piece is None:  # If no stone is selected
            if self.select_field(key):
                pass
        else:  # if a piece is selected
            if self.capture(key):
                succeed = True  # Set only true if half turn is finished
            elif self.stack_up(key):
                succeed = True  # Set only true if half turn is finished

        return succeed

    def board_stuff(self):
        turn_x = 25
        turn_y = 700
        black_color = (0, 0, 0)
        font_style = "freesansbold.ttf"
        if self.players_turn == self.p_white and self.turn_count == 1:
            turn_font = py.font.Font(font_style, 25)
            turn_text = turn_font.render("White, 1st half turn!", True, black_color)
            self.screen.blit(turn_text, (turn_x, turn_y))
        elif self.players_turn == self.p_white and self.turn_count == 2:
            turn_font = py.font.Font(font_style, 25)
            turn_text = turn_font.render("White, 2nd half turn!", True, black_color)
            self.screen.blit(turn_text, (turn_x, turn_y))
        elif self.players_turn == self.p_blue and self.turn_count == 1:
            turn_font = py.font.Font(font_style, 25)
            turn_text = turn_font.render("Blue, 1st half turn!", True, black_color)
            self.screen.blit(turn_text, (turn_x, turn_y))
        elif self.players_turn == self.p_blue and self.turn_count == 2:
            turn_font = py.font.Font(font_style, 25)
            turn_text = turn_font.render("Blue, 2nd half turn!", True, black_color)
            self.screen.blit(turn_text, (turn_x, turn_y))
        else:
            turn_font = py.font.Font(font_style, 25)
            turn_text = turn_font.render("White, the very first turn!", True, black_color)
            self.screen.blit(turn_text, (turn_x, turn_y))

# GAMELOOP
    def run(self):
        while self.running is True:

            # Mouse location    
            self.m_loc = py.mouse.get_pos()

            # EVENTS
            for event in py.event.get():
                # If Quit event
                if event.type == py.QUIT:
                    self.running = False

                # If Mouse Buttons pressed
                if event.type == py.MOUSEBUTTONDOWN:
                     
                    # if you select a piece
                    if event.button == 1:  # Left Mouse Button | Take a Turn

                        if self.turn_count == 1:  # if half turn 1
                            if self.half_turn1():
                                self.turn_count = 2
                        elif self.turn_count == 2:  # if half turn 2
                            if self.half_turn2():
                                self.turn_count = 1
                                if self.players_turn == self.p_white:
                                    self.players_turn = self.p_blue
                                else:
                                    self.players_turn = self.p_white
                        else:
                            # the very first move of the game
                            if self.half_turn1():
                                # After half turn 1 white passes and it's blues turn
                                self.turn_count = 1
                                self.players_turn = self.p_blue

                    if event.button == 3:  # Right Mouse Button | unmark all marked pieces
                        if self.selected_piece is not None:
                            for key in self.board.fd_keys:
                                self.board.fd[key].marked = False
                                self.board.fd[key].selected = False
                            self.selected_piece = None
            
            # UPDATE | First Background | Second Stones
            # Background
            self.screen.blit(self.background_img, (0, 0))

            # Draw stones | Updating the fields on the board
            for key in self.board.fd_keys:
                self.board.fd[key].update()

            self.board_stuff()

            # DISPLAY
            py.display.update()
