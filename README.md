# ValuationService

## Requirements
You are building a valuation service.
Read the input data. From products with particular matching_id take those with
the highest total price (price * quantity), limit data set by top_priced_count and
aggregate prices.
Unit tests are required.

## Input
In the input there are three files containing:
- data.csv - product representation with price,currency,quantity,matching_id
- currencies.csv - currency code and ratio to PLN, ie. GBP,2.4 can be
converted to PLN as follows 1 PLN * 2.4
- matchings.csv - matching data matching_id,top_priced_count
## Output
Save the results as top_products.csv. Output file shall have five columns:
matching_id, total_price, avg_price, currency, ignored_products_count.
