from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView
from PySide6.QtCore import QAbstractTableModel
from Components.componentManager import ComponentManager

class EditorPanel(QVBoxLayout):

    parts_manager = [ComponentManager]

    def __init__(self, parts_manager: ComponentManager):
        super().__init__()

        # We set the parts_manager as this view represents the data from that source
        self.parts_manager = parts_manager

        # Create the views and merge them into the box layout
        tree_view = QTreeWidget()
        table_view = QTableWidget()

        self.addWidget(tree_view)
        self.addWidget(table_view)

        # Set up the tree
        tree_view.setHeaderHidden(True)

        # Set up the table
        # First we set the columns, as these are consistant between all objects
        table_view.setColumnCount(2)
        table_view.setHorizontalHeaderItem(0, QTableWidgetItem("Property"))
        table_view.setHorizontalHeaderItem(1, QTableWidgetItem("Value"))

        # Then for the rows, a more complex handling is required depending on what is selected in tree widget

    # grabTree fetches and updates the information stored by the
    def grabTree(self):
        pass

