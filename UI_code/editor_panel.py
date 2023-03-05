from PySide6 import QtCore
from PySide6.QtWidgets import QTreeWidget, QSplitter, QListWidget, QListWidgetItem, QWidget
from Components.component_manager import ComponentManager
from UI_code.CustomQTreeWidgetItem import CustomQTreeWidgetItem
from event_manager import subscribe, raise_event, Event



class EditorPanel(QVBoxLayout):

    parts_manager = [ComponentManager]
    tree_view: [QTreeWidget]
    list_view: [QListWidget]

    def __init__(self):
        super().__init__()

        # Instantiate and merge the views into the box layout
        self.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.tree_view = QTreeWidget()
        self.list_view = QListWidget()

        self.addWidget(self.tree_view)
        self.addWidget(self.list_view)

        # Set up the tree
        self.tree_view.setHeaderHidden(True)

        # Then for the rows, a more complex handling is required depending on what is selected in tree widget
        # This subscribes the editor panel to events happening in the component manager
        subscribe(Event.ComponentChanged, self._update_view)
        # These connect QT events to functions in the program. This makes user input work.
        self.tree_view.itemActivated.connect(self._on_tree_selection_changed)
        self.tree_view.itemChanged.connect(self._tree_data_changed)

    # Whenever data changes, this function causes the whole editor panel UI to be rebuilt
    def _update_view(self):
        selected_tree_view_item = self.tree_view.selectedItems()
        self.tree_view.clear()
        # self.list_view.clear() IF YOU CALL THIS HERE, IT BREAKS THINGS, I KNOW NOT WHY

        for item in ComponentManager.get_manager().components:
            new_item = CustomQTreeWidgetItem(item)
            new_item.setFlags(new_item.flags() | QtCore.Qt.ItemIsEditable)
            self.tree_view.addTopLevelItem(new_item)


        if len(selected_tree_view_item) != 0:
            self._on_tree_selection_changed(selected_tree_view_item[0])

    # This triggers the table view to be generated whenever a new item is selected in the tree view
    def _on_tree_selection_changed(self, item: CustomQTreeWidgetItem):
        print("Tree Selection changed")
        self.list_view.clear()
        q_list_widget_items: list[QWidget] = item.component.get_ui()

        if len(q_list_widget_items) < 1:
            print("Something's wrong, a component is missing a config UI!")
            return

        for widget in q_list_widget_items:
            new_list_item = QListWidgetItem()
            new_list_item.setSizeHint(widget.sizeHint())
            self.list_view.addItem(new_list_item)
            self.list_view.setItemWidget(new_list_item, widget)

    def _tree_data_changed(self, item: CustomQTreeWidgetItem, _column: int):
        print("Component changed!!")
        item.component.component_name = item.text(0)
        raise_event(Event.ComponentChanged)



