# Initial State File

Each row corresponds to a unique **(Store, Product)** pair at a given week.  

| Column                      | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| **Store**                   | Store identifier.                                                           |
| **Product**                 | Product identifier.                                                         |
| **Start Inventory**         | Units available at the beginning of the week.                               |
| **Sales**                   | Actual sales observed during the week.                                      |
| **Missed Sales**            | Units that could not be sold due to stockouts (lost demand).                 |
| **End Inventory**           | Units left at the end of the week (after sales).                            |
| **In Transit W+1**          | Units scheduled to arrive next week (already ordered).                      |
| **In Transit W+2**          | Units scheduled to arrive in two weeks.                                     |
| **Holding Cost**            | Cost of carrying excess inventory (`0.2€ * End Inventory`).                  |
| **Shortage Cost**           | Cost of missed demand (`1.0€ * Missed Sales`).                               |
| **Cumulative Holding Cost** | Running total of holding costs up to this week.                             |
| **Cumulative Shortage Cost**| Running total of shortage costs up to this week.    


# Sales File

Each row corresponds to a unique **(Store, Product)** pair at a given week.
Each column corresponds to a past week of sales, in Initial State we have a total of 157 weeks of history. 
From 12/04/2021 until 08/04/2025.


# In Stock File

For each Store, Product and Week flags whether it has stock available.


# Masterdata File

The **Masterdata** dataset contains information about stores, products, and their hierarchical classifications within the company. It provides a mapping between individual products and their respective categories, departments, divisions, and store formats. This dataset is useful for analysis, reporting, and aggregating data across different organizational levels.

## Columns

| Column Name        | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| **Store**          | Unique identifier for each store.                                           |
| **Product**        | Unique identifier for each product.                                         |
| **ProductGroup**   | Grouping of products based on category segmentation.                        |
| **Division**       | Higher-level classification grouping multiple product groups.               |
| **Department**     | Organizational unit managing multiple divisions.                            |
| **DepartmentGroup**| Broader classification combining multiple departments.                     |
| **StoreFormat**    | Type of store format (e.g., size, layout, or customer segment).             |
| **Format**         | Numeric code representing the store format.                        