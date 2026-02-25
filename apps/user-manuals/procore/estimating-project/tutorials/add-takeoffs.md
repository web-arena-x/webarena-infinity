# Add Takeoffs

Source: https://v2.support.procore.com/product-manuals/estimating-project/tutorials/add-takeoffs

---

## Background

A takeoff extracts quantities from a drawing or model and associates with items in your cost catalog to create estimates. Using the Takeoffs tab in Procore's Estimating, Bid Board, or Portfolio Planning tool, you can add and manage a wide variety of takeoffs for different trades.

## Things to Consider

- [Required User Permissions](/product-manuals/bid-board-company/permissions) for the **Bid Board** tool.
- [Required User Permissions](/product-manuals/estimating-project/permissions) for the **Estimating** tool.
- [Required User Permissions](/product-manuals/portfolio-planning-company/permissions) for the **Portfolio Planning** tool.
- Before starting a takeoff, make sure that the plan scale is properly configured. See [Set the Drawing Scale for Takeoffs](/product-manuals/estimating-project/tutorials/set-the-drawing-scale-for-takeoffs).
- Premium features with the star icon are only available for paid Procore customer accounts.

## Video

## Steps

1. Navigate to the **Bid Board** or **Portfolio Planning** tool and select the **project**. 
    OR Navigate to the project's **Estimating** tool.
2. Click the **Takeoffs** tab.
3. Select the **drawing** and **revision number**.
4. Click **Create New Takeoff Layer**.
5. Enter a material name, or click **Browse Catalog** to select an item from the material Cost Catalog. 
   *Note:* If you select a material from the catalog, always check to make sure that it matches the clientâs specification and unit prices.
6. Select a **Measurement Type**.
7. Select **Unit of Measurement**, **Color**, **Symbol**, and **Line Width** as necessary for your measurement.
8. Click **Create** to initiate 'Drawing Mode'. Then follow the steps below for the relevant takeoff:

   - **Count Measurements**

     - Do one of the following:

       1. [Run Auto Count](/product-manuals/estimating-project/tutorials/run-auto-count-takeoffs) to count similar symbols using Procore advanced symbol recognition feature.
       2. On the drawing, click each symbol to manually count it in your takeoff.
   - **Linear or Count by Distance Takeoffs**

     1. On the drawing, point and click the cursor at the starting point of the measurement and repeat it by segment until you reach the endpoint of the linear measurement. 
         *Note:* Add multiple points or segments to accommodate the preferred linear measurement.

        1. To delete a segment, press the BACKSPACE or DELETE key on your keyboard.
        2. To delete the entire line placement, press the ESC key on your keyboard.2.
     2. A linear measurement will appear:

        1. Double-click to complete the measurement. 
            The measured distance value will appear under the takeoff name.
   - **Linear with Drop Takeoffs**

     1. On the drawing, point and click the cursor at the starting point of the measurement, click the location of each drop point until you reach the end of the linear measurement. *Note:* To create automatic labels for Drop length points, select the **vertical ellipsis** next to the the takeoff layer and move the **Automatically Label Drops toggle** ON. Labeling can include a Prefix, Suffix, and Incremental numbering.
     2. **Double-click** to complete the measurement.

        1. To delete a segment, press the BACKSPACE or DELETE key on your keyboard.
        2. To delete the entire placement, press the ESC key on your keyboard.
     3. Set the drop length for each drop point.

        1. To set a default drop length for all drop points in the takeoff layer, click the **vertical ellipsis** next to the the takeoff layer. Then enter the default drop length.
        2. To set a drop length for an individual drop point, **double click** the drop point on the drawing. Enter the drop length and click **Confirm**.
   - **Area or Volume Takeoffs**

     - Do one of the following:

       1. [Run Auto Area Takeoff](/product-manuals/estimating-project/tutorials/run-automated-area-takeoffs) to automatically detect areas in a floor plan.
       2. To manually measure, click the starting point of the area followed by different points to cover the area that you want to measure on the drawing.

          1. To delete a point, press the BACKSPACE or DELETE key on your keyboard.
          2. Delete multiple points by pressing the BACKSPACE key one point at a time.
          3. To delete the entire measured area, press the ESC key on your keyboard.
       3. Double-click to complete the measurement. The selected area will be highlighted by the selected color, and the measured area will appear under the takeoff name.
9. To end 'Drawing Mode', **clear the checkbox** for the takeoff layer.
10. *Optional:* You can add additional parameters for the takeoff to add more detail for the set on the estimate.
11. In the list of takeoffs, click the **vertical ellipsis** icon for the takeoff you are working on.
12. Click **Additional Parameters**.
13. Click the toggle ON for a parameter that you want to add details for.
14. Enter information as necessary.
15. Click **Close**