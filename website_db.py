
import pandas as pd
from sqlalchemy import create_engine

# Read CSV directly
df = pd.read_csv("website_traffic_dataset.csv")

# Create connection
engine = create_engine(
    "mysql+mysqlconnector://root:M084637N@localhost/website_analysis"
)

# Upload dataframe to MySQL
df.to_sql(
    name="traffic_data",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ Data uploaded successfully!")

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+mysqlconnector://root:M084637N@localhost/website_analysis"
)

df = pd.read_sql("SELECT * FROM traffic_data", engine)

print(df.head())
print(df.columns)
print(df.info())
print(df.shape)



