from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QTextEdit
from summarize import summarize

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout and widget
        self.setWindowTitle("Summarize Youtube Video")
        self.resize(700,500)

        layout = QVBoxLayout(self)

        # Create a QTextEdit widget
        self.utube_link_input = QLineEdit(self)
        utube_link_label = QLabel("Paste Youtube URL:")
        summary_label = QLabel("Summary:")
        self.summary_text = QTextEdit(self)
        self.summary_text.setReadOnly(True)
        summary_btn = QPushButton("Summarize")
        

        layout.addWidget(utube_link_label)
        layout.addWidget(self.utube_link_input)
        layout.addWidget(summary_label)
        layout.addWidget(summary_btn)
        layout.addWidget(self.summary_text)

        summary_btn.clicked.connect(self.summarize_video)
    def summarize_video(self):
            # Get the YouTube URL from the input field
            youtube_url = self.utube_link_input.text()

            if youtube_url:
                try:
                    # Call the summarize function and get the summary
                    summary = summarize(youtube_url)
                    self.summary_text.setText(summary)  # Display the summary in the label
                except Exception as e:
                    self.summary_text.setText(f"Error occurred: {e}")  # Display error if any
            else:
                self.summary_text.setText("Please enter a valid YouTube URL.")  # If URL is empty


    

if __name__ == "__main__":
    app = QApplication([])
    main_window = MyWindow()
    main_window.show()
    app.exec_()
    
