# %%
import pandas as pd
import numpy as np
import os
from datetime import datetime
from datetime import date

# %%
def splitFireSNOTEL(site_name, fire_dict, variable_type, disruption_dates, filepath, end_date=None):
    """
    splitFireSNOTEL will split up the dataframe before and after a given fire event occured at a site.
    It returns two dataframes, the first of which is all data prior to the fire event, and the second
    being the data after the fire event (inclusive).

    If end_date option is included, this will report after-fire data up to the given date.

    Example:
    filepath = 
    disruption_dates = pd.read_excel(os.path.join(filepath,'snotel_fire_data.xlsx'))
    name = 'Grouse Camp'
    variable = 'swe'
    before, after = splitLogSNOTEL(name, variable, disruption_dates, filepath)

    Args:
        site_name (string): SNOTEL site name
        fire_dict (dictionary): dictionary of fire altered sites and partner sites
        variable_type (string): 'swe' or 'depth'
        disruption_dates (dataframe): dataframe of snotel fire disturbances, located here: 
        filepath (string): path location to file
        end_date (string, optional): date to end after-disturbance dataset. Defaults to None.

    Returns:
        df_b: dataframe before disturbance
        df_a: dataframe after disturbance
    """
    if site_name in fire_dict.keys():
        site = site_name
    elif site_name in fire_dict.values():
        site = list(fire_dict.keys())[list(fire_dict.values()).index(site_name)]
        filepath = os.path.join(filepath,'paired_locs_new')
    else:
        print('Site not in list, ensure spelling is correct')
    # read in disruption date from provided file
    print(site)
    disruption_date = disruption_dates[disruption_dates['site_name']==site]['fire_start_date'].to_list()[0]
    # write out the file name using site name and snow variable of interest (swe or depth)
    filename = os.path.join(filepath,site_name+'_'+variable_type+'.csv')
    site_df = pd.read_csv(filename)
    # make sure datetime is datetime type
    site_df['datetime'] = pd.to_datetime(site_df['datetime'])
    # set index to datetime
    site_df = site_df.set_index('datetime')
    # filter before and after date of disturbance
    df_b = site_df[site_df.index < disruption_date]
    # if end_date was included, the after-fire dataframe will report data up to that date
    if end_date is not None:
       df_a = site_df[(site_df.index >= disruption_date) & (site_df.index <= end_date)] 
    else:
        df_a = site_df[site_df.index >= disruption_date]
    return df_b, df_a

# %%

def splitLogSNOTEL(site_name, logging_dict, variable_type, filepath, end_date=None):
    """splitLogSNOTEL will split up the dataframe before and after a given logging event occured at a site.
    It returns two dataframes, the first of which is all data prior to the logging event, and the second
    being the data after the logging event (inclusive).

    The disruption dates are stated as the first day of each water year on the year the disturbance occurred.

    If end_date option is included, this will report after-logging data up to the given date.
    
    Example:
    name = 'Mowich'
    variable = 'swe'
    before, after = splitLogSNOTEL(name, variable, filepath)

    Args:
        site_name (string): SNOTEL site name
        logging_dict (dictionary): dictionary of logging altered sites and partner sites
        variable_type (string): 'swe' or 'depth'
        filepath (string): path location to file
        end_date (string, optional): date to end after-disturbance dataset. Defaults to None.

    Returns:
        df_b: dataframe before disturbance
        df_a: dataframe after disturbance
    """
    if site_name in logging_dict.keys():
        site = site_name
    elif site_name in logging_dict.values():
        site = list(logging_sites.keys())[list(logging_sites.values()).index(site_name)]
        filepath = os.path.join(filepath,'paired_locs')
    else:
        print('Site not in list, ensure spelling is correct')
    # estimated disturbance dates as first day of WY
    disruption = {'Mowich':datetime(2002,10,1), 'Seine Creek':datetime(2006,10,1)}
    # read in disruption date from dictionary
    disruption_date = disruption[site]
    # write out the file name using site name and snow variable of interest (swe or depth)
    filename = os.path.join(filepath,site_name+'_'+variable_type+'.csv')
    site_df = pd.read_csv(filename)
    # make sure datetime is datetime type
    site_df['datetime'] = pd.to_datetime(site_df['datetime'])
    # set index to datetime
    site_df = site_df.set_index('datetime')
    # filter before and after date of disturbance
    df_b = site_df[site_df.index < disruption_date]
    # if end_date was included, the after-fire dataframe will report data up to that date
    if end_date is not None:
       df_a = site_df[(site_df.index >= disruption_date) & (site_df.index <= end_date)] 
    else:
        df_a = site_df[site_df.index >= disruption_date]
    return df_b, df_a

# %%
filepath = r'C:\Users\dlhogan\OneDrive - UW\Documents\GitHub\CEWA565_project\data\logged_sites'
logging_sites = {'Seine Creek':'Saddle Mountain',
                 'Mowich':'Burnt Mountain'}
name = 'Burnt Mountain'
variable = 'swe'
before, after = splitLogSNOTEL(name, logging_sites, variable, filepath)


# %%



