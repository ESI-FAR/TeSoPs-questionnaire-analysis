#!/usr/bin/env python3

import pandas as pd
import numpy as np
import random

OUTPUT_FILENAME_TIMESTEP_1 = "dataset_T1.csv"
OUTPUT_FILENAME_TIMESTEP_2 = "dataset_T2.csv"

NUMBER_OF_PARTICIPANTS = 100

NUMBER_OF_PERSONAL_VALUES = 22
NUMBER_OF_PREFERRED_TEMPERATURE_SETTINGS = 5
NUMBER_OF_HEATING_MOTIVATIONS = 4

PERSONAL_VALUES_RANGE = range(1, 7)  # [1, 2, 3, 4, 5, 6]

PREFERRED_TEMPERATURE_RANGE = range(10, 31)  # [10, 11, ..., 30]

CURTAILMENT_RANGE = range(11)  # [0, 1, ..., 10]
CURTAILMENT_EXTRA_VALUES = [88, 99]  # 88: not possible, 99: don't know

HEATING_MOTIVATION_RANGE = range(11)  # [0, 1, ..., 10]
HEATING_MOTIVATION_EXTRA_VALUES = [99]  # 99: don't know

ENERGY_POVERTY_RANGE = range(11)  # [0, 1, ..., 10]
ENERGY_POVERTY_EXTRA_VALUES = [99]  # 99: don't know

POLICY_SUPPORT_RANGE = range(11)  # [0, 1, ..., 10]
POLICY_SUPPORT_EXTRA_VALUES = [99]  # 99: don't know

AGE_RANGE = range(18, 101)  # [18, 19, ..., 100]

GENDER_RANGE = range(1, 4)  # [1, 2, 3] 1: male, 2: female, 3: self-describe
GENDER_EXTRA_VALUES = [88]  # 88: prefer not to say

# 1: Less than €1.000
# 2: €1.001 - €1.500
# 3: €1.501 - €2.000
# 4: €2.001 - €2.500
# 5: €2.501 - €3.000
# 6: €3.001 - €3.500
# 7: €3.501 - €4.000
# 8: €4.001 - €4.500
# 9: €4.501 - €5.000
# 10: More than €5.000
INCOME_RANGE = range(1, 11)  # [1, 2, ..., 10]
INCOME_EXTRA_VALUES = [88, 99]  # 88: prefer not to say, 99: don't know

index = [f"participant_{x}" for x in range(NUMBER_OF_PARTICIPANTS)]


def get_random_number(value_range, extra_values=[]):
    possible_values = list(value_range) + extra_values
    return random.choice(possible_values)


# Timestep 1
personal_values = [f"pv{x+1}" for x in range(NUMBER_OF_PERSONAL_VALUES)]
pref_temp = [
    f"temp_pref_{x+1}" for x in range(NUMBER_OF_PREFERRED_TEMPERATURE_SETTINGS)
]
curtailments = ["empty", "clothes", "night", "away", "shut", "shw_time"]
heating_motivations = [f"heat_mot_{x+1}" for x in range(NUMBER_OF_HEATING_MOTIVATIONS)]
energy_poverty = ["bill_diff"]
policy_support = ["nl_con_sup", "nl_cap_sup"]
age = ["age"]
gender = ["gender"]
income = ["income"]


rows = []
for _ in range(NUMBER_OF_PARTICIPANTS):
    row = []

    for personal_value in personal_values:
        row.append(get_random_number(PERSONAL_VALUES_RANGE))

    for preferred_temperature in pref_temp:
        row.append(get_random_number(PREFERRED_TEMPERATURE_RANGE))

    for curtailment in curtailments:
        row.append(get_random_number(CURTAILMENT_RANGE, CURTAILMENT_EXTRA_VALUES))

    for heating_motivation in heating_motivations:
        row.append(
            get_random_number(HEATING_MOTIVATION_RANGE, HEATING_MOTIVATION_EXTRA_VALUES)
        )

    row.append(get_random_number(ENERGY_POVERTY_RANGE, ENERGY_POVERTY_EXTRA_VALUES))

    row.append(get_random_number(POLICY_SUPPORT_RANGE, POLICY_SUPPORT_EXTRA_VALUES))
    row.append(get_random_number(POLICY_SUPPORT_RANGE, POLICY_SUPPORT_EXTRA_VALUES))

    row.append(get_random_number(AGE_RANGE))

    row.append(get_random_number(GENDER_RANGE, GENDER_EXTRA_VALUES))

    row.append(get_random_number(INCOME_RANGE, INCOME_EXTRA_VALUES))

    rows.append(row)

columns = (
    personal_values
    + pref_temp
    + curtailments
    + heating_motivations
    + energy_poverty
    + policy_support
    + age
    + gender
    + income
)

df = pd.DataFrame(rows, index=index, columns=columns)

df.to_csv(OUTPUT_FILENAME_TIMESTEP_1)

# Timestep 2
pref_temp_t2 = [
    f"temp_pref_{x+1}_t2" for x in range(NUMBER_OF_PREFERRED_TEMPERATURE_SETTINGS)
]
curtailments_t2 = [
    "empty_t2",
    "clothes_t2",
    "night_t2",
    "away_t2",
    "shut_t2",
    "shw_time_t2",
]
heating_motivations_t2 = [
    f"heat_mot_{x+1}_t2" for x in range(NUMBER_OF_HEATING_MOTIVATIONS)
]
energy_poverty_t2 = ["bill_diff_t2"]
policy_support_t2 = ["nl_con_sup_t2", "nl_cap_sup_t2"]


rows_t2 = []
for _ in range(NUMBER_OF_PARTICIPANTS):
    row = []

    for preferred_temperature in pref_temp:
        row.append(get_random_number(PREFERRED_TEMPERATURE_RANGE))

    for curtailment in curtailments:
        row.append(get_random_number(CURTAILMENT_RANGE, CURTAILMENT_EXTRA_VALUES))

    for heating_motivation in heating_motivations:
        row.append(
            get_random_number(HEATING_MOTIVATION_RANGE, HEATING_MOTIVATION_EXTRA_VALUES)
        )

    row.append(get_random_number(ENERGY_POVERTY_RANGE, ENERGY_POVERTY_EXTRA_VALUES))

    row.append(get_random_number(POLICY_SUPPORT_RANGE, POLICY_SUPPORT_EXTRA_VALUES))
    row.append(get_random_number(POLICY_SUPPORT_RANGE, POLICY_SUPPORT_EXTRA_VALUES))

    rows_t2.append(row)

columns_t2 = (
    pref_temp_t2 + curtailments_t2 + heating_motivations_t2 + energy_poverty_t2 + policy_support_t2
)

df_t2 = pd.DataFrame(rows_t2, index=index, columns=columns_t2)

df_t2.to_csv(OUTPUT_FILENAME_TIMESTEP_2)
