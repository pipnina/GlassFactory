from dataclasses import dataclass
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QCheckBox
from PySide6.QtCore import Qt
from event_manager import raise_event, Event


@dataclass
class SurfaceProperties:
    focal_length: float = 100
    conic_constant: float = 0
    is_flat: bool = False
    is_reflective: bool = False

    def get_ui(self, index: int):
        vertical_layout = QVBoxLayout()
        top_label = QLabel(f"Surface {index}")
        top_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vertical_layout.addWidget(top_label)

        # Widget for editing the focal length
        focal_length_container = QHBoxLayout()
        focal_length_label = QLabel("Focal Length:")
        focal_length_label.setMinimumSize(130, 10)
        focal_length_edit = QLineEdit()
        focal_length_edit.setText(str(self.focal_length))
        focal_length_edit.editingFinished.connect(lambda: self._on_fl_value_changed(focal_length_edit))
        focal_length_container.addWidget(focal_length_label)
        focal_length_container.addWidget(focal_length_edit)
        vertical_layout.addLayout(focal_length_container)

        # Widget for editing the conic constant
        constant_container = QHBoxLayout()
        constant_label = QLabel("Conic Constant:")
        constant_label.setMinimumSize(130, 10)
        constant_edit = QLineEdit()
        constant_edit.setText(str(self.conic_constant))
        constant_edit.editingFinished.connect(lambda: self._on_conic_value_changed(constant_edit))
        constant_container.addWidget(constant_label)
        constant_container.addWidget(constant_edit)
        vertical_layout.addLayout(constant_container)

        # Widget for toggling if the surface is flat
        flat_container = QHBoxLayout()
        flat_label = QLabel("Flat Surface?")
        flat_label.setMinimumSize(130, 10)
        flat_edit = QCheckBox()
        flat_edit.setChecked(self.is_flat)
        flat_edit.stateChanged.connect(lambda: self._on_flat_value_changed(flat_edit))
        flat_container.addWidget(flat_label)
        flat_container.addWidget(flat_edit)
        vertical_layout.addLayout(flat_container)

        # Widget for toggling if the surface is a mirror
        reflective_container = QHBoxLayout()
        reflective_label = QLabel("Mirror Surface?")
        reflective_label.setMinimumSize(130, 10)
        reflective_edit = QCheckBox()
        reflective_edit.setChecked(self.is_reflective)
        reflective_edit.stateChanged.connect(lambda: self._on_reflective_value_changed(reflective_edit))
        reflective_container.addWidget(reflective_label)
        reflective_container.addWidget(reflective_edit)
        vertical_layout.addLayout(reflective_container)

        return vertical_layout

    def _on_fl_value_changed(self, widgetbox):
        try:
            self.focal_length = float(widgetbox.displayText())
            raise_event(Event.ComponentChanged)
        except ValueError:
            print("You need to enter a number!")
            widgetbox.setText(str(self.focal_length))

    def _on_conic_value_changed(self, widgetbox):
        try:
            self.conic_constant = float(widgetbox.displayText())
            raise_event(Event.ComponentChanged)
        except ValueError:
            print("You need to enter a number!")
            widgetbox.setText(str(self.conic_constant))

    def _on_flat_value_changed(self, widgetbox: QCheckBox):
        try:
            self.is_flat = widgetbox.isChecked()
            raise_event(Event.ComponentChanged)
        except ValueError:
            print("You need to enter a number!")
            widgetbox.setCheckState(self.is_flat)

    def _on_reflective_value_changed(self, widgetbox: QCheckBox):
        try:
            self.is_reflective = widgetbox.isChecked()
            raise_event(Event.ComponentChanged)
        except ValueError:
            print("You need to enter a number!")
            widgetbox.setCheckState(self.is_reflective)
