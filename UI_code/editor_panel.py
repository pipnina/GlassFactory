from PySide6 import QtCore
from PySide6.QtWidgets import QTreeWidget, QSplitter, QListWidget, QListWidgetItem, QWidget, QScrollArea, QVBoxLayout, QLabel, QHBoxLayout, QWidget, QLineEdit
from Components.component_manager import ComponentManager
from UI_code.CustomQTreeWidgetItem import CustomQTreeWidgetItem
from event_manager import subscribe, raise_event, Event


class EditorPanel(QSplitter):

    parts_manager = [ComponentManager]
    tree_view: [QTreeWidget]

    def __init__(self):
        super().__init__()

        # Instantiate and merge the views into the box layout
        self.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.tree_view = QTreeWidget()
        self.tree_view.setMaximumWidth(325)
        # The scroll area for the component configuration needs a special setup
        # The area can only display one QWidget, so we must create a blank one, with a vertical layout set
        # The configuration widgets are then added to the vertical layout, creating a scrollable list!
        """
        ScrollArea
        Widget
        VBoxLayout
        Widget set layout (VBoxLayout)
        ScrollArea set widget (Widget) <- Do this AFTER making the configuration widgets and adding them to VBoxLayout!)        
        """
        self.area = QScrollArea()

        self.addWidget(self.tree_view)
        self.addWidget(self.area)

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

        for item in ComponentManager.get_manager().components:
            new_item = CustomQTreeWidgetItem(item)
            new_item.setFlags(new_item.flags() | QtCore.Qt.ItemIsEditable)
            self.tree_view.addTopLevelItem(new_item)

        if len(selected_tree_view_item) != 0:
            self._on_tree_selection_changed(selected_tree_view_item[0])

    # This triggers the table view to be generated whenever a new item is selected in the tree view
    def _on_tree_selection_changed(self, item: CustomQTreeWidgetItem):
        print("Tree Selection changed")
        fresh_layout = QVBoxLayout()
        config_container = QWidget()

        q_list_widget_items: list[QWidget] = item.component.get_ui()

        if len(q_list_widget_items) < 1:
            print("Something's wrong, a component is missing a config UI!")
            return

        for widget in q_list_widget_items:
            fresh_layout.addLayout(widget)

        config_container.setLayout(fresh_layout)
        self.area.setWidget(config_container)

    def _tree_data_changed(self, item: CustomQTreeWidgetItem, _column: int):
        print("Component changed!!")
        item.component.component_name = item.text(0)
        raise_event(Event.ComponentChanged)



