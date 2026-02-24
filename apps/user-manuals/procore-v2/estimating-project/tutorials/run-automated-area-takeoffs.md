# Run Automated Area Takeoffs

Source: https://v2.support.procore.com/product-manuals/estimating-project/tutorials/run-automated-area-takeoffs

---

## Background

Automated area takeoff uses machine learning technology to automatically detect areas in a floor plan. Instead of needing to manually trace outlines of each room while adding a takeoff, you'll be able to click once on a room to have Procore automatically detect the area.

## Things to Consider

- [Required User Permissions](/product-manuals/bid-board-company/permissions) for the **Bid Board** tool.
- [Required User Permissions](/product-manuals/estimating-project/permissions) for the **Estimating** tool.
- [Required User Permissions](/product-manuals/portfolio-planning-company/permissions) for the **Portfolio Planning** tool.
- Before starting a material count, make sure that the drawing scale is properly configured. See [Set the Drawing Scale for Takeoffs](/product-manuals/estimating-project/tutorials/set-the-drawing-scale-for-takeoffs).
- Automated Area Takeoff can be used on floor plans, concrete, and roofing.
- Since this feature uses machine learning technology, more accurate results are achieved over time. In addition, results are cached so that subsequent runs are completed faster.
- Premium features with the **star** icon are only available for paid Procore customer accounts.

## Steps

1. Navigate to the **Bid Board** or **Portfolio Planning** tool and select the **project**. 
    OR Navigate to the project's **Estimating** tool.
2. Click the **Takeoffs** tab.
3. Select the drawing that you want to add takeoffs to.
4. Click the relevant takeoff, or .
5. Click **Auto Area Takeoff**.
6. Select one of the following options:

   - **Run on all drawings**
   - **Run on active drawing only**
   - **Manually select drawings to run on**
7. Click **Continue**.
8. In the 'Processing Algorithm' column, select the type of drawing that you want to run detection on:

   - **Architectural Floor Plan**
   - **Concrete**
   - **Roofing**
9. Click **Run Area Detection**.
10. If you want to work on other drawings while the detection is in progress, click **Run in Background**. 
    *Note:* This closes the detection window and adds a persistent 'Detecting Rooms' notification to the takeoff page. When the process is complete, the message changes to 'Rooms are Ready for Detection'. The notification can be clicked at any time to cancel the detection or review the detected rooms.
11. After the process is complete, review the areas that you want to select as takeoffs.

- Click on each room that you want to select. 
   OR
- Click **Select All** to select all rooms that were detected. 
 *Note:* You can deselect a room if needed by clicking on it.

1. When you are done selecting rooms, click **Use Selected Takeoffs**. 
    This completes the takeoff.