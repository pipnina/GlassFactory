from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView
from PySide6.QtCore import QAbstractTableModel
from Components.componentManager import ComponentManager
from eventManager import signal_subscribe, signal_send


class EditorPanel(QVBoxLayout):

    parts_manager = [ComponentManager]
    tree_view: [QTreeWidget]
    table_view: [QTableWidget]

    def __init__(self, parts_manager: ComponentManager):
        super().__init__()

        # We set the parts_manager as this view represents the data from that source
        self.parts_manager = parts_manager

        # Instantiate and merge the views into the box layout
        self.tree_view = QTreeWidget()
        self.table_view = QTableWidget()

        self.addWidget(self.tree_view)
        self.addWidget(self.table_view)

        # Set up the tree
        self.tree_view.setHeaderHidden(True)

        # Set up the table
        # First we set the columns, as these are consistant between all objects
        self.table_view.setColumnCount(2)
        self.table_view.setHorizontalHeaderItem(0, QTableWidgetItem("Property"))
        self.table_view.setHorizontalHeaderItem(1, QTableWidgetItem("Value"))

        # Then for the rows, a more complex handling is required depending on what is selected in tree widget

        signal_subscribe("components_changed", self.update_view)

    def update_view(self, data_table):
        # For now we're just going to clear and rebuild the tree every time.
        # Who doesn't love a good old "temporary" solution?!
        self.tree_view.clear()

        for item in data_table:
            new_item = QTreeWidgetItem(item.properties['part_name'])
            new_item.setText(len(item.properties['part_name']), item.properties['part_name'])
            self.tree_view.addTopLevelItem(new_item)

        print("Yo yo mr white")
