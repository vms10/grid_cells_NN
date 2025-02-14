# Grid cells neural network model
This repository contains to code to reproduce the grid cells model of [this paper](https://onlinelibrary.wiley.com/doi/10.1002/hipo.20520). Grid cells, found in the medial entorhinal cortex, exhibit an hexagonal firing pattern that enables spatial navigation and memory formation. While their structure is well-documented, the underlying principles governing their emergence remain debated. In (https://onlinelibrary.wiley.com/doi/10.1002/hipo.20520), the authors analyze self-organization in recurrent networks, highlighting how local connectivity and learning rules can naturally give rise to grid-like firing patterns. They argue that grid cells likely emerge from general principles of neural computation rather than being an explicitly pre-designed feature of the brain. The network architecture includes feedforward connections between place and grid cells, as well as recurrent connections among grid cells. See paper for more details.  

## Organization of the codes
The simulation of the grid cells firing pattern emergence can be found on **rat_1D.ipynb**. There is also a GPU-based implementation at **GPU_rat_1D.ipynb**. 


<p align="center">
  <img src="https://github.com/user-attachments/assets/ea311316-3177-47d2-ac02-3e240379af3b" alt="Descripción de la imagen">
  <br>
  <em> The grid cell hexagonal firing pattern is obtained at the end of the simulation.</em>
</p>

