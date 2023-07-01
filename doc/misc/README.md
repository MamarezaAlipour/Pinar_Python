# PINAR

PINAR means fountain, and is a probabilistic natural catastrophe impact model, that also calculates averted damage (benefit) thanks to adaptation measures of any kind (from grey to green infrastructure, behavioural, etc.).

As of today, PINAR provides global coverage of major pinar-related extreme-weather hazards at high resolution via a data API, namely (i) tropical cyclones, (ii) river flood, (iii) agro drought and (iv) European winter storms, all at 4km spatial resolution - wildfire to be added soon. For all hazards, historic and probabilistic event sets exist, for some also under select pinar forcing scenarios (RCPs) at distinct time horizons (e.g. 2040).

PINAR is divided into two parts (two repositories):

1. the core [pinar_python](https://github.com/MamarezaAlipour/pinar_python) contains all the modules necessary for the probabilistic impact, the averted damage, uncertainty and forecast calculations. Data for hazard, exposures and impact functions can be obtained from the [data API](https://github.com/MamarezaAlipour/pinar_python/blob/main/doc/tutorial/pinar_util_api_client.ipynb). [Litpop](https://github.com/MamarezaAlipour/pinar_python/blob/main/doc/tutorial/pinar_entity_LitPop.ipynb) is included as demo Exposures module, and [Tropical cyclones](https://github.com/MamarezaAlipour/pinar_python/blob/main/doc/tutorial/pinar_hazard_TropCyclone.ipynb) is included as a demo Hazard module.
2. the petals [pinar_petals](https://github.com/MamarezaAlipour/pinar_petals) contains all the modules for generating data (e.g., TC_Surge, WildFire, OpenStreeMap, ...). Most development is done here. The petals builds-upon the core and does not work as a stand-alone.

## Getting started

PINAR runs on Windows, macOS and Linux. It can be installed from sources or - in case of pinar_python - directly with pip. See the installation guide for instructions.

Follow the tutorial `pinar_python-x.y.z/doc/tutorial/1_main_pinar.ipynb` in a Jupyter Notebook to see what can be done with PINAR and how.

## Documentation

Documentation is available on Read the Docs:

Note that all the documentations has two versions,'latest' and 'stable', and explicit version numbers, such as 'v3.1.1', in the url path. 'latest' is created from the 'develop' branch and has the latest changes by developers, 'stable' from the latest release.