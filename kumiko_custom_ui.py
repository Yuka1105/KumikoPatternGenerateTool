#coding: utf-8
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2 import QtWidgets, QtCore, QtGui
from functools import partial
import hou

lsystem_node = hou.node('/obj/Kumiko-geometry/Kumiko_L-System') # L-systemノード
rule_file_path = 'C:/Users/komeda/Desktop/rules.txt' # ルールファイルパス
# ルール
rule = []
rule.append("A = g(v)B(0)\nB(i):i<6 = g(v)+(30)[f(1)+(60)C]+(30)B(i+1)\nC=g(v)[F(1)+(180)D][+(60)E(1)][+(120)F(1)+(180)D][+(180)E(1)][+(240)F(1)+(180)D][+(300)E(1)]\nD=g(v)[+(30)F(0.5/0.57735)][-(30)F(0.5/0.57735)]\nE=g(v)F(0.154701/0.57735)G\nG=g(v)[+(75)F(0.51763797/0.57735)][-(75)F(0.51763797/0.57735)]\n")
rule.append("A = g(v)B(0)\nB(i):i<6 = g(v)+(30)[f(1)+(60)C]+(30)B(i+1)\nC=g(v)[f(1*0.5)D][+(120)f(1*0.5)D][+(240)f(1*0.5)D]\nD=g(v)[+(150)F(0.25/0.57735)][-(150)F(0.25/0.57735)]F(1*0.5)E\nE=g(v)[+(150)F(0.5/0.57735)G][-(150)F(0.5/0.57735)]\nG=g(v)+(60)F(0.5/0.57735)\n")
rule.append("A = g(v)B(0)\nB(i):i<6 = g(v)+(30)[f(1)+(60)C]+(30)B(i+1)\nC=g(v)[f(1)+(180)D][+(120)f(1)+(180)D][+(240)f(1)+(180)D]\nD=g(v)[+(30)F(0.5/0.57735)][-(30)F(0.5/0.57735)]E\nE=g(v)[-(10)F(0.5320886/0.57735)G][+(10)F(0.5320886/0.57735)]\nG=g(v)+(40)F(0.184793/0.57735)\n")
rule.append("A = g(v)B(0)\nB(i):i<6 = g(v)+(30)[f(1)+(60)C]+(30)B(i+1)\nC=g(v)[f(1)D(1)][+(120)f(1)D(1)][+(240)f(1)D(1)]\nD=g(v)+(150)F(0.8/0.57735)[E]F(0.2/0.57735)\nE=g(v)+(120)F(0.8*0.25/0.57735)G\nG=g(v)+(60)F(0.8*0.5/0.57735)\n")
rule.append("A = g(v)B(0)\nB(i):i<6 = g(v)+(30)[f(1)+(60)C]+(30)B(i+1)\nC=g(v)[f(1*0.2)[E]F(1*0.8)D][+(120)f(1*0.2)[E]F(1*0.8)D][+(240)f(1*0.2)[E]F(1*0.8)D]\nD=g(v)[+(150)F(0.5/0.57735)][-(150)F(0.5/0.57735)]\nE=g(v)G\nG=g(v)[+(120)F(0.46188/0.57735)][-(120)F(0.46188/0.57735)]\n")
rule.append("A = g(v)+(30)[f(1)+(60)B(1)][+(60)f(1)+(60)B(1)][+(120)f(1)+(60)B(1)][-(60)f(1)+(60)B(1)][-(120)f(1)+(60)B(1)][+(180)f(1)+(60)B(1)]\nB(1)=g(v)[F(1)+(180)C][+(60)D(1)][+(120)F(1)+(180)C][+(180)D(1)][+(240)F(1)+(180)C][+(300)D(1)]\nC=g(v)[+(30)F(0.5 / 0.57735)][-(30)F(0.5/ 0.57735)]\nD(1)=g(v)F(0.154701 / 0.57735)E\nE=g(v)[+(75)F(0.51763797 / 0.57735)][-(75)F(0.51763797 / 0.57735)]\n")
rule.append("A = g(v)+(30)[f(1)+(60)B(1)][+(60)f(1)+(60)B(1)][+(120)f(1)+(60)B(1)][-(60)f(1)+(60)B(1)][-(120)f(1)+(60)B(1)][+(180)f(1)+(60)B(1)]\nB = g(v)[f(0.5)C(1)][+(120)f(0.5)C(1)][+(240)f(0.5)C(1)]\nC(1)=g(v)[+(150)F(0.25 / 0.57735)][-(150)F(0.25 / 0.57735)]F(0.5)D(1)\nD(1)=g(v)[+(150)F(0.5/0.57735)E][-(150)F(0.5/0.57735)]\nE=g(v)+(60)F(0.5/0.57735)\n")
rule.append("A = g(v)+(30)[f(1)+(60)B(1)][+(60)f(1)+(60)B(1)][+(120)f(1)+(60)B(1)][-(60)f(1)+(60)B(1)][-(120)f(1)+(60)B(1)][+(180)f(1)+(60)B(1)]\nB(1)=g(v)[f(1)+(180)C][+(120)f(1)+(180)C][+(240)f(1)+(180)C]\nC=g(v)[+(30)F(0.5 / 0.57735)][-(30)F(0.5 / 0.57735)]D\nD=g(v)[-(10)F(0.5320886 / 0.57735)E][+(10)F(0.5320886 / 0.57735)]\nE=g(v)+(40)F(0.184793 / 0.57735)\n")
rule.append("A = g(v)+(30)[f(1)+(60)B(1)][+(60)f(1)+(60)B(1)][+(120)f(1)+(60)B(1)][-(60)f(1)+(60)B(1)][-(120)f(1)+(60)B(1)][+(180)f(1)+(60)B(1)]\nB=g(v)[f(1)C(1)][+(120)f(1)C(1)][+(240)f(1)C(1)]\nC=g(v)+(150)F(0.8 / 0.57735)[D]F(0.2 / 0.57735)\nD=g(v)+(120)F(0.8*0.25 / 0.57735)E\nE=g(v)+(60)F(0.8*0.5 / 0.57735)\n")
rule.append("A = g(v)+(30)[f(1)+(60)B(1)][+(60)f(1)+(60)B(1)][+(120)f(1)+(60)B(1)][-(60)f(1)+(60)B(1)][-(120)f(1)+(60)B(1)][+(180)f(1)+(60)B(1)]\nB(1)=g(v)[f(1*0.2)[D(1)]F(1*0.8)C(1)][+(120)f(1*0.2)[D(1)]F(1*0.8)C(1)][+(240)f(1*0.2)[D(1)]F(1*0.8)C(1)]\nC(1)=g(v)[+(150)F(0.5 / 0.57735)][-(150)F(0.5 / 0.57735)]\nD(1)=g(v)E(1)\nE(1)=g(v)[+(120)F(0.46188 / 0.57735)][-(120)F(0.46188 / 0.57735)]\n")
rule.append("A = g(v)[F(0.57735*3)B(0.57735*3)][+(60)F(0.57735*3)E(0.57735*3)][+(120)F(0.57735*3)B(0.57735*3)][-(60)F(0.57735*3)E(0.57735*3)][-(120)F(0.57735*3)B(0.57735*3)][+(180)F(0.57735*3)E(0.57735*3)]\nB(0.57735*3) = g(v)+(120)F(0.57735*3)C(0.57735*3)\nC(0.57735*3) = g(v)[+(105)F(0.57735*3*0.896521)][-(225)F(0.57735*3*0.896521)]\nD(0.57735*3) = g(v)+(120)F(0.57735*3)C(0.57735*3)\nE(0.57735*3) = g(v)D(0.57735*3)\n")
beforeAlf = ["A","B","C","D","E","G"] # 置き換える前のアルファベット
afterAlf = ["H","I","J","K","L","N","M","O","P","Q","R","S","T","U","V","W","Y","Z"] # 置き換えた後のアルファベット
groupNum = ["0","1","2"] # 模様ごとにグループ分けするための数字
checkbox_states = [False] * len(rule) # チェックボックスのオンオフ
output = "A(i) = [X][B(i)][C(i,1)][D(i,1)][E(i)]\nB(i) = +(30)f(i*3)-(30)[X][B(i)][C(i,0)][D(i,0)]\nC(i,j):j=0 = -(30)f(i*3)+(30)[X][C(i,0)]\nC(i,j):j=1 = -(30)f(i*3)+(30)[X][C(i,1)][E(i)]\nD(i,j):j=0 = +(150)f(i*3)-(150)[X][D(i,0)]\nD(i,j):j=1 = +(150)f(i*3)-(150)[X][D(i,1)][E(i)]\nE(i) = -(150)f(i*3)+(150)[X][E(i)]\n" # ルールファイルに出力するテキスト

# チェックボックスがON、OFFされたときに実行される関数
def click_checkbox(checkbox_index):
    def on_state_change(state):
        global checkbox_states
        if state == 0:
            checkbox_states[checkbox_index] = False
        if state == 2:
            checkbox_states[checkbox_index] = True
    return on_state_change

# ボタンが押されたときに実行される関数
def click_button():
    global rule
    global beforeAlf
    global afterAlf
    global checkbox_states
    global output
    tmp_rule = "" # ルールファイルの一時的なコピー先
    selected_pattern = [] # 選択された模様の番号
    firstAlf = [] # 各模様ルールで一番最初に使われたアルファベット
    int_probability = [] # int型の出現確率(0~100)
    float_probability = [] # float型の出現確率(0.0~1.0)
    probability_sum = 0 # 出現確率の合計値
    rule_num = 0 # 実際に適用するルールの番号（順に0から2が入る）
    for i in range(len(rule)):
        # チェックボックスがオンだった場合
        if checkbox_states[i]:
            int_probability.append(int(spinboxes[i].cleanText()))
            float_probability.append(float(spinboxes[i].cleanText())/100)
            tmp_rule = rule[i]
            # アルファベットの置き換え
            for j in range(len(beforeAlf)):
                if j == 0:
                    if len(afterAlf) > 0:
                        firstAlf.append(afterAlf[0])
                    else:
                        print("模様は3つまで選択可能です。")
                        output = "A(i) = [X][B(i)][C(i,1)][D(i,1)][E(i)]\nB(i) = +(30)f(i*3)-(30)[X][B(i)][C(i,0)][D(i,0)]\nC(i,j):j=0 = -(30)f(i*3)+(30)[X][C(i,0)]\nC(i,j):j=1 = -(30)f(i*3)+(30)[X][C(i,1)][E(i)]\nD(i,j):j=0 = +(150)f(i*3)-(150)[X][D(i,0)]\nD(i,j):j=1 = +(150)f(i*3)-(150)[X][D(i,1)][E(i)]\nE(i) = -(150)f(i*3)+(150)[X][E(i)]\n"
                        afterAlf = ["H","I","J","K","L","N","M","O","P","Q","R","S","T","U","V","W","Y","Z"]
                        return
                if beforeAlf[j] not in tmp_rule:
                    break
                if len(afterAlf) > 0:
                    replacement = afterAlf[0] # 先頭文字を取得
                    afterAlf = afterAlf[1:] # 先頭文字を削除
                    tmp_rule = tmp_rule.replace(beforeAlf[j], replacement)
                else:
                    print("模様は3つまで選択可能です。")
                    output = "A(i) = [X][B(i)][C(i,1)][D(i,1)][E(i)]\nB(i) = +(30)f(i*3)-(30)[X][B(i)][C(i,0)][D(i,0)]\nC(i,j):j=0 = -(30)f(i*3)+(30)[X][C(i,0)]\nC(i,j):j=1 = -(30)f(i*3)+(30)[X][C(i,1)][E(i)]\nD(i,j):j=0 = +(150)f(i*3)-(150)[X][D(i,0)]\nD(i,j):j=1 = +(150)f(i*3)-(150)[X][D(i,1)][E(i)]\nE(i) = -(150)f(i*3)+(150)[X][E(i)]\n"
                    afterAlf = ["H","I","J","K","L","N","M","O","P","Q","R","S","T","U","V","W","Y","Z"]
                    return
            tmp_rule = tmp_rule.replace("v", groupNum[rule_num])
            output += tmp_rule
            rule_num += 1
    for i in range(len(int_probability)):
        probability_sum += int_probability[i]
        output += "X=" + firstAlf[i] + ":" + str(float_probability[i]) + "\n"
    if probability_sum == 100:
        # ファイルを開き上書き
        with open(rule_file_path, 'w') as file:
            file.write(output)
        lsystem_node.parm('rulefile').set(rule_file_path)
        # 再適用時のために初期化
        output = "A(i) = [X][B(i)][C(i,1)][D(i,1)][E(i)]\nB(i) = +(30)f(i*3)-(30)[X][B(i)][C(i,0)][D(i,0)]\nC(i,j):j=0 = -(30)f(i*3)+(30)[X][C(i,0)]\nC(i,j):j=1 = -(30)f(i*3)+(30)[X][C(i,1)][E(i)]\nD(i,j):j=0 = +(150)f(i*3)-(150)[X][D(i,0)]\nD(i,j):j=1 = +(150)f(i*3)-(150)[X][D(i,1)][E(i)]\nE(i) = -(150)f(i*3)+(150)[X][E(i)]\n"
        afterAlf = ["H","I","J","K","L","N","M","O","P","Q","R","S","T","U","V","W","Y","Z"]
    else:
        print("出現確率の和が100%になるように設定してください。")
        output = "A(i) = [X][B(i)][C(i,1)][D(i,1)][E(i)]\nB(i) = +(30)f(i*3)-(30)[X][B(i)][C(i,0)][D(i,0)]\nC(i,j):j=0 = -(30)f(i*3)+(30)[X][C(i,0)]\nC(i,j):j=1 = -(30)f(i*3)+(30)[X][C(i,1)][E(i)]\nD(i,j):j=0 = +(150)f(i*3)-(150)[X][D(i,0)]\nD(i,j):j=1 = +(150)f(i*3)-(150)[X][D(i,1)][E(i)]\nE(i) = -(150)f(i*3)+(150)[X][E(i)]\n"
        afterAlf = ["H","I","J","K","L","N","M","O","P","Q","R","S","T","U","V","W","Y","Z"]

# ダイアログの作成
dialog = QWidget()
dialog.setParent(hou.qt.mainWindow(), Qt.Window)
# 画像の作成
image = QLabel()
image.setPixmap(QPixmap("C:/Users/komeda/Desktop/pattern_animation_image.png")) # 画像ファイルパス
# テキストの作成
note = QLabel()
note.setText('\n※ 模様は3つまで選択可。出現確率は和が100%になるよう設定してください。\n')
note_layout = QVBoxLayout()
note_layout.addWidget(note, alignment=QtCore.Qt.AlignHCenter)
# チェックボックスの作成
checkboxes = []
checkbox_labels = ["八重麻の葉(a)", "八重桔梗麻の葉(a)", "二重麻の葉(a)", "毘沙門剣つなぎ(a)", "八重桜(a)", "八重麻の葉(b)", "八重桔梗麻の葉(b)", "二重麻の葉(b)", "毘沙門剣つなぎ(b)", "八重桜(b)", "重ね竜胆(b)"]
for label in checkbox_labels:
    checkbox = QCheckBox(label)
    checkboxes.append(checkbox)
# チェックボックスの状態が変化したときに関連する関数を接続
for i, checkbox in enumerate(checkboxes):
    click_checkbox_function = click_checkbox(i)
    checkbox.stateChanged.connect(click_checkbox_function)
# ボタンの作成
button = QPushButton("適用")
button.clicked.connect(click_button)
button.setFixedWidth(150)
button.setFixedHeight(40)
button_layout = QVBoxLayout()
button_layout.addWidget(button, alignment=QtCore.Qt.AlignHCenter)
# スピンボックス、単位の作成
spinbox_units = []
spinboxes = []
for i in range(len(rule)):
    spinbox = QSpinBox()
    spinbox.setMinimum(0)
    spinbox.setMaximum(100)
    spinbox.setSingleStep(5)
    spinbox.setFixedWidth(60)
    spinboxes.append(spinbox)
    unit = QLabel()
    unit.setText('%')
    unit.setFixedWidth(15)
    spinbox_unit_layout = QHBoxLayout()
    spinbox_unit_layout.addWidget(spinbox)
    spinbox_unit_layout.addWidget(unit)
    spinbox_units.append(spinbox_unit_layout)
# 横並びレイアウトの作成
h_layouts = []
for i in range(len(rule)):
    h_layouts.append(QHBoxLayout())
# レイアウトにUIを追加
for i in range(len(rule)):
    h_layouts[i].addWidget(checkboxes[i])
    h_layouts[i].addLayout(spinbox_units[i])
# グループ分けの作成
group_box_a = QGroupBox("アニメーション(a)")
group_box_b = QGroupBox("アニメーション(b)")
# グループボックス内のウィジェットを配置するレイアウト
group_layout_a = QVBoxLayout()
group_layout_b = QVBoxLayout()
# レイアウトにUIを追加
for i in range(0, 5):
    group_layout_a.addLayout(h_layouts[i])
for i in range(5, 11):
    group_layout_b.addLayout(h_layouts[i])
# グループボックスにレイアウトを設定
group_box_a.setLayout(group_layout_a)
group_box_b.setLayout(group_layout_b)
# 縦並びレイアウトの作成
v_layout = QVBoxLayout()
# レイアウトにUIを追加
v_layout.addWidget(image)
v_layout.addLayout(note_layout)
v_layout.addWidget(group_box_a)
v_layout.addWidget(group_box_b)
v_layout.addLayout(button_layout)
# ダイアログにレイアウトを設定
dialog.setFixedWidth(521)
dialog.setFixedHeight(1230)
dialog.setLayout(v_layout)
# ダイアログの表示
dialog.show()