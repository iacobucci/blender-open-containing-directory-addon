bl_info = {
    "name": "Open containing directory",
    "blender": (2, 80, 0),
    "category": "File",
}

import bpy
import os
import subprocess

class OpenContainingDirectory(bpy.types.Operator):
    bl_idname = "file.open_containing_directory"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Open containing directory"         # Display name in the interface.
    bl_options = {'REGISTER'}  # Enable undo for the operator.

    def execute(self, context):
        # Get the filepath of the current .blend file
        blend_file_path = bpy.data.filepath

        if not blend_file_path:
            self.report({'WARNING'}, "The current file is not saved yet.")
            return {'CANCELLED'}

        # Extract the directory path
        directory_path = os.path.dirname(blend_file_path)

        try:
            # Use xdg-open to open the directory
            subprocess.run(['xdg-open', directory_path], check=True)
            self.report({'INFO'}, f"Opened directory: {directory_path}")
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, f"Failed to open directory: {e}")
            return {'CANCELLED'}

def menu_func(self, context):
    self.layout.operator(OpenContainingDirectory.bl_idname)

def register():
    bpy.utils.register_class(OpenContainingDirectory)
    bpy.types.TOPBAR_MT_file.append(menu_func)  # Adds the new operator to an existing menu.

def unregister():
    bpy.utils.unregister_class(OpenContainingDirectory)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
