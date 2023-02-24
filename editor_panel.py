from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView
from PySide6.QtCore import QAbstractTableModel
from Components.component_manager import ComponentManager
from event_manager import subscribe, raise_event, Event


class EditorPanel(QVBoxLayout):

    parts_manager = [ComponentManager]
    tree_view: [QTreeWidget]
    table_view: [QTableWidget]

    def __init__(self):
        super().__init__()

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

        subscribe(Event.ComponentChanged, self.update_view)

    def update_view(self):
        # For now, we're just going to clear and rebuild the tree every time.
        # Who doesn't love a good old "temporary" solution?!
        self.tree_view.clear()

        for item in ComponentManager.get_manager().components:
            new_item = QTreeWidgetItem(item.component_name)
            new_item.setText(0, item.component_name)
            self.tree_view.addTopLevelItem(new_item)

        print("Yo yo mr white")
