from myprogram import *
import sys
from PyQt5.QtWidgets import QDialog#, QApplication
from CAL import *
#导入，Qapplication，单行文本框，窗口，表单布局
from PyQt5.QtWidgets import QApplication#,QLineEdit,QWidget,QFormLayout
#导入文本校验器：整数校验器与浮点数校验器,其他自定义校验器
#from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
       # self.ui.closeWinBtn.clicked.connect(self.on_pushButton_clicked)
        self.ui.textBrowser.setText("请输入ORDER--整数\n若输入为字符，则闪退\norder:阶数，缺省值3\nepsilon:纹波(dB)，缺省值3"
                                    +"\nFl:通带下限截止频率，缺省值35000\nFu:通带上限截止频率，缺省值40000\n")
#        reg = QRegExp('[a-zA-Z0-9]+$')
        # 自定义文本验证器
#        QIntValidator = QRegExpValidator(self)
        # 设置属性
#        QIntValidator.setRegExp(reg)
#        self.ui.lineEdit.setValidator(QIntValidator)
#        super(MyForm, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
#        self.axes = self.fig.add_subplot(111)
        self.ui.page1Cal.clicked.connect(lambda:self.page1Cal(self.ui.lineEdit.text(),self.ui.lineEdit_epsilon.text(),self.ui.lineEdit_Fl.text(),self.ui.lineEdit_Fu.text()))
        self.ui.pushButton.clicked.connect(lambda:self.K_Cal(self.ui.plainTextEdit.toPlainText(),self.ui.plainTextEdit_2.toPlainText(),self.ui.plainTextEdit_3.toPlainText(),self.ui.plainTextEdit_4.toPlainText(),self.ui.plainTextEdit_5.toPlainText(),self.ui.plainTextEdit_6.toPlainText(),self.ui.plainTextEdit_7.toPlainText(),self.ui.plainTextEdit_8.toPlainText()))
        #self.ui.

#        self.ui.graphicsView.setGeometry()
        self.show();
    def page1Cal(self, order,epsilon, f1, f2):#下一步：限制输入内容
#        n=self.ui.lineEdit.text();
#        epsilon=(self.ui.lineEdit_epsilon.text());
        if order=='':
            order=3;
            self.ui.lineEdit.setText(str(order))
        if epsilon == '':#判断有无输入就用这种方式
            epsilon=3
            self.ui.lineEdit_epsilon.setText(str(epsilon))
        else:
            epsilon=float(epsilon)
        if f1 == '':
            f1=35000
            self.ui.lineEdit_Fl.setText(str(f1))
        if f2 == '':
            f2=40000
            self.ui.lineEdit_Fu.setText(str(f2))
        self.ui.textBrowser.clear();
        self.ui.textBrowser_2.clear();
        order = float(order);
        order = int(order)
        if order<0:
            order=3;
        self.ui.lineEdit.setText(str(order))
        (g, Z1, Z2) = gCal(order, epsilon, f1, f2) ; #Z1:even, Z2:odd
        for i in range(0,order+2):
            self.ui.textBrowser.append("G"+str(i)+"="+str(g[i].real))# append: display things one by one
        for i in range(0,order+1):
            self.ui.textBrowser_2.append("Even Mode"+str(i)+"="+str(Z1[i].real))
            self.ui.textBrowser_2.append("Odd Mode "+str(i)+"="+str(Z2[i].real))
    def K_Cal(self, a, b, c, d, e, f, g, h):
        if a=='':
            a=1;
            self.ui.plainTextEdit.insertPlainText(str(a))
        else:
            a=float(a)
        if b=='':
            b=1;
            self.ui.plainTextEdit_2.insertPlainText(str(b))
        else:
            b=float(b)
        if c=='':
            c=1;
            self.ui.plainTextEdit_3.insertPlainText(str(c))
        else:
            c=float(c)
        if d=='':
            d=1;
            self.ui.plainTextEdit_4.insertPlainText(str(d))
        else:
            d=float(d)
        if e=='':
            e=1
            self.ui.plainTextEdit_5.insertPlainText(str(e))
        else:
            e=float(e)
        if f=='':
            f=1;
            self.ui.plainTextEdit_6.insertPlainText(str(f))
        else:
            f=float(f)
        if g=='':
            g=1;
            self.ui.plainTextEdit_7.insertPlainText(str(g))
        else:
            g=float(g)
        if h=='':
            h=1;
            self.ui.plainTextEdit_8.insertPlainText(str(h))
        else:
            h=float(h)
        k=StableFactor_Cal(a,b,c,d,e,f,g,h);
        self.ui.label_12.setText("K="+str(k))
        if k <1:
            self.ui.label_17.setText("In this Condition, system is STABLE")
        else:
            if k==1:
                self.ui.label_17.setText("In this Condition, system is in CRITICAL STABLE CONDITION")
            else:
                self.ui.label_17.setText("In this Condition, system is UNSTABLE")
        #k=StableFactor_Cal()#StableFactor_Cal(a, b, c, d, e, f, g, h):#S11 S21 S12 S22



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
