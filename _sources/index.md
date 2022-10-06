# Pacific Observatory

The Pacific Observatory is the World Bank analytical program to explore and develop new information sources to mitigate the impact of data gaps in official statistics for Papua New Guinea (PNG) and the Pacific Island Countries (PICs).

This repository hosts the team's efforts to investigate how alternative data sources can be used to generate economic and sector statistics through cost-effective methods. The goal is to assess whether new data sources can produce indicators that are timely, have higher frequency and granularity.

The content is structured by topic of investigation, each thematic folder contains code, notebooks, outputs, and technical notes.

## Research Topics

🔖 [**Night Time Lights Applications**](./ch1_intro.md)
> This note explores socio-economic applications with Night Time Lights data.  

>Are lights at night a good proxy for economic activity or extractives?  

> Can lights be used to aid poverty mapping, estimate access to electrification, or estimate damages/recovery from natural disasters?

🔖 **Market Prices Imputation**
> A machine learning imputation method to fill gaps in food prices from markets in Papua New Guinea.

This follows the estimation proposed by

Andree, Bo Pieter Johannes. 2021. Estimating Food Price Inflation from Partial Surveys. Policy Research Working Paper;No. 9886. World Bank, Washington, DC. © World Bank. https://openknowledge.worldbank.org/handle/10986/36778 License: CC BY 3.0 IGO.

URI: http://hdl.handle.net/10986/36778 

The machine learning imputation code is avilable here https://github.com/worldbank/Food-Price-Estimation 

The code relies on WFP price surveys that are not available for PNG. The code has been adapted to run on IFPRI surveys available here https://www.ifpri.org/project/fresh-food-price-analysis-papua-new-guinea

🔖 [**Aviation Statistics**](./TourUpdates)
> Estimating tourism flows through aviation data.

🔖 **Crop Mapping / Climate Indices**
> Monitor crop productivity and seasonality through vegetation indices.  
> Create new crop masks with limited training data and satellite imagery.  
> Sub-national database of climate indicators.

### Future work

🔖 **Automatic Identification System (AIS)**
> This section assess the feasibility of using AIS data to derive high-frequency and geospatially disaggregated indicators on trade and fishing intensity.

🔖 **Text Mining**


## Additional Resources

- [DIME Analytics Data Handbook](https://worldbank.github.io/dime-data-handbook/)
    > This book is intended to serve as an introduction to the primary tasks required in development research, from experimental design to data collection to data analysis to publication. It serves as a companion to the DIME Wiki and is produced by DIME Analytics.

- [GitHub Pages](https://guides.github.com/features/pages/)
    > GitHub Pages are public webpages hosted and easily published through GitHub.

- [Jupyter Book](https://jupyterbook.org/intro.html)
    > Jupyter Book is an open source project for building beautiful, publication-quality books and documents from computational material.

## License

Materials under this repository are open-source under an [MIT license](LICENSE). The community is invited to test, adapt, and re-purpose materials as needed.