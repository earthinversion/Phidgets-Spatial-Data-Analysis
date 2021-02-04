# ======================================================================================================================================================
# Title:  Reads the sequential csc files in the directory csvdata and 
# write it into mseed files using different interpolation algorithms; also plot the three component recording from the csv file
# Author: Utpal Kumar
# Date:   04 Feb 2021
# ======================================================================================================================================================

import pandas as pd
import os, glob
import matplotlib.pyplot as plt
from obspy import Stream, Trace
from obspy.core import UTCDateTime
import time


dataloc = "csvdata/"
figpath = "figs/"
mseeddata = "mseeddata/"
allDataFiles = glob.glob(dataloc+"*.csv")
# allDataFiles = allDataFiles[0:2]
print(allDataFiles)


dataname0 = os.path.splitext(os.path.basename(allDataFiles[0]))[0]
print(dataname0)

network = "RFI"
station = dataname0.split("_")[0]
startTime = 0
# appended_data = []
appended_df=pd.DataFrame()
for idx, fullFilename in enumerate(allDataFiles):
    dataname = os.path.splitext(os.path.basename(fullFilename))[0]
    df = pd.read_csv(fullFilename, header=None, names=['Datetime', "X", "Y", "Z"])

    df["Datetime"] = pd.to_datetime(df["Datetime"])
    if idx==0:
        startTime = df.loc[0, "Datetime"]
    df["timeDelta"] = df["Datetime"].diff()
    print(fullFilename, df.shape)
    # print(df.shape)
    df = df.iloc[1:-1,:]
    # print(df.head(1))
    # print(df.tail(1))
    appended_df=appended_df.append(df,ignore_index=True)
    
# appended_df = pd.concat(appended_data)
print("-------")
print(appended_df.head(1))
print(appended_df.tail(1))
print(appended_df.shape)
print(f"data starttime is {startTime}")

stats = {}
stats['network'] = network
stats['station'] = station
stats['starttime'] = UTCDateTime(startTime)

statsZ = stats
statsZ['component'] = 'Z'
trZ = Trace(data=appended_df['Z'].values, header = statsZ)

statsX = stats
statsX['component'] = 'X'
trX = Trace(data=appended_df['X'].values, header = statsX)

statsY = stats
statsY['component'] = 'Y'
trY = Trace(data=appended_df['Y'].values, header = statsY)

st = Stream(traces=[trX, trY, trZ])

for method in ["weighted_average_slopes", "lanczos", "linear", "slinear", "cubic"]:
    interp_time_start = time.perf_counter()
    if method=="weighted_average_slopes":
        st.interpolate(sampling_rate=40, method= method) 
    elif method=="lanczos":
        st.interpolate(sampling_rate=40, method= method, a=40) 
    else:
        st.interpolate(sampling_rate=40, method= method) 

    st.write(os.path.join(mseeddata,f'{network}-{station}-{method}.mseed'), format='MSEED', byteorder=-1) 
    print(f"Interpolation using {method} finished in {time.perf_counter()-interp_time_start:.5f}s")

# Create figure and plot space
fig, ax = plt.subplots(4,1,figsize=(10, 6), sharex=True)

# Add x-axis and y-axis
ax[0].plot(appended_df['Datetime'],
        appended_df['Z'],
        color='blue', lw=0.5)
ax[0].set_ylabel("Z")

ax[1].plot(appended_df['Datetime'],
        appended_df['X'],
        color='green', lw=0.5)
ax[1].set_ylabel("X")

ax[2].plot(appended_df['Datetime'],
        appended_df['Y'],
        color='orange', lw=0.5)
ax[2].set_ylabel("Y")


ax[3].plot(appended_df.loc[1:,'Datetime'],
        appended_df.loc[1:,"timeDelta"],
        color='purple', lw=0.5)
ax[3].set_ylabel("Time diff\n(in sec)")


plt.xlabel("Time")
plt.savefig(os.path.join(figpath,f"plot_all_data_{network}-{station}.png"), bbox_inches='tight', dpi=300)
plt.close('all')

# ## Plot the stream
# stFig = st.plot(show=False,
#         size=(1500,600), number_of_ticks=6,
#         type='relative', tick_rotation=60, handle=True,
#         linewidth = 1)
# plt.savefig(os.path.join(f"{station}-XYZ-obspy.png"), dpi=300)
# plt.close('all')

