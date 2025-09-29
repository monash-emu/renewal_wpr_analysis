import pandas as pd
from pathlib import Path

__base_path = Path(__file__).parent

# Function for loading target data
def load_target_data(country):
    target_data_path = __base_path / "data/target-data/case-data.csv"
    if country == 'Malaysia':
        target_data = pd.read_csv(target_data_path, index_col=0)['New_cases_MYS']
    elif country == 'Philippines':
        target_data = pd.read_csv(target_data_path, index_col=0)['New_case_PHL']
    else: target_data = pd.read_csv(target_data_path, index_col=0)['New_case_VNM']
    target_data.index = pd.to_datetime(target_data.index)
    return target_data

# Function for loading google mobility data
def load_mobility_data(country):
    mobility_data_path = __base_path / Path("data/mobility-data/mobility-data.csv")
    mobility_data = pd.read_csv(mobility_data_path, index_col=0)
    mobility_data = mobility_data[mobility_data["country_region"] == country]
    mobility_data.index = pd.to_datetime(mobility_data.index)
    return mobility_data

# function for loading variant prevalence data
def load_variant_prevalence_data(country):
    variant_data_path = __base_path / Path("data/variant-data/variant-prevalence.csv")
    variant_data = pd.read_csv(variant_data_path, index_col=0)
    variant_data = variant_data[variant_data["country"] == country]
    return variant_data

# function for loading vaccination data
def load_vaccination_data(country):
    vaccination_data_path = __base_path / Path("data/vaccination-data/vaccination-data.csv")
    vaccination_data = pd.read_csv(vaccination_data_path, index_col=0)
    vaccination_data = vaccination_data[vaccination_data["location"] == country]
    vaccination_data.index = pd.to_datetime(vaccination_data.index)
    return vaccination_data