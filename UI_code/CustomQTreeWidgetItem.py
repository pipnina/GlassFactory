from PySide6.QtWidgets import QTreeWidgetItem


# This class exists purely to allow me to hard link tree widget items to the component they represent
class CustomQTreeWidgetItem(QTreeWidgetItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.component_UUID = None
