import decimal

from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import uic
import sys
import os

from Tools.scripts.win_add2path import PATH

from db_func import check_login, check_password

UI_DIR_PATH = os.path.join(os.getcwd(), 'ui')


class Login_win(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login_win, self).__init__()
        uic.loadUi(os.path.join(UI_DIR_PATH, 'login_window.ui'), self)
        self.login_btn.clicked.connect(self.login)
        self.not_auto_text.hide()

    def login(self):
        login_text = self.login_line.text()
        password_text = self.password_line.text()
        if check_login(login_text) and check_password(password_text):
            self.close()
            main_window.show()
        else:
            self.not_auto_text.show()


def round_number(number):
    return str(decimal.Decimal(str(number)).quantize(decimal.Decimal('1.0'), rounding=decimal.ROUND_HALF_UP))


class Main_win(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main_win, self).__init__()
        uic.loadUi(os.path.join(UI_DIR_PATH, 'main_window.ui'), self)
        local_teory_view_path = f"file:\\\{os.path.join(os.getcwd(), 'theory', 'page.html')}"
        web_teory_view_path = 'http://feniks7.pythonanywhere.com'
        print(local_teory_view_path)
        self.teory_view.setUrl(QUrl(web_teory_view_path))
        self.pushButton.clicked.connect(self.calc_milk)
        self.pushButton_2.clicked.connect(self.calc_dry_matter)
        self.pushButton_3.clicked.connect(self.calc_dry_rez)
        self.pushButton_4.clicked.connect(self.calc_water)
        self.pushButton_5.clicked.connect(self.calc_fat_suh)
        self.pushButton_6.clicked.connect(self.calc_l_to_kg)
        self.pushButton_7.clicked.connect(self.calc_skim)
        self.pushButton_8.clicked.connect(self.calc_double_fals)
        self.pushButton_9.clicked.connect(self.calc_sale_milk)
        self.pushButton_10.clicked.connect(self.calc_pred)

        self.pushButton_11.clicked.connect(self.calc_towar)

    def show_message_box(self,message):
        QMessageBox.about(self, "Ошибка", message)

    def calc_milk(self):
        print("OK")
        if self.milk_gk_inp.text() and self.fat_milk_inp.text() and self.fat_skim_inp.text() and self.fat_cream_inp.text():
            milk_gk = float(self.milk_gk_inp.text())
            fat_milk = float(self.fat_milk_inp.text())
            fat_skim = float(self.fat_skim_inp.text())
            fat_cream = float(self.fat_cream_inp.text())
            if fat_milk > fat_skim and fat_cream > fat_skim:
                result = (milk_gk * (fat_milk - fat_skim)) / (fat_cream - fat_skim)
                self.milk_kg_ans.setText(round_number(result))
            else:
                message = "Жирность обрата больше чем жирность молока или сливок"
                self.show_message_box(message)

        else:
            message = "Не все поля заполнены"
            self.show_message_box(message)

    def calc_dry_matter(self):
        if self.obesity_inp.text() and self.density_inp.text():
            obesity_milk = float(self.obesity_inp.text())
            density = float(self.density_inp.text())
            result = (((4.9 * obesity_milk) + density)/4) + 0.5
            self.dry_matter_ans.setText(round_number(result))
        else:
            self.show_message_box()

    def calc_dry_rez(self):
        if self.obesity2_inp.text() and self.density2_inp.text():
            obesity_milk = float(self.obesity2_inp.text())
            density = float(self.density2_inp.text())
            result = ((obesity_milk/5) + (density/40) + 0.76)
            self.somo_ans.setText(round_number(result))
        else:
            self.show_message_box()

    def calc_water(self):
        if self.somo_milk_inp.text() and self.dr_matter_inp.text():
            somo_milk = float(self.somo_milk_inp.text())
            dry_rez = float(self.dr_matter_inp.text())
            if somo_milk != 0:
                result = ((somo_milk - dry_rez) / somo_milk * 100)
                self.water_in_milk_ans.setText(round_number(result))
            else:
                message = "СОМО не должно равняться 0"
                self.show_message_box(message)

        else:
            self.show_message_box()

    def calc_skim(self):
        if self.obesity_milk_inp_2.text() and self.fat_milk_et_inp_3.text():
            obesity_milk = float(self.obesity_milk_inp_2.text())
            fat_et = float(self.fat_milk_et_inp_3.text())
            if obesity_milk != 0:
                result = ((obesity_milk - fat_et) / obesity_milk * 100)
                self.skim_in_milk_ans.setText(round_number(result))
            else:
                message = "СОМО не должно равняться 0"
                self.show_message_box(message)
        else:
            self.show_message_box()

    def calc_fat_suh(self):
        if self.fat_cream_inp_2.text() and self.somo_inp.text():
            fat_et = float(self.fat_cream_inp_2.text())
            somo_et = float(self.somo_inp.text())
            result = (fat_et / somo_et * 100)
            self.fat_suh_ans.setText(round_number(result))
        else:
            self.show_message_box()

    def calc_double_fals(self):
        if self.fat_milk_inp_5.text() and self.fat_skim_inp_2.text() and self.somo_inp_2.text() and self.somo_et_inp.text():
            fat_milk = float(self.fat_milk_inp_5.text())
            fat_et = float(self.fat_skim_inp_2.text())
            somo = float(self.somo_inp_2.text())
            somo_et = float(self.somo_et_inp.text())
            result = (100-(fat_et/fat_milk*100))-(100-(somo_et/somo*100))
            print(result)
            self.double_f_ans.setText(round_number(result))
        else:
            self.show_message_box()

    def calc_towar(self):
        if self.milk_get_inp.text() and self.sale_milk_inp.text():
            nad_milk = float(self.milk_get_inp.text())
            sale_milk = float(self.sale_milk_inp.text())
            result = (sale_milk/nad_milk)*100
            self.tow_milk_ans.setText(round_number(result))
        else:
            self.show_message_box()

    def calc_l_to_kg(self):
        if self.l_milk_inp.text() and self.density_inp_2.text():
            milk_l = float(self.l_milk_inp.text())
            density = float(self.density_inp_2.text())
            result = milk_l * density
            self.l_to_kg_ans.setText(round_number(result))
        else:
            self.show_message_box()

    def calc_sale_milk(self):
        if self.milk_fack_dens_inp.text() and self.milk_fact_inp.text() and self.base_dens_inp.text():
            fact_milk = float(self.milk_fack_dens_inp.text())
            fact_den = float(self.milk_fact_inp.text())
            base_den = float(self.base_dens_inp.text())
            result = ((fact_milk*fact_den)/base_den)
            self.milk_sale_ans.setText(round_number(result))
        else:
            self.show_message_box()

    def calc_pred(self):
        if self.milk_1_inp.text() and self.density_milk_inp.text():
            milk_1 = float(self.milk_1_inp.text())
            milk_den = float(self.density_milk_inp.text())
            result = milk_den * milk_1
            self.pred_score_ans.setText(round_number(result))
        else:
            self.show_message_box()

    def logout(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_win = Login_win()
    main_window = Main_win()
    web = QWebEngineView()
    login_win.show()
    sys.exit(app.exec())
