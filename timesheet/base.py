
import pandas


def main():
    print("READ timesheet.xlsx")
    data = pandas.read_excel("timesheet.xlsx", sheet_name="DATA")
    print("SIZE: {}".format(data.shape))
    print("ROWS: {}".format(data.index))
    print("COLS: {}".format(data.columns))
    print("=" * 60)
    print(data)
    print("=" * 60)

    print("UPDATE Name column")
    data["Name"] = data.loc[:, "Name"].apply(lambda n: n.title())
    print("=" * 60)
    print(data)
    print("=" * 60)

    print("ADD OT column")
    data["OT"] = data.loc[:, "Total Hours"].apply(lambda h: h - 40)
    print("=" * 60)
    print(data)
    print("=" * 60)

    print("DROP EmployeeID column")
    data.drop(columns=["EmployeeID"], inplace=True)
    print("=" * 60)
    print(data)
    print("=" * 60)


main()
