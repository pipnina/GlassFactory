from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView
from PySide6.QtCore import QAbstractTableModel

class EditorPanel(QVBoxLayout):
    def __init__(self):
        super().__init__()
        # Create the views and merge them into the box layout
        treeView = QTreeWidget()
        tableView = QTableWidget()

        self.addWidget(treeView)
        self.addWidget(tableView)

        # Set up the tree
        treeView.setHeaderHidden(True)

        # Set up the table
        # First we set the columns, as these are consistant between all objects
        tableView.setColumnCount(2)
        tableView.setHorizontalHeaderItem(0, QTableWidgetItem("Property"))
        tableView.setHorizontalHeaderItem(1, QTableWidgetItem("Value"))

        # Then for the rows, a more complex handling is required depending on what is selected in tree widget
