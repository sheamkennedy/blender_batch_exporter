# Blender Add-on: Batch Exporter

It is often easier to work with multiple objects in a single Blender file, for example when different models share the same texture. This add-on makes it possible to export multiple root objects (and their children) from a single Blender file to individual files on disk. glTF and FBX are currently supported, though adding support for other file types is quite easy.

Features Added:
* **Export Prefix** - Many game engines support prefixes which can be added to the filename models in order to resolve tedious model setup when importing into the game engines. With this feature the user can now type an Export Prefix into a textfield before batch exporting. The prefix will be added to every model that is exported saving game developers a lot of time in their workflow between Blender and their chosen game engine.
* **Export Suffix** - Many game engines support suffixes which can be added to the filename models in order to resolve tedious model setup when importing into the game engine (For instance Godot game engine uses suffixes like: -col or -rigid in order to create collisions and rigidbody physics behavior on import). With this feature the user can now type an Export Suffix into a textfield before batch exporting. The suffix will be added to every model that is exported saving game developers a lot of time in their workflow between Blender and their chosen game engine.

## Installation

* Download the latest release from [here](https://github.com/sheamkennedy/blender_batch_exporter/releases/tag/doffu-batch-exporter) or clone it using Git to your custom Blender `...\scripts\addons\` folder.
* From Blender's Main Menu:
  * *Edit / Preferences*
  * Click the *Install* button and select the downloaded zip file.
  * Check the check-box next to the add-on to activate it.
  * Once install is active, the add-on window can be found under Scene > Batch Exporter (Shown in visual aid below).
 
  ![batch-exporter-visual-instructions](https://github.com/sheamkennedy/blender_batch_exporter/assets/13323856/d40e294c-8e23-407e-bf64-5a9ade64ded1)

  
## Batch Exporter Configuration

The add-on can be found in the *Scene Properties* tab in Blender.

* *Export Directory* - The location to export model file to. Note that the add-on tries to use relative paths from the Blender file if possible. (This can be disable at the top of the add-on's script file.)
* *Export Format* - The file format used to export. The built-in exporter must be installed for the selected file type.
* *File Format Settings* - After selecting an export format, format-specific settings are displayed. Currently this list includes some of the more common settings. If a new setting needs to be added, it is quite easy to expose one in the add-on's script.
*  *Export Prefix* - Input a prefix which will be prepended to the exported filenames. This is useful if you're later importing models into a game engine that supports prefixes for speeding up model setup.
*  *Export Suffix* - Input a suffix which will be appended to the exported filenames. This is useful if you're later importing models into a game engine that supports suffixes for speeding up model setup.
* *Set Exported / Set Not-Exported* - This sets a per-object property to mark an object for export. This can also be changed on a selected object from the *Object Properties* tab in Blender.
* *Export All / Selected* - Click to export all configured root objects or just the selected ones. (`Ctrl+Alt E` / `Ctrl+Alt+Shift E`)
