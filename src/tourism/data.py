"""
The module provides loaders for Country-level visitor data, Covid data, and Google-
trends data, and model-required data. 

Last Modified:
    2024-02-01
"""

import os
import pandas as pd
import chardet
from .ts_utils import check_and_modify_date

__all__ = [
    "CountryDataLoader",
    "TrendsDataLoader",
    "CovidDataLoader",
    "AviationDataLoader",
    "SARIMAXData",
    "MultiTSData",
    "TRENDS_DATA_FOLDER",
    "COVID_DATA_PATH",
    "DEFAULT_AVIATION_DATA_PATH"
]

TRENDS_DATA_FOLDER = os.path.join(os.getcwd(), "data", "tourism", "trends")
COVID_DATA_PATH = os.path.join(
    os.getcwd(), "data", "tourism", "oceania_covid_stringency.csv")
DEFAULT_AVIATION_DATA_PATH = os.path.join(
    os.getcwd(), "data", "tourism", "aviation_data_201901-202310.csv")


class CountryDataLoader:

    def __init__(self, country: str):
        """
        Initialize CountryDataLoader object.

        Args:
          country (str): The country code.

        """
        self.country = country
        self.country_data_folder = os.path.join(
            os.getcwd(), "data", "tourism", str(country))

    def read_country_data(self) -> pd.DataFrame:
        """
        Read and preprocess country data.

        Returns:
          pd.DataFrame: Preprocessed country data.

        """
        country = (pd.read_csv(self.country_data_folder + "/intermediate/" +
                               str(self.country) + "_monthly_visitor.csv")
                   .drop("Unnamed: 0", axis=1))
        country.columns = [col.lower().replace(" ", "_")
                           for col in country.columns]
        country["date"] = pd.to_datetime(country["date"])
        country["date"] = [check_and_modify_date(
            date) for date in country["date"]]
        return country


class TrendsDataLoader:
    def __init__(self, country: str,
                 trends_data_folder: str = TRENDS_DATA_FOLDER):
        """
        Initialize the TrendsDataLoader object.

        Args:
          country (str): The country code.
          trends_data_folder (str): the folder stores Google Trends Data.
            Set Default to `TRENDS_DATA_FOLDER`. 

        """
        self.country = country
        self.trends_data_folder = trends_data_folder

    def read_trends_data(self):
        """
        Read and preprocess trends data.

        Returns:
          pd.DataFrame: Preprocessed trends data.

        """
        trends = (pd.read_csv(self.trends_data_folder + "/trends_" +
                              str(self.country) + ".csv")
                  .drop("Unnamed: 0", axis=1))
        trends["date"] = pd.to_datetime(trends["date"])
        return trends


class CovidDataLoader:
    def __init__(self, country, covid_idx_path: str = COVID_DATA_PATH):
        """
        Initialize the CovidDataLoader object.

        Args:
          country (str): The country code.
          covid_idx_path (str): the single file that stores the Covid
            Stringency Index for Pacific Islands. Defaults to 
            `COVID_DATA_PATH`. 

        """
        self.country = country
        if os.path.exists(covid_idx_path):
            self.covid_idx_path = covid_idx_path
        else:
            raise FileNotFoundError(f"Cannot find {covid_idx_path}.")

    def read_covid_data(self):
        covid_idx = pd.read_csv(self.covid_idx_path)
        if "Unnamed: 0" in covid_idx.columns:
            covid_idx = covid_idx.drop("Unnamed: 0", axis=1)
        covid_idx["date"] = pd.to_datetime(covid_idx["date"])
        covid_idx["covid"] = ((covid_idx.date >= "2020-03-11")
                              & (covid_idx.date <= "2023-05-11")).astype(int)
        return covid_idx


class AviationDataLoader:
    def __init__(self, 
                 country: str,
                 select_col,
                 aviation_path: str = DEFAULT_AVIATION_DATA_PATH
                 ):
        self.country = country
        self.select_col = select_col
        self.aviation_path = aviation_path

    @staticmethod
    def load_aviation_data(filepath: str):
        # Process the Aviation Data
        if ".csv" in filepath:
            with open(filepath, 'rb') as f:
                encoding = chardet.detect(f.read())['encoding']
            avi = pd.read_csv(filepath, encoding=encoding)
        elif ".xlsx" in filepath:
            avi = pd.read_excel(filepath)
        else:
            raise ValueError("Unsupported file format")
        return avi

    def process_aviation_data(self):
        avi = self.load_aviation_data(self.aviation_path)
        avi.columns = [col.lower().replace(" ", "_") for col in avi.columns]
        avi["date"] = pd.to_datetime(avi["date"])

        avi["country"] = avi["country"].str.lower().str.replace(" ", "_")
        avi_subset = (avi[(avi.country == self.country)]
                      .sort_values(by="date", ascending=True)
                      .reset_index(drop=True))

        date_min, date_max = avi.date.min(), avi.date.max()
        continuous_date_df = pd.DataFrame(pd.date_range(date_min, date_max, freq="D"),
                                          columns=["date"])
        avi_clean = continuous_date_df.merge(avi_subset,
                                             how="left", on="date")

        avi_monthly = avi_clean.set_index("date").groupby(
            pd.Grouper(freq="MS"))[self.select_col].sum()
        return avi_monthly


class SARIMAXData:
    """
    A class for preparing and managing time series data for SARIMAX. This class is 
    designed to handle the loading, processing, and merging of country-specific 
    economic, COVID Stringency Index, and Google Trends data.
    """
    def __init__(self,
                 country: str,
                 y_var: str,
                 exog_var: list,
                 trends_data_folder: str = TRENDS_DATA_FOLDER,
                 covid_idx_path: str = COVID_DATA_PATH):
        """
        Initialize SARIMAXData object.

        Args:
          country (str): The country code.
          y_var (str): The dependent variable.
          exog_var (List[str]): List of exogenous variables.
          transform_method (str): The transformation method.
          trends_data_folder (str, optional): Path to trends data folder. 
            Defaults to TRENDS_DATA_FOLDER.
          covid_idx_path (str, optional): Path to COVID data. Defaults to COVID_DATA_PATH.
        """
        self.country = country
        self.trends_data_folder = trends_data_folder
        self.covid_idx_path = covid_idx_path
        self.country_data_loader = CountryDataLoader(self.country)
        self.trends_data_loader = TrendsDataLoader(
            self.country, self.trends_data_folder)
        self.covid_data_loader = CovidDataLoader(
            self.country, self.covid_idx_path)
        self.y_var = y_var
        self.exog_var = exog_var
        self.data = None
        self.country_raw = None
        self.trends_raw = None
        self.covid_raw = None


    def read_and_merge(self):
        """
        Read and merge data from various sources.
        """
        self.country_raw = self.country_data_loader.read_country_data()
        self.trends_raw = self.trends_data_loader.read_trends_data()
        self.covid_raw = self.covid_data_loader.read_covid_data()

        data = self.country_raw.merge(
            self.covid_raw, how="left", on="date").fillna(0)
        data = data.merge(self.trends_raw.iloc[:, [0, -3, -2, -1]],
                          how="left", on="date")
        data.columns = [col.lower().replace(" ", "_") for col in data.columns]
        dropped_date_cols = [col for col in data.columns
                             if col.startswith("year") or col.startswith("month")]
        dropped_idx = data[data["date"].diff() >= "32 days"].index - 1
        data = (data.drop(dropped_date_cols, axis=1)
                    .drop(dropped_idx, axis=0)
                    .reset_index(drop=True)
                    .fillna(0))
        first_col = data.pop("date")
        data.insert(0, "date", first_col)
        self.data = data


class MultiTSData(SARIMAXData):

    def __init__(self, country: str,
                 y_var: str,
                 exog_var: list,
                 select_col: list = ["seats_arrivals_intl"],
                 trends_data_folder: str = TRENDS_DATA_FOLDER,
                 covid_idx_path: str = COVID_DATA_PATH,
                 aviation_path: str = DEFAULT_AVIATION_DATA_PATH):
        super().__init__(country, y_var, exog_var)
        self.aviation_path = aviation_path
        self.avi_data = None
        self.aviation_data_loader = AviationDataLoader(
            self.country, select_col, self.aviation_path)

    def read_and_merge(self):
        """
        Read and merge data inherited from SARIMAXData and aviation data.
        """
        # Inherit from the read_and_merge method from SARIMAXData
        super().read_and_merge()
        self.avi_data = self.aviation_data_loader.process_aviation_data()
        self.data = (self.data.merge(self.avi_data, how="outer", on="date")
                     .reset_index(drop=True))
