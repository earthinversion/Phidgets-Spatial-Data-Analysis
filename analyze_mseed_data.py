from obspy import read
import matplotlib.pyplot as plt
import os, glob


dataloc = "data/"
allDataFiles = glob.glob(dataloc+"*.csv")


dataname0 = os.path.splitext(os.path.basename(allDataFiles[0]))[0]

network = "RFI"
station = dataname0.split("_")[0]


###
for method in ["weighted_average_slopes", "lanczos", "linear", "slinear", "cubic"]:
    stream = read(f'{network}-{station}-{method}.mseed', format="MSEED")
    ## Plot the stream
    stream.plot(outfile=f"{network}-{station}-{method}-ZXY.png", linewidth=0.5, title = f"{method}")

    plt.close('all')