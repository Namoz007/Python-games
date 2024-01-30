from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
import random as rand
class game(QWidget):
    def __init__(self):
        super().__init__()
        self.buttons()
        self.buttons_text()
        self.start_count = 0
        self.game_count = 0


    def buttons(self):
        self.h_btn_1 = QHBoxLayout()
        self.h_btn_2 = QHBoxLayout()
        self.h_btn_3 = QHBoxLayout()
        self.h_btn_4 = QHBoxLayout()
        self.v_btn_main = QVBoxLayout()
        self.start_lay = QHBoxLayout()
        self.h_danger = QHBoxLayout()
        self.h_count = QHBoxLayout()
        
        self.danger = QLabel()
        self.h_danger.addWidget(self.danger)

        self.btn1 = QPushButton()
        self.btn1.clicked.connect(self.push_btn1)

        self.btn2 = QPushButton()
        self.btn2.clicked.connect(self.push_btn2)

        self.btn3 = QPushButton()
        self.btn3.clicked.connect(self.push_btn3)
        
        self.btn4 = QPushButton()
        self.btn4.clicked.connect(self.push_btn4)

        self.btn5 = QPushButton()
        self.btn5.clicked.connect(self.push_btn5)

        self.btn6 = QPushButton()
        self.btn6.clicked.connect(self.push_btn6)

        self.btn7 = QPushButton()
        self.btn7.clicked.connect(self.push_btn7)

        self.btn8 = QPushButton()
        self.btn8.clicked.connect(self.push_btn8)

        self.btn9 = QPushButton()
        self.btn9.clicked.connect(self.push_btn9)

        self.btn10 = QPushButton()
        self.btn10.clicked.connect(self.push_btn10)

        self.btn11 = QPushButton()
        self.btn11.clicked.connect(self.push_btn11)

        self.btn12 = QPushButton()
        self.btn12.clicked.connect(self.push_btn12)

        self.btn13 = QPushButton()
        self.btn13.clicked.connect(self.push_btn13)

        self.btn14 = QPushButton()
        self.btn14.clicked.connect(self.push_btn14)

        self.btn15 = QPushButton()
        self.btn15.clicked.connect(self.push_btn15)

        self.btn16 = QPushButton()
        self.btn16.clicked.connect(self.push_btn16)

        self.game_countt = QLabel('                                                0')
        self.h_count.addWidget(self.game_countt)

        self.start = QPushButton("Start")
        self.start.clicked.connect(self.start_push)
        self.exit = QPushButton("Exit")
        self.exit.clicked.connect(self.exit_met)

        self.res = QPushButton("Restart")
        self.res.clicked.connect(self.res_met)

        self.start_lay.addWidget(self.start)
        self.start_lay.addWidget(self.exit)
        self.start_lay.addWidget(self.res)

        self.h_btn_1.addWidget(self.btn1)
        self.h_btn_1.addWidget(self.btn2)
        self.h_btn_1.addWidget(self.btn3)
        self.h_btn_1.addWidget(self.btn4)

        self.h_btn_2.addWidget(self.btn5)
        self.h_btn_2.addWidget(self.btn6)
        self.h_btn_2.addWidget(self.btn7)
        self.h_btn_2.addWidget(self.btn8)

        self.h_btn_3.addWidget(self.btn9)
        self.h_btn_3.addWidget(self.btn10)
        self.h_btn_3.addWidget(self.btn11)
        self.h_btn_3.addWidget(self.btn12)

        self.h_btn_4.addWidget(self.btn13)
        self.h_btn_4.addWidget(self.btn14)
        self.h_btn_4.addWidget(self.btn15)
        self.h_btn_4.addWidget(self.btn16)

        self.v_btn_main.addLayout(self.h_danger)
        self.v_btn_main.addLayout(self.h_btn_1)
        self.v_btn_main.addLayout(self.h_btn_2)
        self.v_btn_main.addLayout(self.h_btn_3)
        self.v_btn_main.addLayout(self.h_btn_4)
        self.v_btn_main.addLayout(self.h_count)
        self.v_btn_main.addLayout(self.start_lay)
        
        
        self.setLayout(self.v_btn_main)
    def exit_met(self):
        self.close()
    
    def res_met(self):
        self.btn1.setText('1')
        self.btn2.setText('2')
        self.btn3.setText('3')
        self.btn4.setText('4')
        self.btn5.setText('5')
        self.btn6.setText('6')
        self.btn7.setText('7')
        self.btn8.setText('8')
        self.btn9.setText('9')
        self.btn10.setText('10')
        self.btn11.setText('11')
        self.btn12.setText('12')
        self.btn13.setText('13')
        self.btn14.setText('14')
        self.btn15.setText('15')
        self.btn16.setText(' ')
        self.game_count = 0
        self.game_countt.setText(f'                                                {str(self.game_count)}')
        self.start_count = 0

    def control(self):
        self.btn_lst = [self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,self.btn11,self.btn12,self.btn13,self.btn14,self.btn15,self.btn16]
        for i in self.btn_lst:
            i.setDisabled(True)

        if self.btn1 == '1' and self.btn2 == '2' and self.btn3 == '3' and self.btn4 == '4' and self.btn5 == '5' and self.btn6 == '6' and self.btn7 == '7' and self.btn8 == '8' and self.btn9 == '9' and self.btn10 == '10' and self.btn11 == '11' and self.btn12 == '12' and self.btn13 == '13' and self.btn14 == '14' and self.btn15 == '15' and self.btn16 == ' ':
            self.win = QMessageBox()
            self.win.setWindowTitle("Winner")
            self.win.setText(f"Winner! You have won in {self.game_count} total attamps!")
            self.win.setIcon(QMessageBox.Warning)
            self.win.clickedButton(self.res_met)
            self.win.exec_()

    def buttons_text(self):
        self.btn1.setText('1')
        self.btn2.setText('2')
        self.btn3.setText('3')
        self.btn4.setText('4')
        self.btn5.setText('5')
        self.btn6.setText('6')
        self.btn7.setText('7')
        self.btn8.setText('8')
        self.btn9.setText('9')
        self.btn10.setText('10')
        self.btn11.setText('11')
        self.btn12.setText('12')
        self.btn13.setText('13')
        self.btn14.setText('14')
        self.btn15.setText('15')
        self.btn16.setText(' ')

    def start_push(self):
        if self.start_count == 0:
            self.start_count += 1
            self.random_choise = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15',' ']

            choise = rand.choices(self.random_choise)
            self.btn1.setText(choise[0])
            self.random_choise.remove(choise[0])

            choise = rand.choices(self.random_choise)
            self.btn2.setText(choise[0])
            self.random_choise.remove(choise[0])

            choise = rand.choices(self.random_choise)
            self.btn3.setText(choise[0])
            self.random_choise.remove(choise[0])

            choise = rand.choices(self.random_choise)
            self.btn4.setText(choise[0])
            self.random_choise.remove(choise[0])

            choise = rand.choices(self.random_choise)
            self.btn5.setText(choise[0])
            self.random_choise.remove(choise[0])

            choise = rand.choices(self.random_choise)
            self.btn6.setText(choise[0])
            self.random_choise.remove(choise[0])

            choise = rand.choices(self.random_choise)
            self.btn7.setText(choise[0])
            self.random_choise.remove(choise[0])

            choise = rand.choices(self.random_choise)
            self.btn8.setText(choise[0])
            self.random_choise.remove(choise[0])

            choise = rand.choices(self.random_choise)
            self.btn9.setText(choise[0])
            self.random_choise.remove(choise[0])

            choise = rand.choices(self.random_choise)
            self.btn10.setText(choise[0])
            self.random_choise.remove(choise[0])

            choise = rand.choices(self.random_choise)
            self.btn11.setText(choise[0])
            self.random_choise.remove(choise[0])

            choise = rand.choices(self.random_choise)
            self.btn12.setText(choise[0])
            self.random_choise.remove(choise[0])

            choise = rand.choices(self.random_choise)
            self.btn13.setText(choise[0])
            self.random_choise.remove(choise[0])

            choise = rand.choices(self.random_choise)
            self.btn14.setText(choise[0])
            self.random_choise.remove(choise[0])

            choise = rand.choices(self.random_choise)
            self.btn15.setText(choise[0])
            self.random_choise.remove(choise[0])

            choise = rand.choices(self.random_choise)
            self.btn16.setText(choise[0])
            self.random_choise.remove(choise[0])
        else: 
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("You don't choise!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()

    
    def push_btn1(self):
        if self.start_count > 0:
            if self.btn1 == ' ':
                self.danger.setText("                                  Your choice is incorrect!")
            elif self.btn2.text() == " ":
                self.btn2.setText(self.btn1.text())
                self.btn1.setText(" ")
                self.game_count += 1
            elif self.btn5.text() == " ":
                self.btn5.setText(self.btn1.text())
                self.btn1.setText(" ")
                self.game_count += 1
            else:
                self.danger.setText("                                  Your choice is incorrect!")
            self.game_countt.setText(f'                                                {str(self.game_count)}')
        else:
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("First to click start!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()

    def push_btn2(self):
        if self.start_count > 0:
            if self.btn2.text() == ' ':
                self.danger.setText("                                  Your choice is incorrect!")
            elif self.btn1.text() == " ":
                self.btn1.setText(self.btn2.text())
                self.btn2.setText(" ")
                self.game_count += 1
            elif self.btn3.text() == " ":
                self.btn3.setText(self.btn2.text())
                self.btn2.setText(" ")
                self.game_count += 1
            elif self.btn6.text() == " ":
                self.btn6.setText(self.btn2.text())
                self.btn2.setText(" ")
                self.game_count += 1
            else:
                self.danger.setText("                                  Your choice is incorrect!")
            self.game_countt.setText(f'                                                {str(self.game_count)}')

        else:
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("First to click start!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()

    def push_btn3(self):
        if self.start_count > 0:
            if self.btn3 == ' ':
                self.danger.setText("                                  Your choice is incorrect!")
            elif self.btn2.text() == " ":
                self.btn2.setText(self.btn3.text())
                self.btn3.setText(" ")
                self.game_count += 1
            elif self.btn4.text() == " ":
                self.btn4.setText(self.btn3.text())
                self.btn3.setText(" ")
                self.game_count += 1
            elif self.btn7.text() == ' ':
                self.btn7.setText(self.btn3.text())
                self.btn3.setText(" ")
                self.game_count += 1
            else:
                self.danger.setText("                                  Your choice is incorrect!")
            self.game_countt.setText(f'                                                {str(self.game_count)}')
        else:
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("First to click start!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()

    def push_btn4(self):
        if self.start_count > 0:
            if self.btn4.text() == ' ':
                self.danger.setText("                                  Your choice is incorrect!")
            if self.btn3.text() == " ":
                self.btn3.setText(self.btn4.text())
                self.btn4.setText(" ")
                self.game_count += 1
            elif self.btn8.text() == " ":
                self.btn8.setText(self.btn4.text())
                self.btn4.setText(" ")
                self.game_count += 1
            else:
                self.danger.setText("                                  Your choice is incorrect!")
            self.game_countt.setText(f'                                                {str(self.game_count)}')
        else:
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("First to click start!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()

    def push_btn5(self):
        if self.start_count > 0:
            if self.btn5 == ' ':
                self.danger.setText("                                  Your choice is incorrect!")
            elif self.btn1.text() == " ":
                self.btn1.setText(self.btn5.text())
                self.btn5.setText(" ")
                self.game_count += 1
            elif self.btn6.text() == " ":
                self.btn6.setText(self.btn5.text())
                self.btn5.setText(" ")
                self.game_count += 1
            elif self.btn9.text() == ' ':
                self.btn9.setText(self.btn5.text())
                self.btn5.setText(" ")
                self.game_count += 1
            else:
                self.danger.setText("                                  Your choice is incorrect!")
            self.game_countt.setText(f'                                                {str(self.game_count)}')
        else:
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("First to click start!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()


    def push_btn6(self):
        if self.start_count > 0:
            if self.btn6 == ' ':
                self.danger.setText("                                  Your choice is incorrect!")
            elif self.btn5.text() == " ":
                self.btn5.setText(self.btn6.text())
                self.btn6.setText(" ")
                self.game_count += 1
            elif self.btn7.text() == " ":
                self.btn7.setText(self.btn6.text())
                self.btn6.setText(" ")
                self.game_count += 1
            elif self.btn2.text() == " ":
                self.btn2.setText(self.btn6.text())
                self.btn6.setText(" ")
                self.game_count += 1
            elif self.btn10.text() == " ":
                self.btn10.setText(self.btn6.text())
                self.btn6.setText(" ")
                self.game_count += 1
            else:
                self.danger.setText("                                  Your choice is incorrect!")
            self.game_countt.setText(f'                                                {str(self.game_count)}')
        else:
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("First to click start!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()


    def push_btn7(self):
        if self.start_count > 0:
            if self.btn7 == ' ':
                self.danger.setText("                                  Your choice is incorrect!")
            if self.btn3.text() == " ":
                self.btn3.setText(self.btn7.text())
                self.btn7.setText(" ")
                self.game_count += 1
            elif self.btn8.text() == " ":
                self.btn8.setText(self.btn7.text())
                self.btn7.setText(" ")
                self.game_count += 1
            elif self.btn6.text() == " ":
                self.btn6.setText(self.btn7.text())
                self.btn7.setText(" ")
                self.game_count += 1
            elif self.btn11.text() == " ":
                self.btn11.setText(self.btn7.text())
                self.btn7.setText(" ")
                self.game_count += 1
            else:
                self.danger.setText("                                  Your choice is incorrect!")
            self.game_countt.setText(f'                                                {str(self.game_count)}')
        else:
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("First to click start!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()

    def push_btn8(self):
        if self.start_count > 0:
            if self.btn8 == ' ':
                self.danger.setText("                                  Your choice is incorrect!")
            elif self.btn4.text() == " ":
                self.btn4.setText(self.btn8.text())
                self.btn8.setText(" ")
                self.game_count += 1
            elif self.btn7.text() == " ":
                self.btn7.setText(self.btn8.text())
                self.btn8.setText(" ")
                self.game_count += 1
            elif self.btn12.text() == ' ':
                self.btn12.setText(self.btn8.text())
                self.btn8.setText(" ")
                self.game_count += 1
            else:
                self.danger.setText("                                  Your choice is incorrect!")
            self.game_countt.setText(f'                                                {str(self.game_count)}')
        else:
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("First to click start!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()

    def push_btn9(self):
        if self.start_count > 0:
            if self.btn9 == ' ':
                self.danger.setText("                                  Your choice is incorrect!")
            elif self.btn10.text() == " ":
                self.btn10.setText(self.btn9.text())
                self.btn9.setText(" ")
                self.game_count += 1
            elif self.btn13.text() == " ":
                self.btn13.setText(self.btn9.text())
                self.btn9.setText(" ")
                self.game_count += 1
            elif self.btn5.text() == " ":
                self.btn5.setText(self.btn9.text())
                self.btn9.setText(" ")
                self.game_count += 1
            else:
                self.danger.setText("                                  Your choice is incorrect!")
            self.game_countt.setText(f'                                                {str(self.game_count)}')
        else:
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("First to click start!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()

    def push_btn10(self):
        if self.start_count > 0:
            if self.btn10.text() == ' ':
                self.danger.setText("                                  Your choice is incorrect!")
            elif self.btn9.text() == " ":
                self.btn9.setText(self.btn10.text())
                self.btn10.setText(" ")
                self.game_count += 1
            elif self.btn11.text() == " ":
                self.btn11.setText(self.btn10.text())
                self.btn10.setText(" ")
                self.game_count += 1
            elif self.btn6.text() == " ":
                self.btn6.setText(self.btn10.text())
                self.btn10.setText(" ")
                self.game_count += 1
            elif self.btn14.text() == " ":
                self.btn14.setText(self.btn10.text())
                self.btn10.setText(" ")
                self.game_count += 1
            else:
                self.danger.setText("                                  Your choice is incorrect!")
            self.game_countt.setText(f'                                                {str(self.game_count)}')
        else:
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("First to click start!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()

    def push_btn11(self):
        if self.start_count > 0:
            if self.btn11.text() == ' ':
                self.danger.setText("                                  Your choice is incorrect!")
            elif self.btn10.text() == " ":
                self.btn10.setText(self.btn11.text())
                self.btn11.setText(" ")
                self.game_count += 1
            elif self.btn12.text() == " ":
                self.btn12.setText(self.btn11.text())
                self.btn11.setText(" ")
                self.game_count += 1
            elif self.btn7.text() == " ":
                self.btn7.setText(self.btn11.text())
                self.btn11.setText(" ")
                self.game_count += 1
            elif self.btn15.text() == " ":
                self.btn15.setText(self.btn11.text())
                self.btn11.setText(" ")
                self.game_count += 1
            else:
                self.danger.setText("                                  Your choice is incorrect!")
            self.game_countt.setText(f'                                                {str(self.game_count)}')
        else:
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("First to click start!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()

    def push_btn12(self):
        if self.start_count > 0:
            if self.btn12.text() == ' ':
                self.danger.setText("                                  Your choice is incorrect!")
            elif self.btn8.text() == " ":
                self.btn8.setText(self.btn12.text())
                self.btn12.setText(" ")
                self.game_count += 1
            elif self.btn11.text() == " ":
                self.btn11.setText(self.btn12.text())
                self.btn12.setText(" ")
                self.game_count += 1
            elif self.btn16.text() == " ":
                self.btn16.setText(self.btn12.text())
                self.btn12.setText(" ")
                self.game_count += 1
            else:
                self.danger.setText("                                  Your choice is incorrect!")
            self.game_countt.setText(f'                                                {str(self.game_count)}')
        else:
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("First to click start!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()

    def push_btn13(self):
        if self.start_count > 0:
            if self.btn13.text() == ' ':
                self.danger.setText("                                  Your choice is incorrect!")
            elif self.btn9.text() == " ":
                self.btn9.setText(self.btn13.text())
                self.btn13.setText(" ")
                self.game_count += 1
            elif self.btn14.text() == " ":
                self.btn14.setText(self.btn13.text())
                self.btn13.setText(" ")
                self.game_count += 1
            else:
                self.danger.setText("                                  Your choice is incorrect!")
            self.game_countt.setText(f'                                                {str(self.game_count)}')
        else:
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("First to click start!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()


    def push_btn14(self):
        if self.start_count > 0:
            if self.btn14.text() == ' ':
                self.danger.setText("                                  Your choice is incorrect!")
            elif self.btn13.text() == " ":
                self.btn13.setText(self.btn14.text())
                self.btn14.setText(" ")
                self.game_count += 1
            elif self.btn15.text() == " ":
                self.btn15.setText(self.btn14.text())
                self.btn14.setText(" ")
                self.game_count += 1
            elif self.btn10.text() == " ":
                self.btn10.setText(self.btn14.text())
                self.btn14.setText(" ")
                self.game_count += 1
            else:
                self.danger.setText("                                  Your choice is incorrect!")
            self.game_countt.setText(f'                                                {str(self.game_count)}')
        else:
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("First to click start!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()

    def push_btn15(self):
        if self.start_count > 0:
            if self.btn15.text() == ' ':
                self.danger.setText("                                  Your choice is incorrect!")
            elif self.btn14.text() == " ":
                self.btn14.setText(self.btn15.text())
                self.btn15.setText(" ")
                self.game_count += 1
            elif self.btn16.text() == " ":
                self.btn16.setText(self.btn15.text())
                self.btn15.setText(" ")
                self.game_count += 1
            elif self.btn11.text() == " ":
                self.btn11.setText(self.btn15.text())
                self.btn15.setText(" ")
                self.game_count += 1
            else:
                self.danger.setText("                                  Your choice is incorrect!")
            self.game_countt.setText(f'                                                {str(self.game_count)}')
        else:
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("First to click start!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()

    def push_btn16(self):
        if self.start_count > 0:
            if self.btn16.text() == " ":
                self.danger.setText("                                  Your choice is incorrect!")
            elif self.btn15.text() == " ":
                self.btn15.setText(self.btn16.text())
                self.btn1.setText(" ")
                self.game_count += 1
            elif self.btn12.text() == " ":
                self.btn12.setText(self.btn16.text())
                self.btn16.setText(" ")
                self.game_count += 1
            else:
                self.danger.setText("                                  Your choice is incorrect!")
            self.game_count += 1
            self.game_countt.setText(f'                                                {str(self.game_count)}')

        else:
            self.not_start_message = QMessageBox()
            self.not_start_message.setWindowTitle("Not!")
            self.not_start_message.setText("First to click start!")
            self.not_start_message.setIcon(QMessageBox.Warning)
            self.not_start_message.exec_()

app = QApplication([])
main_game = game()

main_game.show()
app.exec_()