from PySide6.QtWidgets import QTreeWidgetItem
from Components.component import Component


# This class exists purely to allow me to hard link tree widget items to the component they represent
class CustomQTreeWidgetItem(QTreeWidgetItem):
    def __init__(self, component: Component, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.component = component
        self.setText(0, component.component_name)
