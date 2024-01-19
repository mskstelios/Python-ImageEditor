from PIL import Image, ImageEnhance, ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QListWidget,
    QHBoxLayout, QVBoxLayout, QFileDialog, QCheckBox)
from PyQt5.QtGui import QPixmap
import os



class ImageProcessor:
    def __init__(self):
        self.show_image = None
        self.image = None
        self.directory = None
        self.filename = None
        self.save_image = 'Modified/'

    def load_image(self, directory, filename):
        self.directory = directory
        self.filename = filename
        image_path = os.path.join(directory, filename)
        self.image = Image.open(image_path)

    def get_modified_filename(self, filter_name):
        base_name, extension = os.path.splitext(self.filename)
        return f"{filter_name}.{base_name}{extension}"

    def show_images(self, path):
        show_image.hide()
        pixelimage = QPixmap(path)
        width, height = show_image.width(), show_image.height()
        image = pixelimage.scaled(width, height, Qt.KeepAspectRatio)
        show_image.setPixmap(image)
        show_image.show()
    def saving_image(self, filter_name):
        path = os.path.join(self.directory, self.save_image)
        if not os.path.exists(path):
            os.mkdir(path)
        modified_filename = self.get_modified_filename(filter_name)
        image_path = os.path.join(path, modified_filename)
        self.image.save(image_path)
    def save_button(self):
        path = os.path.join(self.directory, self.save_image)
        if left_button.isChecked():
            self.image = self.image.transpose(Image.ROTATE_90)
            filter_name = 'left'
            modified_filename = self.get_modified_filename(filter_name)
            self.saving_image(filter_name)
            self.show_images(os.path.join(path, modified_filename))
        if bw_button.isChecked():
            self.image = self.image.convert('L')
            filter_name = 'bw'
            modified_filename = self.get_modified_filename(filter_name)
            self.saving_image(filter_name)
            self.show_images(os.path.join(path, modified_filename))
        if mirror_button.isChecked():
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            filter_name = 'mirror'
            modified_filename = self.get_modified_filename(filter_name)
            self.saving_image(filter_name)
            self.show_images(os.path.join(path, modified_filename))
        if sharpness_button.isChecked():
            enhancer = ImageEnhance.Sharpness(self.image)
            enhanced_image = enhancer.enhance(5.0)
            filter_name = 'sharpness'
            modified_filename = self.get_modified_filename(filter_name)
            enhanced_image.save(os.path.join(path, modified_filename))
            self.show_images(os.path.join(path, modified_filename))
        if normal_button.isChecked():
            self.load_image(self.directory, self.filename)
            filter_name = 'normal'
            modified_filename = self.get_modified_filename(filter_name)
            self.saving_image(filter_name)
            self.show_images(os.path.join(path, modified_filename))
        if blur_button.isChecked():
            self.image = self.image.filter(ImageFilter.BoxBlur(10)) # You can change the value here.
            filter_name = 'blur'
            modified_filename = self.get_modified_filename(filter_name)
            self.saving_image(filter_name)
            self.show_images(os.path.join(path, modified_filename))


workimage = ImageProcessor()

# Functions
def filter(files, extensions):
    result = []
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    for i in files:
        result.extend(i for extension in extensions if i.endswith(extension))
    return result

def workdirs():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def show_files():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    workdirs()
    filenames = filter(os.listdir(workdir), extensions)
    box_files.addItems(filenames)
def show_chosen_image():
    filename = box_files.currentItem().text()
    workimage.load_image(workdir, filename)
    image_path = os.path.join(workdir, filename)
    workimage.show_images(image_path)

# Configuration
app = QApplication([])
display = QWidget()
display.setWindowTitle('Image Editor')
display.resize(300, 300)

# Making the editor
open_folders = QPushButton("Open Folder")
box_files = QListWidget()

show_image = QLabel("Image:")

# Buttons
left_button = QCheckBox("Left")
mirror_button = QCheckBox("Mirror")
sharpness_button = QCheckBox("Sharpness")
bw_button = QCheckBox("B&W")
blur_button = QCheckBox("Blur")
normal_button = QCheckBox("Normal")

save_buttons = QPushButton("Save Edited Image")

# Setting Layout
row_v = QVBoxLayout()
row = QHBoxLayout()

row_v.addWidget(open_folders)
row_v.addWidget(box_files)
row.addLayout(row_v)


row2_v = QVBoxLayout()
row2_v.addWidget(show_image)


row2 = QHBoxLayout()
row2.addWidget(left_button)
row2.addWidget(mirror_button)
row2.addWidget(sharpness_button)
row2.addWidget(bw_button)
row2.addWidget(blur_button)
row2.addWidget(normal_button)
row2.addWidget(save_buttons)
row2_v.addLayout(row2)
row.addLayout(row2_v)

display.setLayout(row)

# Connections
open_folders.clicked.connect(show_files)
box_files.currentRowChanged.connect(show_chosen_image)
save_buttons.clicked.connect(workimage.save_button)

# Events
if __name__ == '__main__':
    display.show()
    app.exec_()