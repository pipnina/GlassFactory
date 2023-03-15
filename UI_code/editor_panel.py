from PySide6 import QtCore
from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QTreeWidget, QSplitter, QScrollArea, QVBoxLayout, QWidget, QMenu
from Components.component_manager import ComponentManager
from Components.component import ComponentType, Component
from Components.group import Group
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
        # create a tree widget item for every TOP LEVEL item in the components list
        for item in ComponentManager.get_manager().components:
            if item.parent is None:
                new_item = CustomQTreeWidgetItem(item)
                new_item.setFlags(new_item.flags() | QtCore.Qt.ItemIsEditable)
                new_item.setExpanded(True)
                self.tree_view.addTopLevelItem(new_item)
        # Iterate through the top level items, to recursively add their children to the tree.
        for widget_index in range(0, self.tree_view.topLevelItemCount()):
            widget = self.tree_view.topLevelItem(widget_index)
            if type(widget.component) == Group and len(widget.component.children) > 0:
                self._add_children_to_tree(self.tree_view.topLevelItem(widget_index))

        self.tree_view.expandAll()

    # For each top level component:
    # Build the top level tree widget item
    # Call _add_children on all of that component's children
    # recursively call _add_children to the children of those children
    # needs to be passed the component and the tree widget item as reference each time.

    # Recursively add child component to the tree widget
    def _add_children_to_tree(self, widget: CustomQTreeWidgetItem):
            for component in widget.component.children:
                new_widget = CustomQTreeWidgetItem(component)
                new_widget.setFlags(new_widget.flags() | QtCore.Qt.ItemIsEditable)
                new_widget.setExpanded(True)
                widget.addChild(new_widget)
                if type(component) == Group and len(component.children) > 0:
                    self._add_children_to_tree(new_widget)




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
        widget: CustomQTreeWidgetItem = self.tree_view.itemAt(menu_position)

        menu = QMenu()
        menu_add_group = menu.addAction("Add Group")
        menu_add_group.triggered.connect(lambda: self._tree_context_menu_add_component(ComponentType.Group, widget))
        menu_add_lens = menu.addAction("Add Lens")
        menu_add_lens.triggered.connect(lambda: self._tree_context_menu_add_component(ComponentType.Lens, widget))
        menu_spacer = menu.addSeparator()
        menu_cut = menu.addAction("Cut")
        menu_cut.triggered.connect(lambda: self._tree_context_menu_cut(widget))
        menu_copy = menu.addAction("Copy")
        menu_copy.triggered.connect(lambda: self._tree_context_menu_copy(widget))
        menu_paste = menu.addAction("Paste")
        menu_paste.triggered.connect(lambda: self._tree_context_menu_paste(widget))

        menu.exec(self.tree_view.mapToGlobal(menu_position))

    def _tree_context_menu_add_component(self, component_type, tree_widget: CustomQTreeWidgetItem):
        if tree_widget is not None:
            ComponentManager.get_manager().new_component(component_type, parent=tree_widget.component)
            return

        if tree_widget is None:
            ComponentManager.get_manager().new_component(component_type)
            return

    def _tree_context_menu_cut(self, widget: CustomQTreeWidgetItem):
        if widget is None:
            return
        ComponentManager.get_manager().cut_component(widget.component)

    def _tree_context_menu_copy(self, widget: CustomQTreeWidgetItem):
        if widget is None:
            return
        ComponentManager.get_manager().copy_component(widget.component)
        pass

    def _tree_context_menu_paste(self, widget: CustomQTreeWidgetItem):
        if widget is None:
            ComponentManager.get_manager().paste_component(None)
            return
        ComponentManager.get_manager().paste_component(widget.component)
        pass
