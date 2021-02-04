<h1>Analysis of the recordings from the Phidget Spatial Sensor</h1> 

<code>Utpal Kumar</code>


<h2><code>analyze_csv_data.py</code></h2> 
<p>Reads the sequential csc files in the directory csvdata and 
write it into mseed files using different interpolation algorithms; also plot the three component recording from the csv file</p>


<p align="center">
  <img width="80%" src="figs/plot_all_data_RFI-phidgetData.png">
</p>

<h2><code>analyze_mseed_data.py</code></h2> 
<p>Reads the mseed data interpolated using different algorithms and plot it</p>


<figure style="float: right; width: 30%; text-align: center; font-style: italic; font-size: smaller; text-indent: 0; border: thin silver solid; margin: 0.5em; padding: 0.5em;">
    <img src="figs/RFI-phidgetData-weighted_average_slopes-ZXY.png">
    <figcaption>weighted_average_slopes</figcaption>
</figure>

<figure style="float: right; width: 30%; text-align: center; font-style: italic; font-size: smaller; text-indent: 0; border: thin silver solid; margin: 0.5em; padding: 0.5em;">
    <img src="figs/RFI-phidgetData-lanczos-ZXY.png">
    <figcaption>lanczos</figcaption>
</figure>