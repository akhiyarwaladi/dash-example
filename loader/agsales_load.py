import pandas as pd


def get_agsales():
    sales_plot = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/sales_plot_oshop.csv', \
                        sep='\t')

    return sales_plot