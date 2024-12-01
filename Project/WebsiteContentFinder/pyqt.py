import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QHBoxLayout,
    QScrollArea,
    QLabel,
)
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QGuiApplication, QIcon, QPixmap


class WebpageTextExtractor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Webpage Text Extractor")
        self.setGeometry(100, 100, 800, 600)  # Set initial window size
        self.setup_ui()

    def setup_ui(self):
        # Create widgets
        self.url_label = QLabel("Enter URL:")
        self.url_entry = QLineEdit()
        self.url_entry.setPlaceholderText("Enter URL")
        self.url_entry.setStyleSheet("border-radius: 10px; padding: 10px 20px;")
        self.extract_button = QPushButton("Extract Text")
        self.extract_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 10px; padding: 10px 20px;")
        self.extract_button.setCursor(Qt.PointingHandCursor)

        # Create scroll area to contain the text widgets
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Create widget to contain text widgets
        self.text_widgets_container = QWidget()
        self.text_widgets_layout = QVBoxLayout(self.text_widgets_container)

        # Create layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.url_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.url_entry)
        layout.addWidget(self.extract_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.scroll_area)

        # Set text widgets container as scroll area widget
        self.scroll_area.setWidget(self.text_widgets_container)

        # Connect button click event
        self.extract_button.clicked.connect(self.extract_text)

    def extract_text(self):
        url = self.url_entry.text()
        try:
            # Send a GET request to the URL
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the HTML content using Beautiful Soup
                soup = BeautifulSoup(response.text, "html.parser")

                # Extract all text from the parsed HTML
                text = soup.get_text()

                # Display the extracted text in QTextEdits with copy buttons
                self.display_text_in_widgets(text)

            else:
                self.display_error(f"Error: {response.status_code} - {response.reason}")

        except Exception as e:
            self.display_error(f"Error: {e}")

    def display_text_in_widgets(self, text):
        # Clear existing text widgets
        self.clear_text_widgets()

        # Split the text into paragraphs
        paragraphs = [paragraph.strip() for paragraph in text.split("\n") if paragraph.strip()]

        # Create a QTextEdit and copy button for each paragraph
        for paragraph in paragraphs:
            text_edit = QTextEdit(paragraph)
            text_edit.setReadOnly(True)
            text_edit.setStyleSheet(
                "background-color: #f2f2f2; border: 1px solid #d9d9d9; padding: 5px; margin-bottom: 5px;"
            )

            copy_button = QPushButton("Copy")
            copy_button.setCursor(Qt.PointingHandCursor)
            copy_button.setStyleSheet("background-color: #007BFF; color: white; border-radius: 5px; padding: 7px 10px;")
            copy_button.clicked.connect(lambda _, t=paragraph: self.copy_text(t))

            # Create a layout to hold the text edit and copy button
            layout = QHBoxLayout()
            layout.addWidget(text_edit)
            layout.addWidget(copy_button)

            # Add the layout to the main layout
            self.text_widgets_layout.addLayout(layout)

    def clear_text_widgets(self):
        # Remove all existing text widgets
        for i in reversed(range(self.text_widgets_layout.count())):
            layout_item = self.text_widgets_layout.itemAt(i)
            for j in reversed(range(layout_item.count())):
                widget = layout_item.itemAt(j).widget()
                if widget:
                    widget.deleteLater()
            layout_item.deleteLater()

    def copy_text(self, text):
        # Create a MIME data object and set its text to the clicked text
        mime_data = QMimeData()
        mime_data.setText(text)

        # Copy the clicked text to the clipboard
        clipboard = QGuiApplication.clipboard()
        clipboard.setMimeData(mime_data)

    def display_error(self, error_message):
        # Display error message in a QTextEdit
        error_widget = QTextEdit(error_message)
        error_widget.setReadOnly(True)
        error_widget.setStyleSheet(
            "color: red; background-color: #f2f2f2; border: 1px solid #d9d9d9; padding: 5px; margin-bottom: 5px;"
        )
        self.text_widgets_layout.addWidget(error_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.png"))
    window = WebpageTextExtractor()
    window.show()
    sys.exit(app.exec_())
