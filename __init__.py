# Copyright 2022 by Hextant Studios. https://HextantStudios.com
# This work is licensed under GNU General Public License Version 3.
# License: https://download.blender.org/release/GPL3-license.txt
# Modified by Shea Kennedy, Oct. 30 2023.
# Modifications made:
# --- Changed bl_info to reflect project branch.

import bpy
bl_info = {
    "name": "Batch Exporter",
    "author": "Doffu (Shea Kennedy) + Hextant Studios",
    "version": (1, 0, 1),
    "blender": (3, 2, 0),
    "location": "Scene > Batch Exporter",
    "description": "A batch exporter which currently supports glTF and FBX formats.",
    "doc_url": "https://github.com/sheamkennedy/blender_batch_exporter",
    "category": "Import-Export",
}


# Include *all* modules in this package for proper reloading.
#   * All modules *must* have a register() and unregister() method!
#   * Dependency *must* come *before* modules that use them in the list!
register, unregister = bpy.utils.register_submodule_factory(__package__, (
    'batch_exporter',
))
