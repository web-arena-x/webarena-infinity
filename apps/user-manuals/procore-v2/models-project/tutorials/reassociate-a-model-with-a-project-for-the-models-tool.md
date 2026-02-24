# Reassociate a Model with a Project for the Models Tool

Source: https://v2.support.procore.com/product-manuals/models-project/tutorials/reassociate-a-model-with-a-project-for-the-models-tool

---

## Background

When you associate a model with a project in Procore, you are able to publish models from NavisworksÂ® so that you can view them in Procore.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' on the project's Models tool on the project you will associate the model with.
- **Additional Information:**

  - A model can be associated (i.e., linked) to only one (1) Procore project at a time. However, a single Procore project can host multiple models.
  - If you need to associate a model that is currently linked to a different project, you must first delete the existing association in that projectâs Models tool. See [Delete a Model](/product-manuals/models-project/tutorials/delete-a-model).

## Prerequisites

- [Delete any Procore models associated with the model file](/product-manuals/models-project/tutorials/delete-a-model)
- Levels/Location associations must be removed from the model ('level' must be deleted from the plugin-side).
- Delete any Coordination Issues associated with the model using the web application or NavisworksÂ® plugin.

## Steps

1. Open the model in NavisworksÂ® that you want to associate with a Procore project.
2. Click the **Procore** tab.
3. Click **Settings.**  
    This opens a Settings window.
4. Use the **Company** and **Project** drop-down menus to select the project that you want to associate the model to.  
   ***Tip!*** Use the search bar to search by project name or number.
5. Click **Update**.