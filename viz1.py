import matplotlib.pyplot as plt
import pandas as pd


def lineplot(df, headers):
    """creates line chart and saves in a file.

    Parameters:
        - df (dataframe): Dataset.
        - headers (strings[]): The headers of Datasets each column 
                               represents a line

    Example:
        >>> lineplot(df, headers)

    Returns:
        None
    """

    plt.figure(figsize=(12, 12))
    for head in headers:
        print(df[head])
        plt.plot(df["Year"], df[head], label=head)

    # labelling
    plt.xlabel("Year")
    plt.ylabel("No of Baggage Complaints")

    # removing white space left and right. Both standard and pandas min/max
    # can be used
    plt.xlim(min(df["Year"]), df["Year"].max())
    plt.legend()
    plt.title("Baggage Complaints Trends by Different Airlines: 2004-2010.")
    # save as png
    plt.savefig("complaints_vs_year.png")
    plt.show()

    return


def pieplot(df):
    """creates pie chart and saves in a file.

    Parameters:
        - df (dataframe): Dataset.

    Example:
        >>> pieplot(df)

    Returns:
        None
    """

    plt.figure(figsize=(8, 8))

    colors = ["lightblue", "orange", "lightgreen"]
    explode = (0, 0, 0)

    plt.pie(
        df["Baggage"],
        explode=explode,
        labels=df["Airline"],
        colors=colors,
        autopct="%1.1f%%",
        shadow=True,
        startangle=140,
    )
    plt.title("Distribution of Total Baggage Complaints ")
    plt.legend()
    plt.savefig("baggage_comp_dist.png")
    plt.show()
    return


def barplot(df):
    """creates bar chart and saves in a file.

    Parameters:
        - df (dataframe): Dataset.

    Example:
        >>> barplot(df)

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))

    years = df["year"]
    men_health_insurance_coverage = df["men"]
    women_health_insurance_coverage = df["women"]
    plt.bar(
        years,
        men_health_insurance_coverage,
        label="Men Health Insurance Coverage in percentage",
        alpha=0.7,
    )
    plt.bar(
        years,
        women_health_insurance_coverage,
        label="Women Health Insurance Coverage in percentage",
        alpha=0.7,
        bottom=men_health_insurance_coverage,
    )
    plt.xlabel("Year")
    plt.ylabel("Health Insurance Coverage in Percentage")
    plt.title(
        "Percentage of Men and Women who are covered by Health Insurance \
        in UK(1979-2019.)"
    )
    plt.legend()
    plt.savefig("health_insurance_coverage.png")
    plt.show()
    return


# Reading the first dataset and plotting a line plot for different airlines
csv_file_path = "datasets/baggagecomplaints.csv"
df = pd.read_csv(csv_file_path)
summary_year = df.groupby(["Airline", "Year"])["Baggage"].sum().reset_index()
pivoted_df = summary_year.pivot(
    index="Year", columns="Airline", values="Baggage").reset_index()
lineplot(pivoted_df, ["American Eagle", "Hawaiian", "United"])

# Plotting the pie chart on the baggage complaints based on the airlines
summary_airline = df.groupby(["Airline"])["Baggage"].sum().reset_index()
total_baggage_complaints = summary_airline["Baggage"].sum()
summary_airline["Baggage"] = (
    summary_airline["Baggage"] / total_baggage_complaints) * 100
pieplot(summary_airline)

# Reading the dataset2 and plotting the bar chart on health insurance cover
csv_file_path2 = "datasets/health_insurance_coverage.csv"
df_health_insurance = pd.read_csv(csv_file_path2)
summary_barplot = df_health_insurance.loc[:, ["year", "men", "women"]]
rows_to_keep = summary_barplot.index % 5 == 0
summary_barplot = summary_barplot[rows_to_keep]
barplot(summary_barplot)
