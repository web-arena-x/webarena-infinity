# View a Model

Source: https://v2.support.procore.com/product-manuals/models-project/tutorials/view-a-model

---

## Things to Consider

- [Required User Permissions](/product-manuals/models-project/permissions)

## Prerequisites

- At least one model must be published to the project. See [Publish a Model to Procore](/product-manuals/models-project/tutorials/publish-a-model-to-procore).

## Steps

1. Navigate to the project's **Models** tool.
2. Click the model that you want to view in the 3D Model Viewer.
3. Options when viewing a model include:

   - Core Navigation Controls

     - Navigational Aids
     - Navigation Modes
     - Shortcut Menu
   - Additional Actions & Keyboard Commands
   - Collaboration Tools

### Core Navigation Controls

Efficiently navigate your model using a variety of camera modes and aids.

#### Navigational Aids

Use these navigational aids when viewing the model.

| **Aid** | **Keyboard Shortcut** | **Primary Function** | Navigation Options |
| --- | --- | --- | --- |
| **Home** | **CTRL+O** (Windows) **CMD+0** (Mac) | Click Home to return to the model's Home viewpoint. | Standard navigation with pan, zoom, and rotate controls. |
| **2D Drawing View** | - | Click the 2D drawing thumbnail to open a top-down view. | Click to place a position mark and double-click to jump to that location in the 3D model. |

#### Navigation Modes

Select a mode from the toolbar to control the camera movement.

| **Mode** | **Keyboard Shortcut** | **Primary Function** | **Navigation Options** |
| --- | --- | --- | --- |
| **Default** | **V** | Standard navigation with pan, zoom, and rotate controls. | **Left-click + drag:** Rotate camera **Scroll:** Move forward/backward **Middle-click + drag:** Pan camera **SPACEBAR+left-click**: Pan camera |
| **Fly** | **F** | Navigate the model from a first-person perspective at variable speeds. *Note:* The velocity of the camera movement increases or decreases depending on how far you move your mouse cursor. | **Left-click + drag (up/down):** Move forward/backward **Left-click + drag (left/right):** Pan camera **Scroll:** Rotate camera up/down **Middle-click + drag**: Move the camera perpendicularly. **SPACEBAR+left-click**: Move the camera perpendicularly. |
| **Orbit** | **O** | Rotate the camera around a fixed point. | **Left-click object + drag:** Orbit around the click point. **Left-click a space + drag:** Orbit the model's center. **Middle-click + drag**: Move the camera perpendicularly around an object. **SPACEBAR+left-click**: Move the camera perpendicularly around an object |
| **Views** | **ALT+V** (Windows) **OPTION+V** (Mac) | Access and navigate to viewpoints created in NavisworksÂ®. *Note:* Viewpoints must be imported into the viewer when publishing models. See [Publish a Model to Procore](/product-manuals/models-project/tutorials/publish-a-model-to-procore) or [Publish a Model from the Documents Tool](/product-manuals/documents-project/tutorials/publish-a-model-from-the-documents-tool). |  |
| **Objects** | **ALT+O** (Windows) **OPTION+O** (Mac) | Manage the model hierarchy and visibility in the Objects panel. See [Search for Objects in a](/product-manuals/models-project/tutorials/search-for-objects-in-a-model) [Model](/product-manuals/models-project/tutorials/search-for-objects-in-a-model) and [Show or Hide Objects in a Model](/product-manuals/models-project/tutorials/show-or-hide-objects-in-a-model). | - **Search**: Find objects by name. The results will highlight matching objects in the model tree. - **Toggle Visibility**: Click **show**  or **hide**  to control object or level visibility. - **Bulk Actions**: Select multiple objects using the checkboxes to perform actions like **Hide**, **Isolate**, or **Zoom to Selection**. |
| **Properties** | **ALT+P** (Windows) **OPTION+P** (Mac) | Inspect the BIM data embedded in model objects in the Properties panel. See [View Object Properties in a Model](/product-manuals/models-project/tutorials/view-object-properties-in-a-model). | Select an object in the model to populate its data:   - **Default Tab**: Displays a curated list of common properties. - **All Properties Tab**: Displays all metadata from the authoring application. - **Search**: Filter the property list to find specific parameters. |
| **Measure** | **M** | Calculate the shortest distance between two points or objects. See [Measure the Distance Between Objects in a Model](/product-manuals/models-project/tutorials/measure-the-distance-between-objects-in-a-model). | - |
| **Section Box** | - | Click and drag to adjust a section box to slice through the model to reveal internal components by clicking and dragging the sectioning planes. | Choose an option from the drop-down menu:   - **Display Planes**: Shows or hides the section planes. - **Reset Planes**: Resets the section planes. - **Zoom to Box Extents**: Zooms to the extents of the section box. |
| **X-Ray Mode** | - | Isolate selected objects while retaining the rest of the model in a simplified, transparent view for context. See [View a Model in X-Ray Mode](/product-manuals/models-project/tutorials/view-a-model-in-x-ray-mode). | - |
| **Settings** | - | Click the gear icon to change the default measurement units. | Select a measurement from the drop-down:   - Ft' In" - Meters - Millimeters |

#### Shortcut Menu

A shortcut menu is available in all modes. To open the menu, right-click to choose one of these options:

- **Hide Object:** Hide the selected object
- **Hide Similar: Hide all objects with the same name.**
- **Isolate:** Isolate the selected object in the view.
- **Isolate in X-Ray Mode:** Activate X-Ray mode, which isolates selected objects while simplifying the rest of the model. See [View a Model in X-Ray Mode](/product-manuals/models-project/tutorials/view-a-model-in-x-ray-mode).
- **Isolate in Section Box**. Creates a tight, 3D-cropped view called a section box around selected object(s).
- **View Properties:** Open the Properties window for the selected object.
- **Zoom to Selection:** Zoom to the selected object's bounding box.

### Additional Actions & Keyboard Commands

| **Action** | **Keyboard Command** |
| --- | --- |
| Return to **Home Viewpoint** | **CTRL+0** (Windows) **CMD+0** (Mac) |
| Select **Default** tool | **V** |
| Select **Fly** tool | **F** |
| Select **Orbit** tool | **O** |
| Open **Views** window | **ALT+V** (Windows) **OPTION+V** (Mac) |
| Open **Objects** window | **ALT+O** (Windows) **OPTION+O** (Mac) |
| Open **Properties** window | **ALT+P** (Windows) **OPTION+P** (Mac) |
| Select **Measure** tool | **M** |
| Look left | **Left arrow** |
| Look right | **Right arrow** |
| Look up | **Up arrow** |
| Look down | **Down arrow** |
| Move forward | **W** |
| Move left | **A** |
| Move backward | **S** |
| Move right | **D** |
| Move up vertically | **E** |
| Move down vertically | **Q** |
| Hide selected object | **H** |
| Return to the last selected tool Close any open windows Hide measurement info | **Esc** |

### Collaboration Tools

#### View Active Collaborators

Each user viewing a model appears as a blue dot with their name. To jump to their viewpoint, click their name and select **Go to Location**. To learn more, see [View Active Collaborators on a Model](/product-manuals/models-project/tutorials/view-active-collaborators-on-a-model).