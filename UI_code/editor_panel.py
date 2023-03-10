from PySide6 import QtCore
from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QTreeWidget, QSplitter, QScrollArea, QVBoxLayout, QWidget, QMenu
from Components.component_manager import ComponentManager
from Components.component import ComponentType, Component
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
        self.tree_view.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)

        # Then for the rows, a more complex handling is required depending on what is selected in tree widget
        # This subscribes the editor panel to events happening in the component manager
        subscribe(Event.ComponentChanged, self._update_view)
        # These connect QT events to functions in the program. This makes user input work.
        self.tree_view.currentItemChanged.connect(self._on_tree_selection_changed)
        self.tree_view.itemChanged.connect(self._tree_data_changed)
        self.tree_view.customContextMenuRequested.connect(self._tree_context_menu_requested)

    # Whenever data changes, this function causes the whole editor panel UI to be rebuilt
    def _update_view(self):
        # This builds the data in the tree view
        self.tree_view.clear()

        children: list = []

        for item in ComponentManager.get_manager().components:
            new_item = CustomQTreeWidgetItem(item)
            new_item.setFlags(new_item.flags() | QtCore.Qt.ItemIsEditable)
            new_item.setExpanded(True)

            if item.parent is None:
                self.tree_view.addTopLevelItem(new_item)
            else:
                children.append(item)

        if len(children) > 0:
            self._add_children(children)

    # Recursively add child component to the tree widget
    def _add_children(self, children: list [Component]):
        next_layer_children: list[Component] = []
        for item in children:
            if item.parent.parent is None:
                # This is a child that definitely has a parent already in the tree
                new_widget = CustomQTreeWidgetItem(item)
                new_widget.setFlags(new_widget.flags() | QtCore.Qt.ItemIsEditable)
                new_widget.setExpanded(True)
                for widget in range(0, self.tree_view.topLevelItemCount()):
                    if self.tree_view.topLevelItem(widget).component.component_UUID == item.parent.component_UUID:
                        self.tree_view.topLevelItem(widget).addChild(new_widget)
            else:
                # This is a child that does NOT have a parent with a parent, we must pass these
                # on to the next recursion of the _add_children function.
                pass


    # This triggers the table view to be generated whenever a new item is selected in the tree view
    def _on_tree_selection_changed(self, item: CustomQTreeWidgetItem, old_item: CustomQTreeWidgetItem):
        fresh_layout = QVBoxLayout()
        config_container = QWidget()

        if item is None and old_item is None:
            print("No CutsomQTreeWidgeItem passed, blanking!")
            return

        if item is None and old_item is not None:
            old_item.setSelected(True)
            return

        q_list_widget_items: list[QWidget] = item.component.get_ui()

        if len(q_list_widget_items) < 1:
            print("Something's wrong, a component is missing a config UI!")
            return

        for widget in q_list_widget_items:
            fresh_layout.addLayout(widget)

        config_container.setLayout(fresh_layout)
        self.area.setFixedWidth(q_list_widget_items[0].sizeHint().width()+40)
        self.area.setWidget(config_container)

    def _tree_data_changed(self, item: CustomQTreeWidgetItem, _column: int):
        item.component.component_name = item.text(0)
        self._on_tree_selection_changed(item)
        raise_event(Event.ComponentChanged)

    def _tree_context_menu_requested(self, menu_position: QPoint):
        menu = QMenu()
        menu_add_group = menu.addAction("Add Group")
        menu_add_group.triggered.connect(lambda: self._tree_context_menu_add_component(ComponentType.Group))
        menu_add_lens = menu.addAction("Add Lens")
        menu_add_lens.triggered.connect(lambda: self._tree_context_menu_add_component(ComponentType.Lens))
        menu_spacer = menu.addSeparator()
        menu_cut = menu.addAction("Cut")
        menu_copy = menu.addAction("Copy")
        menu_paste = menu.addAction("Paste")


        menu.exec(QPoint(menu_position.x()+menu.sizeHint().width(), menu_position.y()+menu.sizeHint().height()))

    def _tree_context_menu_add_component(self, component_type):
        if self.tree_view.currentItem() is not None:
            ComponentManager.get_manager().new_component(component_type, parent=self.tree_view.currentItem().component)
            return

        if self.tree_view.currentItem() is None:
            ComponentManager.get_manager().new_component(component_type)
            return
