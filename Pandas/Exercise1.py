# Check pandas version
import pandas as pd
print(pd.__version__," is the current pandas version")

# Create a dataset and display it as a DataFrame
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

# Print the DataFrame
print("DataFrame:")
print(myvar)


