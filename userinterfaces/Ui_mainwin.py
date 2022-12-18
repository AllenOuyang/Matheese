/********************************************************************************
** Form generated from reading UI file 'mainwin.ui'
**
** Created by: Qt User Interface Compiler version 6.3.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWIN_H
#define UI_MAINWIN_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionFile;
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout_3;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label;
    QTabWidget *tabWidget;
    QWidget *Task1;
    QVBoxLayout *verticalLayout_2;
    QLabel *label_10;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_2;
    QLineEdit *function1;
    QHBoxLayout *horizontalLayout_4;
    QLabel *label_4;
    QLineEdit *function2;
    QHBoxLayout *horizontalLayout_5;
    QLabel *label_3;
    QLineEdit *function3;
    QHBoxLayout *horizontalLayout_14;
    QHBoxLayout *horizontalLayout_6;
    QLabel *label_5;
    QLineEdit *arange1;
    QHBoxLayout *horizontalLayout_7;
    QLabel *label_6;
    QLineEdit *brange1;
    QHBoxLayout *horizontalLayout_8;
    QLabel *label_13;
    QLineEdit *arange2;
    QHBoxLayout *horizontalLayout_11;
    QLabel *label_14;
    QLineEdit *brange2;
    QHBoxLayout *horizontalLayout_12;
    QLabel *label_15;
    QLineEdit *arange3;
    QHBoxLayout *horizontalLayout_13;
    QLabel *label_16;
    QLineEdit *brange3;
    QWidget *Task2;
    QVBoxLayout *verticalLayout_4;
    QLabel *label_11;
    QHBoxLayout *horizontalLayout_9;
    QLabel *label_7;
    QLineEdit *function2d;
    QLabel *label_17;
    QLineEdit *startpoint;
    QLabel *label_23;
    QLineEdit *xx;
    QLabel *label_20;
    QLineEdit *yy;
    QHBoxLayout *horizontalLayout_15;
    QLabel *label_18;
    QLineEdit *grx;
    QLabel *label_22;
    QLineEdit *gry;
    QSpacerItem *verticalSpacer;
    QWidget *Task3;
    QVBoxLayout *verticalLayout;
    QLabel *label_12;
    QTabWidget *TypeTap;
    QWidget *Type1;
    QVBoxLayout *verticalLayout_5;
    QHBoxLayout *horizontalLayout_10;
    QLabel *label_8;
    QLineEdit *rightpart;
    QLabel *label_26;
    QLineEdit *interval1;
    QLabel *label_9;
    QComboBox *comboBox;
    QSpacerItem *verticalSpacer_2;
    QWidget *Type2;
    QVBoxLayout *verticalLayout_6;
    QHBoxLayout *horizontalLayout_16;
    QLabel *label_19;
    QLineEdit *rightpart_2;
    QLabel *label_27;
    QLineEdit *interval2;
    QLabel *label_21;
    QComboBox *comboBox_2;
    QSpacerItem *verticalSpacer_3;
    QHBoxLayout *horizontalLayout;
    QPushButton *button;
    QMenuBar *menubar;
    QMenu *menu;
    QMenu *menuHelp;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(639, 633);
        MainWindow->setMinimumSize(QSize(600, 0));
        MainWindow->setMaximumSize(QSize(16777215, 16777215));
        QIcon icon;
        icon.addFile(QString::fromUtf8("../../../../Desktop/nailao.png"), QSize(), QIcon::Normal, QIcon::Off);
        icon.addFile(QString::fromUtf8("../../../../Desktop/nailao.png"), QSize(), QIcon::Normal, QIcon::On);
        MainWindow->setWindowIcon(icon);
        actionFile = new QAction(MainWindow);
        actionFile->setObjectName(QString::fromUtf8("actionFile"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        verticalLayout_3 = new QVBoxLayout(centralwidget);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label = new QLabel(centralwidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setEnabled(true);
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(label->sizePolicy().hasHeightForWidth());
        label->setSizePolicy(sizePolicy);
        label->setMinimumSize(QSize(385, 110));
        label->setMaximumSize(QSize(285, 110));
        label->setTextFormat(Qt::PlainText);
        label->setPixmap(QPixmap(QString::fromUtf8(":/resource/cheesemath1.png")));
        label->setScaledContents(true);
        label->setWordWrap(false);

        horizontalLayout_2->addWidget(label);


        verticalLayout_3->addLayout(horizontalLayout_2);

        tabWidget = new QTabWidget(centralwidget);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setEnabled(true);
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(tabWidget->sizePolicy().hasHeightForWidth());
        tabWidget->setSizePolicy(sizePolicy1);
        tabWidget->setMinimumSize(QSize(0, 0));
        tabWidget->setMaximumSize(QSize(16777215, 16777215));
        tabWidget->setTabletTracking(false);
        tabWidget->setLayoutDirection(Qt::LeftToRight);
        tabWidget->setTabShape(QTabWidget::Rounded);
        Task1 = new QWidget();
        Task1->setObjectName(QString::fromUtf8("Task1"));
        verticalLayout_2 = new QVBoxLayout(Task1);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        label_10 = new QLabel(Task1);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(label_10->sizePolicy().hasHeightForWidth());
        label_10->setSizePolicy(sizePolicy2);
        label_10->setTextFormat(Qt::MarkdownText);
        label_10->setScaledContents(true);

        verticalLayout_2->addWidget(label_10);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        label_2 = new QLabel(Task1);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        QFont font;
        font.setFamilies({QString::fromUtf8("Times New Roman")});
        font.setPointSize(18);
        font.setItalic(true);
        label_2->setFont(font);
        label_2->setTextFormat(Qt::AutoText);

        horizontalLayout_3->addWidget(label_2);

        function1 = new QLineEdit(Task1);
        function1->setObjectName(QString::fromUtf8("function1"));
        QFont font1;
        font1.setFamilies({QString::fromUtf8(".AppleSystemUIFont")});
        function1->setFont(font1);

        horizontalLayout_3->addWidget(function1);


        verticalLayout_2->addLayout(horizontalLayout_3);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        label_4 = new QLabel(Task1);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setFont(font);

        horizontalLayout_4->addWidget(label_4);

        function2 = new QLineEdit(Task1);
        function2->setObjectName(QString::fromUtf8("function2"));

        horizontalLayout_4->addWidget(function2);


        verticalLayout_2->addLayout(horizontalLayout_4);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        label_3 = new QLabel(Task1);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setFont(font);

        horizontalLayout_5->addWidget(label_3);

        function3 = new QLineEdit(Task1);
        function3->setObjectName(QString::fromUtf8("function3"));

        horizontalLayout_5->addWidget(function3);


        verticalLayout_2->addLayout(horizontalLayout_5);

        horizontalLayout_14 = new QHBoxLayout();
        horizontalLayout_14->setObjectName(QString::fromUtf8("horizontalLayout_14"));
        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        label_5 = new QLabel(Task1);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        sizePolicy.setHeightForWidth(label_5->sizePolicy().hasHeightForWidth());
        label_5->setSizePolicy(sizePolicy);
        label_5->setFont(font);

        horizontalLayout_6->addWidget(label_5);

        arange1 = new QLineEdit(Task1);
        arange1->setObjectName(QString::fromUtf8("arange1"));
        sizePolicy2.setHeightForWidth(arange1->sizePolicy().hasHeightForWidth());
        arange1->setSizePolicy(sizePolicy2);

        horizontalLayout_6->addWidget(arange1);


        horizontalLayout_14->addLayout(horizontalLayout_6);

        horizontalLayout_7 = new QHBoxLayout();
        horizontalLayout_7->setObjectName(QString::fromUtf8("horizontalLayout_7"));
        label_6 = new QLabel(Task1);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        sizePolicy.setHeightForWidth(label_6->sizePolicy().hasHeightForWidth());
        label_6->setSizePolicy(sizePolicy);
        label_6->setFont(font);

        horizontalLayout_7->addWidget(label_6);

        brange1 = new QLineEdit(Task1);
        brange1->setObjectName(QString::fromUtf8("brange1"));
        sizePolicy2.setHeightForWidth(brange1->sizePolicy().hasHeightForWidth());
        brange1->setSizePolicy(sizePolicy2);

        horizontalLayout_7->addWidget(brange1);


        horizontalLayout_14->addLayout(horizontalLayout_7);

        horizontalLayout_8 = new QHBoxLayout();
        horizontalLayout_8->setObjectName(QString::fromUtf8("horizontalLayout_8"));
        label_13 = new QLabel(Task1);
        label_13->setObjectName(QString::fromUtf8("label_13"));
        sizePolicy.setHeightForWidth(label_13->sizePolicy().hasHeightForWidth());
        label_13->setSizePolicy(sizePolicy);
        label_13->setFont(font);

        horizontalLayout_8->addWidget(label_13);

        arange2 = new QLineEdit(Task1);
        arange2->setObjectName(QString::fromUtf8("arange2"));
        sizePolicy2.setHeightForWidth(arange2->sizePolicy().hasHeightForWidth());
        arange2->setSizePolicy(sizePolicy2);

        horizontalLayout_8->addWidget(arange2);


        horizontalLayout_14->addLayout(horizontalLayout_8);

        horizontalLayout_11 = new QHBoxLayout();
        horizontalLayout_11->setObjectName(QString::fromUtf8("horizontalLayout_11"));
        label_14 = new QLabel(Task1);
        label_14->setObjectName(QString::fromUtf8("label_14"));
        sizePolicy.setHeightForWidth(label_14->sizePolicy().hasHeightForWidth());
        label_14->setSizePolicy(sizePolicy);
        label_14->setFont(font);

        horizontalLayout_11->addWidget(label_14);

        brange2 = new QLineEdit(Task1);
        brange2->setObjectName(QString::fromUtf8("brange2"));
        sizePolicy2.setHeightForWidth(brange2->sizePolicy().hasHeightForWidth());
        brange2->setSizePolicy(sizePolicy2);

        horizontalLayout_11->addWidget(brange2);


        horizontalLayout_14->addLayout(horizontalLayout_11);

        horizontalLayout_12 = new QHBoxLayout();
        horizontalLayout_12->setObjectName(QString::fromUtf8("horizontalLayout_12"));
        label_15 = new QLabel(Task1);
        label_15->setObjectName(QString::fromUtf8("label_15"));
        sizePolicy.setHeightForWidth(label_15->sizePolicy().hasHeightForWidth());
        label_15->setSizePolicy(sizePolicy);
        label_15->setFont(font);

        horizontalLayout_12->addWidget(label_15);

        arange3 = new QLineEdit(Task1);
        arange3->setObjectName(QString::fromUtf8("arange3"));
        sizePolicy2.setHeightForWidth(arange3->sizePolicy().hasHeightForWidth());
        arange3->setSizePolicy(sizePolicy2);

        horizontalLayout_12->addWidget(arange3);


        horizontalLayout_14->addLayout(horizontalLayout_12);

        horizontalLayout_13 = new QHBoxLayout();
        horizontalLayout_13->setObjectName(QString::fromUtf8("horizontalLayout_13"));
        label_16 = new QLabel(Task1);
        label_16->setObjectName(QString::fromUtf8("label_16"));
        sizePolicy.setHeightForWidth(label_16->sizePolicy().hasHeightForWidth());
        label_16->setSizePolicy(sizePolicy);
        label_16->setFont(font);

        horizontalLayout_13->addWidget(label_16);

        brange3 = new QLineEdit(Task1);
        brange3->setObjectName(QString::fromUtf8("brange3"));
        sizePolicy2.setHeightForWidth(brange3->sizePolicy().hasHeightForWidth());
        brange3->setSizePolicy(sizePolicy2);

        horizontalLayout_13->addWidget(brange3);


        horizontalLayout_14->addLayout(horizontalLayout_13);


        verticalLayout_2->addLayout(horizontalLayout_14);

        tabWidget->addTab(Task1, QString());
        Task2 = new QWidget();
        Task2->setObjectName(QString::fromUtf8("Task2"));
        verticalLayout_4 = new QVBoxLayout(Task2);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        label_11 = new QLabel(Task2);
        label_11->setObjectName(QString::fromUtf8("label_11"));
        label_11->setTextFormat(Qt::MarkdownText);

        verticalLayout_4->addWidget(label_11);

        horizontalLayout_9 = new QHBoxLayout();
        horizontalLayout_9->setObjectName(QString::fromUtf8("horizontalLayout_9"));
        label_7 = new QLabel(Task2);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setFont(font);

        horizontalLayout_9->addWidget(label_7);

        function2d = new QLineEdit(Task2);
        function2d->setObjectName(QString::fromUtf8("function2d"));

        horizontalLayout_9->addWidget(function2d);

        label_17 = new QLabel(Task2);
        label_17->setObjectName(QString::fromUtf8("label_17"));
        QFont font2;
        font2.setFamilies({QString::fromUtf8("Times New Roman")});
        font2.setPointSize(18);
        font2.setBold(false);
        font2.setItalic(true);
        label_17->setFont(font2);

        horizontalLayout_9->addWidget(label_17);

        startpoint = new QLineEdit(Task2);
        startpoint->setObjectName(QString::fromUtf8("startpoint"));
        startpoint->setMaximumSize(QSize(60, 16777215));

        horizontalLayout_9->addWidget(startpoint);

        label_23 = new QLabel(Task2);
        label_23->setObjectName(QString::fromUtf8("label_23"));
        label_23->setFont(font);

        horizontalLayout_9->addWidget(label_23);

        xx = new QLineEdit(Task2);
        xx->setObjectName(QString::fromUtf8("xx"));
        xx->setMaximumSize(QSize(60, 16777215));

        horizontalLayout_9->addWidget(xx);

        label_20 = new QLabel(Task2);
        label_20->setObjectName(QString::fromUtf8("label_20"));
        label_20->setFont(font);

        horizontalLayout_9->addWidget(label_20);

        yy = new QLineEdit(Task2);
        yy->setObjectName(QString::fromUtf8("yy"));
        yy->setMaximumSize(QSize(60, 16777215));

        horizontalLayout_9->addWidget(yy);


        verticalLayout_4->addLayout(horizontalLayout_9);

        horizontalLayout_15 = new QHBoxLayout();
        horizontalLayout_15->setObjectName(QString::fromUtf8("horizontalLayout_15"));
        label_18 = new QLabel(Task2);
        label_18->setObjectName(QString::fromUtf8("label_18"));
        label_18->setFont(font);

        horizontalLayout_15->addWidget(label_18);

        grx = new QLineEdit(Task2);
        grx->setObjectName(QString::fromUtf8("grx"));

        horizontalLayout_15->addWidget(grx);

        label_22 = new QLabel(Task2);
        label_22->setObjectName(QString::fromUtf8("label_22"));
        label_22->setFont(font);

        horizontalLayout_15->addWidget(label_22);

        gry = new QLineEdit(Task2);
        gry->setObjectName(QString::fromUtf8("gry"));

        horizontalLayout_15->addWidget(gry);


        verticalLayout_4->addLayout(horizontalLayout_15);

        verticalSpacer = new QSpacerItem(20, 90, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_4->addItem(verticalSpacer);

        tabWidget->addTab(Task2, QString());
        Task3 = new QWidget();
        Task3->setObjectName(QString::fromUtf8("Task3"));
        verticalLayout = new QVBoxLayout(Task3);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        label_12 = new QLabel(Task3);
        label_12->setObjectName(QString::fromUtf8("label_12"));
        label_12->setTextFormat(Qt::MarkdownText);

        verticalLayout->addWidget(label_12);

        TypeTap = new QTabWidget(Task3);
        TypeTap->setObjectName(QString::fromUtf8("TypeTap"));
        Type1 = new QWidget();
        Type1->setObjectName(QString::fromUtf8("Type1"));
        verticalLayout_5 = new QVBoxLayout(Type1);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        horizontalLayout_10 = new QHBoxLayout();
        horizontalLayout_10->setObjectName(QString::fromUtf8("horizontalLayout_10"));
        label_8 = new QLabel(Type1);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setFont(font);

        horizontalLayout_10->addWidget(label_8);

        rightpart = new QLineEdit(Type1);
        rightpart->setObjectName(QString::fromUtf8("rightpart"));

        horizontalLayout_10->addWidget(rightpart);

        label_26 = new QLabel(Type1);
        label_26->setObjectName(QString::fromUtf8("label_26"));
        label_26->setFont(font);

        horizontalLayout_10->addWidget(label_26);

        interval1 = new QLineEdit(Type1);
        interval1->setObjectName(QString::fromUtf8("interval1"));
        interval1->setMaximumSize(QSize(70, 16777215));

        horizontalLayout_10->addWidget(interval1);

        label_9 = new QLabel(Type1);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setFont(font);

        horizontalLayout_10->addWidget(label_9);

        comboBox = new QComboBox(Type1);
        comboBox->addItem(QString());
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        horizontalLayout_10->addWidget(comboBox);


        verticalLayout_5->addLayout(horizontalLayout_10);

        verticalSpacer_2 = new QSpacerItem(20, 81, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_5->addItem(verticalSpacer_2);

        TypeTap->addTab(Type1, QString());
        Type2 = new QWidget();
        Type2->setObjectName(QString::fromUtf8("Type2"));
        verticalLayout_6 = new QVBoxLayout(Type2);
        verticalLayout_6->setObjectName(QString::fromUtf8("verticalLayout_6"));
        horizontalLayout_16 = new QHBoxLayout();
        horizontalLayout_16->setObjectName(QString::fromUtf8("horizontalLayout_16"));
        label_19 = new QLabel(Type2);
        label_19->setObjectName(QString::fromUtf8("label_19"));
        label_19->setFont(font);

        horizontalLayout_16->addWidget(label_19);

        rightpart_2 = new QLineEdit(Type2);
        rightpart_2->setObjectName(QString::fromUtf8("rightpart_2"));

        horizontalLayout_16->addWidget(rightpart_2);

        label_27 = new QLabel(Type2);
        label_27->setObjectName(QString::fromUtf8("label_27"));
        label_27->setFont(font);

        horizontalLayout_16->addWidget(label_27);

        interval2 = new QLineEdit(Type2);
        interval2->setObjectName(QString::fromUtf8("interval2"));
        interval2->setMaximumSize(QSize(70, 16777215));

        horizontalLayout_16->addWidget(interval2);

        label_21 = new QLabel(Type2);
        label_21->setObjectName(QString::fromUtf8("label_21"));
        label_21->setFont(font);

        horizontalLayout_16->addWidget(label_21);

        comboBox_2 = new QComboBox(Type2);
        comboBox_2->addItem(QString());
        comboBox_2->setObjectName(QString::fromUtf8("comboBox_2"));

        horizontalLayout_16->addWidget(comboBox_2);


        verticalLayout_6->addLayout(horizontalLayout_16);

        verticalSpacer_3 = new QSpacerItem(20, 103, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_6->addItem(verticalSpacer_3);

        TypeTap->addTab(Type2, QString());

        verticalLayout->addWidget(TypeTap);

        tabWidget->addTab(Task3, QString());

        verticalLayout_3->addWidget(tabWidget);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        button = new QPushButton(centralwidget);
        button->setObjectName(QString::fromUtf8("button"));
        sizePolicy.setHeightForWidth(button->sizePolicy().hasHeightForWidth());
        button->setSizePolicy(sizePolicy);
        button->setMinimumSize(QSize(100, 0));

        horizontalLayout->addWidget(button);


        verticalLayout_3->addLayout(horizontalLayout);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 639, 24));
        menu = new QMenu(menubar);
        menu->setObjectName(QString::fromUtf8("menu"));
        menuHelp = new QMenu(menubar);
        menuHelp->setObjectName(QString::fromUtf8("menuHelp"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menu->menuAction());
        menubar->addAction(menuHelp->menuAction());

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(2);
        TypeTap->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "Matheese", nullptr));
        actionFile->setText(QCoreApplication::translate("MainWindow", "File", nullptr));
        label->setText(QString());
        label_10->setText(QCoreApplication::translate("MainWindow", "## Task description\n"
"This part is to calculate the area of the area surrounded by 3 functions.\n"
"## Argument reqirements\n"
" **f(x), g(x), h(x)**: Three funtion expressions. \n"
"\n"
" **a1,  b1**: range of the intersect [a1,  b1] of f and g.\n"
"\n"
" **a2, b2**: range of the intersect [a2, b2] of f and h. \n"
"\n"
" **a3, b3**: range of the intersect [a3, b3] of g and h.", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "f (x):", nullptr));
        function1->setPlaceholderText(QCoreApplication::translate("MainWindow", "Enter 1st function", nullptr));
        label_4->setText(QCoreApplication::translate("MainWindow", "g(x):", nullptr));
        function2->setPlaceholderText(QCoreApplication::translate("MainWindow", "Enter 2nd function", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "h(x):", nullptr));
        function3->setPlaceholderText(QCoreApplication::translate("MainWindow", "Enter 3rd function", nullptr));
        label_5->setText(QCoreApplication::translate("MainWindow", "a1:", nullptr));
        arange1->setPlaceholderText(QCoreApplication::translate("MainWindow", "Enter left border", nullptr));
        label_6->setText(QCoreApplication::translate("MainWindow", "b1:", nullptr));
        brange1->setPlaceholderText(QCoreApplication::translate("MainWindow", "Enter right border", nullptr));
        label_13->setText(QCoreApplication::translate("MainWindow", "a2:", nullptr));
        arange2->setPlaceholderText(QCoreApplication::translate("MainWindow", "Enter left border", nullptr));
        label_14->setText(QCoreApplication::translate("MainWindow", "b2:", nullptr));
        brange2->setPlaceholderText(QCoreApplication::translate("MainWindow", "Enter right border", nullptr));
        label_15->setText(QCoreApplication::translate("MainWindow", "a3:", nullptr));
        arange3->setPlaceholderText(QCoreApplication::translate("MainWindow", "Enter left border", nullptr));
        label_16->setText(QCoreApplication::translate("MainWindow", "b3:", nullptr));
        brange3->setPlaceholderText(QCoreApplication::translate("MainWindow", "Enter right border", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(Task1), QCoreApplication::translate("MainWindow", "Task 1", nullptr));
        label_11->setText(QCoreApplication::translate("MainWindow", "## Task description\n"
"This part is to calculate the minimum of a function. \n"
"## Argument reqirements\n"
" **f(x,y)**: Funtion expression. \n"
"\n"
" **Origin(x,y)**: The start point. \n"
"\n"
" **[x0, x1]**: [x0, x1] is plot area. \n"
"\n"
" **[y0, y1]**: [y0, y1] is plot area. \n"
"\n"
" **Gradxf(x,y)**: Derivative of f(x,y) by x. \n"
"\n"
" **Gradyf(x,y):** Derivative of f(x,y) by y.", nullptr));
        label_7->setText(QCoreApplication::translate("MainWindow", "f(x, y):", nullptr));
        function2d->setPlaceholderText(QCoreApplication::translate("MainWindow", "Enter function", nullptr));
        label_17->setText(QCoreApplication::translate("MainWindow", "(x,y):", nullptr));
        label_23->setText(QCoreApplication::translate("MainWindow", "[x0, x1]:", nullptr));
        label_20->setText(QCoreApplication::translate("MainWindow", "[y0, y1]:", nullptr));
        label_18->setText(QCoreApplication::translate("MainWindow", "Gradxf(x,y):", nullptr));
        label_22->setText(QCoreApplication::translate("MainWindow", "Gradyf(x,y):", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(Task2), QCoreApplication::translate("MainWindow", "Task 2", nullptr));
        label_12->setText(QCoreApplication::translate("MainWindow", "## Task description\n"
"This part is to calculate the minimum of a function. \n"
"## Argument reqirements\n"
" **f(x)**: Right hand function. \n"
"\n"
" **Tips:** You can choose the Core function K(x, s)", nullptr));
        label_8->setText(QCoreApplication::translate("MainWindow", "f(x):", nullptr));
        rightpart->setText(QString());
        rightpart->setPlaceholderText(QCoreApplication::translate("MainWindow", "Enter right part", nullptr));
        label_26->setText(QCoreApplication::translate("MainWindow", "Interval:", nullptr));
        label_9->setText(QCoreApplication::translate("MainWindow", "Core:", nullptr));
        comboBox->setItemText(0, QCoreApplication::translate("MainWindow", "(default)", nullptr));

        TypeTap->setTabText(TypeTap->indexOf(Type1), QCoreApplication::translate("MainWindow", "Type 1", nullptr));
        label_19->setText(QCoreApplication::translate("MainWindow", "f(x):", nullptr));
        rightpart_2->setText(QString());
        rightpart_2->setPlaceholderText(QCoreApplication::translate("MainWindow", "Enter right part", nullptr));
        label_27->setText(QCoreApplication::translate("MainWindow", "Interval:", nullptr));
        label_21->setText(QCoreApplication::translate("MainWindow", "Core:", nullptr));
        comboBox_2->setItemText(0, QCoreApplication::translate("MainWindow", "(default)", nullptr));

        TypeTap->setTabText(TypeTap->indexOf(Type2), QCoreApplication::translate("MainWindow", "Type 2", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(Task3), QCoreApplication::translate("MainWindow", "Task 3", nullptr));
        button->setText(QCoreApplication::translate("MainWindow", "Go", nullptr));
        menu->setTitle(QCoreApplication::translate("MainWindow", "File", nullptr));
        menuHelp->setTitle(QCoreApplication::translate("MainWindow", "Help", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWIN_H
