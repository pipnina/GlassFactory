from PySide6 import QtCore
from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QListWidget, QListWidgetItem
from Components.component_manager import ComponentManager
from Components.component import ComponentType, Component
from UI_code.CustomQTreeWidgetItem import CustomQTreeWidgetItem
from event_manager import subscribe, raise_event, Event



class EditorPanel(QVBoxLayout):

    parts_manager = [ComponentManager]
    tree_view: [QTreeWidget]
    table_view: [QTableWidget]
    list_view: [QListWidget]
    selected_tree_item: [Component]

    def __init__(self):
        super().__init__()

        # Instantiate and merge the views into the box layout
        self.tree_view = QTreeWidget()
        self.table_view = QTableWidget()
        self.list_view = QListWidget()
        self.list_view.show()

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
        # This subscribes the editor panel to events happening in the component manager
        subscribe(Event.ComponentChanged, self.update_view)
        # These connect QT events to functions in the program. This makes user input work.
        self.tree_view.itemActivated.connect(self.tree_selection_changed)
        self.tree_view.itemChanged.connect(self.tree_data_changed)

    def update_view(self):
        # For now, we're just going to clear and rebuild the tree every time.
        # Who doesn't love a good old "temporary" solution?!
        self.tree_view.clear()

        for item in ComponentManager.get_manager().components:
            new_item = CustomQTreeWidgetItem(item.component_name, item.component_UUID)
            new_item.setText(0, item.component_name)
            new_item.setFlags(new_item.flags() | QtCore.Qt.ItemIsEditable)
            self.tree_view.addTopLevelItem(new_item)

        # self.table_add_lens(ComponentManager.get_manager().components[0])

    # This triggers the table view to be updated whenever a new item is selected in the tree view
    # TODO: Maybe implement something to protect it, as currently called when tree empty at program start
    def tree_selection_changed(self, item: QTreeWidgetItem, column: int):
        for component in ComponentManager.get_manager().components:
            if item.text(0) == component.component_name:
                if component.component_type == ComponentType.Lens:
                    self.table_add_lens(component)
                    self.selected_tree_item = component
        print("Tree Selection changed")
        pass

    def tree_data_changed(self):
            for component in ComponentManager.get_manager().components:
                if self.tree_view.currentItem().text() == component.component_name:
                    print("Two components have the same name! Abort!")
                    self.update_view()



    # We need some functions for allowing us to present the component's properties in the table
    def table_add_lens(self, lens):
        q_list_widget_items: list[QListWidgetItem] = lens.get_ui()

        if len(q_list_widget_items) >= 1:
            for widget in q_list_widget_items:
                self.list_view.addItem(widget)
        else:
            print("Something's wrong, a component is missing a config UI!")


        self.table_view.clear()
        self.table_view.setRowCount(14)
        self.table_view.setItem(0,0, QTableWidgetItem("Name"))
        self.table_view.item(0, 0).setFlags(QtCore.Qt.ItemIsEditable)
        self.table_view.setItem(0,1, QTableWidgetItem(lens.component_name))
        self.table_view.setItem(1,0, QTableWidgetItem("X"))
        self.table_view.item(1, 0).setFlags(QtCore.Qt.ItemIsEditable)
        self.table_view.setItem(1,1, QTableWidgetItem(str(lens.x)))
        self.table_view.setItem(2,0, QTableWidgetItem("Y"))
        self.table_view.item(2, 0).setFlags(QtCore.Qt.ItemIsEditable)
        self.table_view.setItem(2,1, QTableWidgetItem(str(lens.y)))
        self.table_view.setItem(3,0, QTableWidgetItem("Rotation"))
        self.table_view.item(3, 0).setFlags(QtCore.Qt.ItemIsEditable)
        self.table_view.setItem(3,1, QTableWidgetItem(str(lens.xr)))
        self.table_view.setItem(4,0, QTableWidgetItem("Diameter"))
        self.table_view.item(4, 0).setFlags(QtCore.Qt.ItemIsEditable)
        self.table_view.setItem(4,1, QTableWidgetItem(str(lens.diameter)))
        self.table_view.setItem(5,0, QTableWidgetItem("Thickness"))
        self.table_view.item(5, 0).setFlags(QtCore.Qt.ItemIsEditable)
        self.table_view.setItem(5,1, QTableWidgetItem(str(lens.thickness)))
        self.table_view.setItem(6,0, QTableWidgetItem("Surface 1 FL"))
        self.table_view.item(6, 0).setFlags(QtCore.Qt.ItemIsEditable)
        self.table_view.setItem(6,1, QTableWidgetItem(str(lens.surfaces[0].focal_length)))
        self.table_view.setItem(7,0, QTableWidgetItem("Surface 1 K"))
        self.table_view.item(7, 0).setFlags(QtCore.Qt.ItemIsEditable)
        self.table_view.setItem(7,1, QTableWidgetItem(str(lens.surfaces[0].conic_constant)))
        self.table_view.setItem(8,0, QTableWidgetItem("Surface 1 Flat"))
        self.table_view.item(8, 0).setFlags(QtCore.Qt.ItemIsEditable)
        self.table_view.setItem(8,1, QTableWidgetItem(str(lens.surfaces[0].is_flat)))
        self.table_view.setItem(9,0, QTableWidgetItem("Surface 1 Reflective"))
        self.table_view.item(9, 0).setFlags(QtCore.Qt.ItemIsEditable)
        self.table_view.setItem(9,1, QTableWidgetItem(str(lens.surfaces[0].is_reflective)))
        self.table_view.setItem(10,0, QTableWidgetItem("Surface 2 FL"))
        self.table_view.item(10, 0).setFlags(QtCore.Qt.ItemIsEditable)
        self.table_view.setItem(10,1, QTableWidgetItem(str(lens.surfaces[1].focal_length)))
        self.table_view.setItem(11,0, QTableWidgetItem("Surface 2 K"))
        self.table_view.item(11, 0).setFlags(QtCore.Qt.ItemIsEditable)
        self.table_view.setItem(11,1, QTableWidgetItem(str(lens.surfaces[1].conic_constant)))
        self.table_view.setItem(12,0, QTableWidgetItem("Surface 2 Flat"))
        self.table_view.item(12, 0).setFlags(QtCore.Qt.ItemIsEditable)
        self.table_view.setItem(12,1, QTableWidgetItem(str(lens.surfaces[1].is_flat)))
        self.table_view.setItem(13,0, QTableWidgetItem("Surface 2 Reflective"))
        self.table_view.item(13, 0).setFlags(QtCore.Qt.ItemIsEditable)
        self.table_view.setItem(13,1, QTableWidgetItem(str(lens.surfaces[1].is_reflective)))

