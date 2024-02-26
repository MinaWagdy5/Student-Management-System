import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSV Export Example")

        self.export_button = QPushButton("Export CSV", self)
        self.export_button.clicked.connect(self.export_button_clicked)
        self.export_button.setGeometry(50, 50, 200, 50)

    def export_button_clicked(self):
        target_filename = "students.csv"  # Assuming data is stored in "data.csv"
        exported_filename = self.export_csv(self, target_filename)
        if exported_filename:
            print(f"CSV file exported successfully as {exported_filename}")
        else:
            print("Export cancelled or error occurred")

    def export_csv(self, parent, target_filename):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            chosen_filename, _ = QFileDialog.getSaveFileName(parent, "Save CSV File", "", "CSV Files (*.csv)", options=options)
            
            if chosen_filename:
                with open(chosen_filename, 'w', newline='') as new_csv_file:
                    # Open the target file
                    with open(target_filename, 'r', newline='') as target_file:
                        reader = csv.reader(target_file)
                        writer = csv.writer(new_csv_file)
                        for row in reader:
                            writer.writerow(row)
                return chosen_filename
            
            return None
            
        except Exception as e:
            print("Error:", e)
            return None

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 300, 200)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
