from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView
from PySide6.QtCore import QAbstractTableModel

class EditorPanel(QVBoxLayout):
    def __init__(self):
        super().__init__()
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
