from pyspark.sql import SparkSession
from pyspark.sql.functions import col, dayofweek, sum, mean


spark = SparkSession.builder.appName("SundaySalesAnalysis").getOrCreate()



merged_data = (
    fact_internet_sales
    .join(dim_customer, "CustomerKey", "inner")
    .join(dim_product, "ProductKey", "inner")
)

# Filtering
filtered_data = (
    merged_data
    .filter(dayofweek(col("OrderDate")) == 1)
    .filter(col("Color") == "Silver")       
    .filter(col("Size").isNotNull()) 
    .filter(col("Weight") > 10)               
    .filter(col("YearlyIncome") > 100000.0)  
    .filter(col("NumberChildrenAtHome") > 1)  
)

#groupping
aggregated_data = (
    filtered_data
    .groupby("CustomerKey", "FirstName")
    .agg(
        sum("TaxAmt").alias("TotalTaxAmt"),
        mean("SalesAmount").alias("AverageSalesAmount"),
        mean("TotalProductCost").alias("AverageTotalProductCost")
    )
)


final_data = aggregated_data.drop("CustomerKey").orderBy("FirstName")


final_data.show()
