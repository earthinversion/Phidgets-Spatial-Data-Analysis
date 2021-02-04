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

<p align="center">
    <img width="80%" src="figs/RFI-phidgetData-weighted_average_slopes-ZXY.png">
    <p align="center" style="text-align: center; font-style: italic; font-size: smaller;">weighted_average_slopes</p>
</p>

<p align="center">
    <img width="80%" src="figs/RFI-phidgetData-lanczos-ZXY.png">
    <p align="center" style="text-align: center; font-style: italic; font-size: smaller;">lanczos</p>
</p>

<div class="gallery" style="margin: 5px;
  border: 1px solid #ccc;
  float: left;
  width: 180px;">
    <img src="figs/RFI-phidgetData-weighted_average_slopes-ZXY.png" alt="weighted_average_slopes" width="600" height="400" style="width: 100%;
  height: auto;">
  <div class="desc" style="padding: 15px;
  text-align: center;">weighted_average_slopes</div>
</div>

<div class="gallery" style="margin: 5px;
  border: 1px solid #ccc;
  float: left;
  width: 180px;">
    <img src="figs/RFI-phidgetData-lanczos-ZXY.png" alt="lanczos" width="600" height="400" style="width: 100%;
  height: auto;">
  <div class="desc" style="padding: 15px;
  text-align: center;">lanczos</div>
</div>