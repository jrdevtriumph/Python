# This code will run in terminal 
# from pytube import YouTube

# def Download(link):
#     youtubeObject = YouTube(link)
#     youtubeObject = youtubeObject.streams.get_highest_resolution()
#     try:
#         youtubeObject.download()
#     except:
#         print("An error has occurred")
#     print("Download is completed successfully")


# link = input("Enter the YouTube video URL: ")
# Download(link)

# This code will run by double click the file as any .exe file (tkinter)
# from tkinter import *
# from pytube import YouTube

# def download_video():
#     link = link_entry.get()
#     try:
#         youtube_object = YouTube(link)
#         youtube_object = youtube_object.streams.get_highest_resolution()
#         youtube_object.download()
#         status_label.config(text="Download completed successfully")
#     except Exception as e:
#         status_label.config(text=f"Error: {str(e)}")

# # Create a Tkinter window
# window = Tk()
# window.title("YouTube Video Downloader")

# # Create labels, entry, and button widgets
# label = Label(window, text="Enter the YouTube video URL:")
# label.pack()

# link_entry = Entry(window, width=50)
# link_entry.pack()

# download_button = Button(window, text="Download", command=download_video)
# download_button.pack()

# status_label = Label(window, text="")
# status_label.pack()

# # Run the Tkinter event loop
# window.mainloop()



# This code will run by double click the file as any .exe file (pyqt)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from pytube import YouTube

class YouTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Video Downloader")
        self.setStyleSheet("background-color: #f0f0f0;")

        self.label = QLabel("Enter the YouTube video URL:")
        self.label.setStyleSheet("font-size: 16px; color: #333;")

        self.link_entry = QLineEdit()
        self.link_entry.setStyleSheet("font-size: 14px; padding: 8px; border: 1px solid #ccc; border-radius: 4px;")
        self.link_entry.setFixedWidth(400)  # Set the width of the input box to 400 pixels

        self.download_button = QPushButton("Download")
        self.download_button.setStyleSheet("font-size: 16px; padding: 10px; background-color: #007bff; color: #fff; border: none; border-radius: 4px;")
        
        self.status_label = QLabel("")
        self.status_label.setStyleSheet("font-size: 14px; color: #333;")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.link_entry)
        layout.addWidget(self.download_button)
        layout.addWidget(self.status_label)
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(20, 20, 20, 20)

        self.download_button.clicked.connect(self.download_video)

        self.setLayout(layout)

    def download_video(self):
        link = self.link_entry.text()
        try:
            youtube_object = YouTube(link)
            youtube_object = youtube_object.streams.get_highest_resolution()
            youtube_object.download()
            self.status_label.setText("Download completed successfully")
        except Exception as e:
            self.status_label.setText(f"Error: {str(e)}")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = YouTubeDownloader()
    window.show()
    sys.exit(app.exec_())

