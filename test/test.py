from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl

app = QApplication([])

# 创建一个 QWebEngineView 控件
web_view = QWebEngineView()

# 设置要加载的 HTML 文档
# 其中包含 LaTeX 数学公式
html = """
<html>
<body>
<img src="https://latex.codecogs.com/svg.latex?\large&space;x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" title="\large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" />
</body>
</html>
"""

# 使用 QWebEngineView 控件的 setHtml() 方法加载 HTML 文档
web_view.setHtml(html)

# 显示 QWebEngineView 控件
web_view.show()

# 运行应用程序
app.exec()