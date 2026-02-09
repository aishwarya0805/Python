import pandas as pd

url= 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep='\t')
print(chipo.head(10))

#shape gives number of records
print("Dataset has ",chipo.shape[0],"records")

#What is the number of columns in the dataset
print("This Dataset has", chipo.shape[1],"columns")

#Print the name of all the columns in a list format
print("Column names are:", chipo.columns.tolist())

#How is the dataset indexed?
print("Dataset is indexed by:", chipo.index)

#Which was the most ordered item and how many items were ordered?
most_ordered = (
    chipo
    .groupby('item_name', as_index=False)['quantity']
    .sum()
    .sort_values('quantity', ascending=False)
    .head(1)
)

print(most_ordered)

#Which was the most ordered item in the choice_description column?
most_ordered_choice = (
    chipo
    .groupby('choice_description', as_index=False)['quantity']
    .sum()
    .sort_values('quantity', ascending=False)
    .head(1)
)

print(most_ordered_choice)

#which was the most ordered item in the choice_description. Display only item name not quantity
most_ordered_choice= (
    chipo
    .groupby('choice_description')['quantity']
    .sum()
    .idxmax()
)
print("Most ordered item from Choice Description column is: ",most_ordered_choice)

#How many items were ordered in total?
total_quantity= chipo['quantity'].sum()
print("Total number of items ordered:", total_quantity)

#How many unique items are sold?
unique_items= chipo['item_name'].nunique()
print("Number of unique items sold:", unique_items)

#What is the total revenue of the company?
chipo['item_price'] = chipo['item_price'].str.replace('$', '').astype(float)
total_revenue= (chipo['quantity'] * chipo['item_price']).sum()
print("Total revenue of the company: $", total_revenue)

#How many orders were made in the period?
orders = chipo.order_id.value_counts().count()
print(orders,"orders were made in the period")

#What is the average revenue per order?
avg_orders= chipo.groupby('order_id')[chipo['quantity'] * chipo['item_price']].sum().mean()
print("Average revenue per order: $", round(avg_orders,2))