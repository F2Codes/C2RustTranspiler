# main.py
import sys, json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QComboBox
from PyQt6.QtGui import QFontDatabase, QFont
from transpiler import transpile_c_to_rust

class C2RustApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("C → Rust ⚡")
        self.setGeometry(100, 100, 900, 600)

        # فونت Vazirmatn-Medium
        QFontDatabase.addApplicationFont("resources/fonts/Vazirmatn-Medium.ttf")
        self.font = QFont("Vazirmatn-Medium", 12)

        # Layout اصلی
        self.layout = QVBoxLayout()

        # انتخاب زبان با پرچم
        self.lang_select = QComboBox()
        self.lang_select.addItems(["🇬🇧 EN", "🇮🇷 FA", "🇷🇺 RU"])
        self.lang_select.currentIndexChanged.connect(self.load_language)
        self.layout.addWidget(self.lang_select)

        # ویرایشگر کد C
        self.c_input = QTextEdit()
        self.c_input.setFont(self.font)
        self.layout.addWidget(self.c_input)

        # خروجی Rust
        self.rust_output = QTextEdit()
        self.rust_output.setFont(self.font)
        self.rust_output.setReadOnly(True)
        self.layout.addWidget(self.rust_output)

        # دکمه ترنسپایل
        self.transpile_btn = QPushButton()
        self.transpile_btn.setFont(self.font)
        self.transpile_btn.clicked.connect(self.run_transpile)
        self.layout.addWidget(self.transpile_btn)

        self.setLayout(self.layout)
        self.load_language(0)  # پیشفرض انگلیسی

    def load_language(self, index):
        lang_map = {0: "en.json", 1: "fa.json", 2: "ru.json"}
        with open(f"locales/{lang_map[index]}", "r", encoding="utf-8") as f:
            self.translations = json.load(f)
        self.c_input.setPlaceholderText(self.translations["placeholder"])
        self.transpile_btn.setText(self.translations["transpile"])

    def run_transpile(self):
        c_code = self.c_input.toPlainText()
        rust_code = transpile_c_to_rust(c_code)
        self.rust_output.setPlainText(rust_code)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = C2RustApp()
    window.show()
    sys.exit(app.exec())
