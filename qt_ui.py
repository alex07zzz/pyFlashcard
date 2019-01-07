# coding:utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome

class MainUI (QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_left_layout()
        self.init_right_layout()
        self.set_style()

    def init_ui(self):
        self.setFixedSize(960,700)
        self.main_widget = QtWidgets.QWidget()  # create main window
        self.main_layout = QtWidgets.QGridLayout()  # create main grid main_layout
        self.main_widget.setLayout(self.main_layout)

        self.left_widget = QtWidgets.QWidget()
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()
        self.left_widget.setLayout(self.left_layout)

        self.right_widget = QtWidgets.QWidget()
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)
        self.setCentralWidget(self.main_widget)

    def init_left_layout(self):
        self.left_close = QtWidgets.QPushButton(" ")    # close button
        self.left_visit = QtWidgets.QPushButton(" ")    # blank button
        self.left_mini = QtWidgets.QPushButton(" ")     # minimize button

        self.left_label_1 = QtWidgets.QPushButton("Recent")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("My FlashCard")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("Edit")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton("Recent File 1")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton("Recent File 2")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton("Local Files 1")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton("Local Files 2")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton("Change")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton("Add")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton("Delete")
        self.left_button_7.setObjectName('left_button')

        self.left_layout.addWidget(self.left_close, 0, 0, 1, 0)
        self.left_layout.addWidget(self.left_mini, 0, 1, 1, 0)
        self.left_layout.addWidget(self.left_visit, 0, 2, 1, 0)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)

    def init_right_layout(self):
        # search bar
        self.right_search_bar_widget = QtWidgets.QWidget()
        self.right_search_bar_layout = QtWidgets.QGridLayout()
        self.right_search_bar_widget.setLayout(self.right_search_bar_layout)

        self.search_icon = QtWidgets.QLabel(chr(0x2315) + ' ' + 'search ')

        self.right_search_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right_search_bar_widget_search_input.setPlaceholderText("Enter FlashCard list name, press RETURN to search")

        self.right_search_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right_search_bar_layout.addWidget(self.right_search_bar_widget_search_input, 0, 1, 1, 8)

        self.right_layout.addWidget(self.right_search_bar_widget, 0, 0, 1, 9)

        # FlashCard
        self.right_flashcard_widget = QtWidgets.QWidget()
        self.right_flashcard_layout = QtWidgets.QGridLayout()
        self.right_flashcard_widget.setLayout(self.right_flashcard_layout)
        self.right_flashcard_button_1 = QtWidgets.QPushButton("Question")
        self.right_flashcard_button_1.setObjectName('flashcard_button')
        self.right_flashcard_button_1.setFixedSize(750, 200)
        self.right_flashcard_button_2 = QtWidgets.QPushButton("Answer")
        self.right_flashcard_button_2.setObjectName('flashcard_button')
        self.right_flashcard_button_2.setFixedSize(750, 300)
        self.right_flashcard_layout.addWidget(self.right_flashcard_button_1, 0, 0)
        self.right_flashcard_layout.addWidget(self.right_flashcard_button_2, 1, 0)
        self.right_layout.addWidget(self.right_flashcard_widget, 2, 0, 1, 9)



        self.right_playconsole_widget = QtWidgets.QWidget()
        self.right_playconsole_layout = QtWidgets.QGridLayout()
        self.right_playconsole_widget.setLayout(self.right_playconsole_layout)

        self.console_backward_button = QtWidgets.QPushButton(qtawesome.icon('fa.backward', color = '#F76677', fontsize=18), "")
        self.console_backward_button.setObjectName('console_button')
        self.console_backward_button.setFixedSize(50, 50)
        self.console_forward_button = QtWidgets.QPushButton(qtawesome.icon('fa.forward', color = '#F76677', fontsize=18), "")
        self.console_forward_button.setObjectName('console_button')
        self.console_forward_button.setFixedSize(50, 50)
        self.console_check_button = QtWidgets.QPushButton(qtawesome.icon('fa.check', color = '#F76677', fontsize=18), "")
        self.console_check_button.setObjectName('console_button')
        self.console_check_button.setFixedSize(50,50)

        self.right_playconsole_layout.addWidget(self.console_backward_button, 0, 0)
        self.right_playconsole_layout.addWidget(self.console_check_button, 0, 1)
        self.right_playconsole_layout.addWidget(self.console_forward_button, 0, 2)
        self.right_playconsole_layout.setAlignment(QtCore.Qt.AlignJustify)

        self.right_layout.addWidget(self.right_playconsole_widget, 10, 0, 1, 9)

    def set_style(self):
        self.left_close.setFixedSize(15, 15)
        self.left_visit.setFixedSize(15, 15)
        self.left_mini.setFixedSize(15, 15)

        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_mini.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_visit.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none; color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
            }
            QPushButton#left_button:hover{
                border-left:4px solid #F76677;
                font-weight:700;
            }
            QWidget#left_widget{
                background:gray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                background:LightGray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-right:1px solid white;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
        ''')

        self.right_search_bar_widget_search_input.setStyleSheet('''
            QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
            }
        ''')

        self.right_flashcard_widget.setStyleSheet('''
            QPushButton{
                border:none;
                background:white;
                color:LightGray;
            }
        ''')

        self.right_playconsole_widget.setStyleSheet('''
            QPushButton{
                border:none;
            }
        ''')

        self.setWindowOpacity(0.9)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.main_layout.setSpacing(0)


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
