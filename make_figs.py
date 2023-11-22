import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from scipy.stats import linregress
import numpy as np

def plot_stacked_hist(dt):
    fig, ax = plt.subplots()
    sns.histplot(dt,x="Year",hue="Book Type",multiple="stack",shrink=4, ax=ax)
    fig.patch.set_facecolor('white')
    fig.savefig("hist_plot.png", bbox_inches='tight')
    plt.close(fig)


def plot_min_max(dt):
	level_over_time_no_sep = dt.drop(labels=['Language', 'Book Title', 'Status', 'Date Started', 'Date Started (Raw)', 
    	'Date Finished (Raw)', 'My Review Headline', 'My Review', 'My Lists', 'Book ID', 'Book Type', 
    	'Series ID', 'Series Title', 'Book Tags (No Spoilers)', 'Book Genre Tags', 'Book Spoiler Tags'],axis=1).groupby("Year Month")
	res_no_sep = level_over_time_no_sep.agg(["min","mean","max"])["Difficulty Level"]
	fig, ax = plt.subplots()
	sns.lineplot(data=res_no_sep, x="Year Month", y="mean", ax = ax)
	sns.lineplot(data=res_no_sep, x="Year Month", y="max", color="C0", ax=ax, style=True, dashes=[(2,2)], legend=False)
	sns.lineplot(data=res_no_sep, x="Year Month", y="min", ax=ax, color="C0", style=True, dashes=[(2,2)], legend=False)
	ax.set_ylabel("Level")
	ax.set_xlabel("Date")
	ax.tick_params(axis='x', rotation=45)
	fig.patch.set_facecolor('white')
	fig.savefig("min_max_plot.png", bbox_inches='tight')
	plt.close(fig)

def plot_over_time_dots(dt):
    subs = pd.DataFrame(dt[["Date Finished","Book Type","Difficulty Level"]])
    subs["Date"] = dt["Date Finished"].map(datetime.toordinal)
    fig, ax = plt.subplots()
    sns.scatterplot(data=dt, x="Date Finished", y="Difficulty Level", hue="Book Type", ax=ax)
    ax.set_ylabel("Level")
    ax.set_xlabel("Date")
    ax.tick_params(axis='x', rotation=45)
    ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    handles, labels = ax.get_legend_handles_labels()
    all_regs = get_regs(subs, labels)
    for i, v in enumerate(labels):
        tp_dt = subs[subs["Book Type"]==v]
        reg = all_regs[i]
        x1,x2 = min(tp_dt["Date Finished"]), max(tp_dt["Date Finished"])
        y1, y2 = min(tp_dt["Date"]), max(tp_dt["Date"])
        ax.plot([x1,x2], reg.intercept + reg.slope*np.array([y1,y2]), label=v)
    fig.patch.set_facecolor('white')
    fig.savefig("with_regs.png", facecolor=plt.gcf().get_facecolor(), transparent=False,bbox_inches='tight')
    plt.close(fig)

def get_regs(subs, labels):
    all_regs = []
    for v in labels:
        tp_dt = subs[subs["Book Type"]==v]
        reg = linregress(tp_dt["Date"], tp_dt["Difficulty Level"])
        all_regs.append(reg)
    return all_regs

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        printf("Usage:",sys.argv[0],"csv_file")
        exit()
    dat = pd.read_csv(sys.argv[1])
    dat["Date Finished"] = pd.to_datetime(dat["Date Finished"])
    finished = pd.DataFrame(dat[dat["Status"]=="finished"])
    finished["Year"] = list(map(lambda x: datetime.strptime(x.strftime("%Y"),"%Y"), finished["Date Finished"].dt.to_pydatetime()))
    finished["Year Month"] = list(map(lambda x: datetime.strptime(x.strftime("%Y-%m"),"%Y-%m"), finished["Date Finished"].dt.to_pydatetime()))
    
    final_data = finished[finished["Year Month"]>datetime(2021,6,1)]
    plot_stacked_hist(finished)
    plot_min_max(final_data)
    plot_over_time_dots(final_data)




