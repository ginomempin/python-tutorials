
import pandas

print("READ timesheet.xlsx")
df = pandas.read_excel("timesheet.xlsx", sheet_name="DATA")
print("SIZE: {}".format(df.shape))
print("ROWS: {}".format(df.index))
print("COLS: {}".format(df.columns))
print("=" * 60)
print(df)
print("=" * 60)

print("UPDATE Name column")
df["Name"] = df.loc[:, "Name"].apply(lambda n: n.title())
print("=" * 60)
print(df)
print("=" * 60)

print("ADD OT column")
df["OT"] = df.loc[:, "Total Hours"].apply(lambda h: h - 40)
print("=" * 60)
print(df)
print("=" * 60)

print("DROP EmployeeID column")
df.drop(columns=["EmployeeID"], inplace=True)
print("=" * 60)
print(df)
print("=" * 60)
