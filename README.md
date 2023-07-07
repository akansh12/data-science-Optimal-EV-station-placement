[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
<!-- [![MIT License][license-shield]][license-url] -->
<!-- [![LinkedIn][linkedin-shield]][linkedin-url] -->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href=https://github.com/akansh12/data-science-Optimal-EV-station-placement">
    <img src="figures/saarland-log.png" alt="Logo" width="300" height="115">
  </a>

  <h3 align="center">Spatial-Economic Analysis for Optimal EV Charging Station Placement.</h3>

  <p align="center">
    Group 7, Data Science 2023
    <br />
    <a href="https://huggingface.co/spaces/Saira20/Optimal-EV-charging-stations">Dashboard</a>
    ·
    <a href="https://docs.google.com/presentation/d/1DvyXtf6PmHJlR4AY10__-B9UUPlWWLx9KHOHKlJr2W0/edit#slide=id.g20a8aeeec89_3_133">Presentation</a>
    ·
    <a href="https://youtu.be/kW-kBFeq9E0">Video</a>
    .
    <a href="https://github.com/akansh12/data-science-Optimal-EV-station-placement/blob/main/Report/Project_Report.pdf">Report</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#folder-structure">Folder structure</a></li>
    <li><a href="#data">Data and Usage</a></li>
    <li><a href="#dashboard">Dashboard</a></li>
    <li><a href="#team-memebers">Team Members</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#paper-and-citation">Paper and Citation</a></li>
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>


## About The Project
Spatial-Economic Analysis for Optimal EV Charging Station Placement using Machine Learning.
[![Optimal EV charging station placement][product-screenshot]](https://github.com/akansh12/data-science-Optimal-EV-station-placement)

The global transportation sector has been facing serious issues due to the use of internal combustion engines (ICEs), including their contribution to global warming. The exhaustion of fossil fuels and greenhouse gas emissions, particularly carbon dioxide, have raised concerns about climate change and global warming. To combat these problems, there is growing interest in transitioning from ICEs to cleaner and more sustainable alternatives, such as electric vehicles (EVs). EVs, running on electricity produced from renewable sources, offer the advantage of zero tailpipe emissions and can significantly reduce greenhouse gas emissions in the transportation industry. The transition to EVs has gained momentum, driven by declining battery prices and advancing charging methods. However, the widespread adoption of EVs requires an expansion of public charging infrastructure, necessitating the optimal placement of EV charging stations (EVCS).

In our work we focused on following task:
* Geographical and socio-economic variables can serve as indicators or proxies for understanding the demand for EV charging stations.
* The project aims to create an exhaustive dataset considering socio-demographic features of Germany and solve the problem of optimal EVCS placement using classical ML algorithms.
* The study evaluates different ML models and compares their performance to identify the most suitable approach.
* The findings contribute to the understanding of optimal EVCS placement and facilitate automated decision-making in expanding EV charging infrastructure.

## Folder structure
- All the code can be found under notebook/
- The final dataset can be found under data/processed/all_city_data_with_pop.csv
```
├── Dashboard
│   ├── app.py
│   ├── Data
│   ├── MyMap.html
│   ├── README.md
│   └── requirements.txt
├── data
│   └── processed
│       ├── all_city_data_with_pop.csv
│       ├── berlin_data_detailed.csv
│       ├── Frankfurt_data_detailed.csv
│       ├── Kaiserslautern_data_detailed.csv
│       ├── karlsruhe_data_detailed.csv
│       ├── Mainz_data_detailed.csv
│       └── Saarbrücken_data_detailed.csv
│   └── raw
├── figures
│   ├── XX.png
├── notebooks
│   ├── CITY_NAME.ipynb
│   ├── cache
│   ├── Data_Science_Mini_project_EDA.ipynb
│   ├── EDA.ipynb
│   ├── make_data_set.ipynb
│   ├── map_images
│   │   ├── xx.jpg
│   ├── modeling.ipynb
│   ├── plots.ipynb
└── README.md
```

## Data and Usage
<figure style="text-align:center">
  <img
  src="/figures/Data-collection.jpeg"
  alt="pipeline">
  <figcaption>Data Collection Pipeline</figcaption>
</figure>

### How replicate results
1. set path_root_dir in notebook/modeling.ipynb
2. results will be created under result directory

### How to create dataset from raw data

1. Download data from [here](https://drive.google.com/drive/folders/1j2lwYuwfH4WuZ8j0VPc17SbCqO11yYYJ?usp=sharing)
2. Set path_to_downlaoded_data in notebooks/make_data_set.ipynb
3. run the notebook and data will be created


## Dashboard
The dashboard is created with Streamlit in Python, which is an open-source framework designed to create interactive web apps. Our app is hosted on Hugging Face. The dashboard shows a map of Saarbrücken, Germany, with points-of-interest, existing EV charging stations, residential, and commercial areas marked on the map, along with the optimal location of new EV charging stations predicted by our model. The app gives the option to view different features marked on the map that were collected and used to train our model. Final results and EDA plots, for example, a pie chart of the number of different types of infrastructure in Saarbrücken, are also displayed on the dashboard to help visualize the data and evaluate overall model performance.
<figure style="text-align:center">
  <img
  src="/figures/dashboard.png"
  alt="pipeline">
  <figcaption>Data Collection Pipeline</figcaption>
</figure>

[Link to the app hosted on hugging-face](https://huggingface.co/spaces/Saira20/Optimal-EV-charging-stations)

Dashboard code can be found under: [Dashboard](https://github.com/akansh12/data-science-Optimal-EV-station-placement/tree/main/Dashboard)

## Roadmap

- [x] Collect and gather data for the task
- [x] Performed EDA [EDA_Notebook_1](https://github.com/akansh12/data-science-Optimal-EV-station-placement/blob/main/notebooks/Data_Science_Mini_project_EDA.ipynb) [EDA Notebook_2](https://github.com/akansh12/data-science-Optimal-EV-station-placement/blob/main/notebooks/EDA.ipynb)
- [x] Developed Machine Learning Model 
- [x] Deployment of final prototype to [Dashboard](https://huggingface.co/spaces/Saira20/Optimal-EV-charging-stations) for the end user. 

## Team Members
1. Bahram Khan Baloch (7047281) 
2. Saira Sohail Anwari (7047706)
3. Umer Butt (7024124)
4. Cicy Kuriakose Agnes (7047703)
5. Akansh Maurya (7047939)

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
We would like to thank Prof. Dr.-Ing. Wolfgang Maaß and tutors of Data Science course 2023 at Saarland University for giving us the opportunity to work in such a industry relevant project. We would also like to acknowledge the following repositories/organization for making this project successful. 
- OpenStreetmap: (https://www.openstreetmap.org)
- Germna Federal Network Agency: (https://www.bundesnetzagentur.de)
- Humanitarian Data Exchange: (https://data.humdata.org)
- Data for Good at Meta: 
- [Where Should We Be Placing EV Charging Stations? (Using QGIS and PulP)]()

<!-- Paper and Citation -->
## Paper and Citation
Please use the following citation for our data or methodology: 

<!-- Contact -->
## Contact
If dashboard is not working, please create an [new issue](https://github.com/akansh12/data-science-Optimal-EV-station-placement/issues) or email at: akanshmaurya@gmail.com





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/akansh12/data-science-Optimal-EV-station-placement
[contributors-url]: https://github.com/akansh12/data-science-Optimal-EV-station-placement/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/akansh12/data-science-Optimal-EV-station-placement
[forks-url]: https://github.com/akansh12/data-science-Optimal-EV-station-placement/forks

[stars-shield]: https://img.shields.io/github/stars/akansh12/data-science-Optimal-EV-station-placement
[stars-url]: https://github.com/akansh12/data-science-Optimal-EV-station-placement/stargazers

[issues-shield]: https://img.shields.io/github/issues/akansh12/data-science-Optimal-EV-station-placement
[issues-url]: https://github.com/akansh12/data-science-Optimal-EV-station-placement/issues

<!-- [license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew -->

[product-screenshot]: figures/overview.gif
[data-collect-pipeline]: figures/Data-collection.jpeg
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 





