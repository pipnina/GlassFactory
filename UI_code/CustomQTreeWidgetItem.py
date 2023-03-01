from PySide6.QtWidgets import QTreeWidgetItem


# This class exists purely to allow me to hard link tree widget items to the component they represent
class CustomQTreeWidgetItem(QTreeWidgetItem):
    def __init__(self):
        super().__init__()
        self.component_UUID = None
