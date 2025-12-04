"""View model implementation for file download example."""

import os
import zipfile
from io import BytesIO
from typing import Any, Dict, Optional

from nova.mvvm.interface import BindingInterface

from .model import Model


class ViewModel:
    """View model implementation for file download example."""

    def __init__(self, model: Model, binding: BindingInterface) -> None:
        self.model = model

        # self.on_update is called any time the view updates the binding.
        self.form_data_bind = binding.new_bind(self.model.form, callback_after_update=self.on_update)

    def on_update(self, results: Dict[str, Any]) -> None:
        # This fires when the data selector is updated. You could run some process on the newly selected data or update
        # other portions of the UI here as necessary.
        print(f"Selected files updated: {self.model.get_selected_files()}")

    def prepare_zip(self) -> Optional[bytes]:
        selected_files = self.model.get_selected_files()
        if not selected_files:
            return None

        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED, False) as zip_file:
            for file_path in selected_files:
                file_name = os.path.basename(file_path)
                print(file_name)
                zip_file.write(file_path, arcname=f"test/{file_name}")

        return zip_buffer.getvalue()

    def update_form_data(self) -> None:
        # This will fail if you haven't called connect on the binding!
        self.form_data_bind.update_in_view(self.model.form)
