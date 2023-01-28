import matplotlib.pyplot as plt
import seaborn as sns
from IPython import display
display.set_matplotlib_formats("svg")


# customizations
plt.rcParams["font.family"] = "monospace"
plt.rcParams["font.size"] = 8
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.titlecolor"] = "black"
plt.rcParams["axes.titlesize"] = 10
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.labelcolor"] = "darkgray"
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["axes.edgecolor"] = "darkgray"
plt.rcParams["axes.linewidth"] = 0.2
plt.rcParams["ytick.color"] = "darkgray"
plt.rcParams["xtick.color"] = "darkgray"

tips = sns.load_dataset("tips")
print(tips.head(3))

# let's create a new calculated column that represents the tip
# as a percent of the total bill
tips["perc_bill"] = tips["tip"] / tips["total_bill"] * 100
print(tips.head())

# Creating a figure/axes
fig, ax = plt.subplots()

plt.scatter(
        tips["total_bill"],
        tips["perc_bill"],
        color="darkgray",
        alpha=0.3
)

plt.show()

tips_highlight = tips.query("perc_bill >= 20")

plt.scatter(
        tips_highlight["total_bill"],
        tips_highlight["perc_bill"],
        color="indigo",
        alpha=0.7
)

plt.show()

fig, ax = plt.subplots()

plt.scatter(
        tips["total_bill"],
        tips["perc_bill"],
        color="darkgray",
        alpha=0.3
)

tips_highlight = tips.query("perc_bill >= 20")

plt.scatter(
        tips_highlight["total_bill"],
        tips_highlight["perc_bill"],
        color="#5D3FD3",
        alpha=0.7
)

title_top = "How many waiters receive tips that represent more"
title_bottom = "\nthan 20% of total bill"
title = title_top + title_bottom

plt.title(title,
          loc="left", pad=5)
plt.xlabel("Total bill ($)")
plt.ylabel("Tip: % of \ntotal bill ($)", rotation=0, labelpad=35)
plt.text(15, 35,
         "Only 1 of 4 waiters receive at least\n20% of total bill as a tip",
         color="#5D3FD3",
         verticalalignment="center",
         ha="left",
         size=7)
plt.tight_layout()
plt.show()
