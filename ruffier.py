"""
Module for calculating the results of Ruffier tests.

The sum of the three tries at pulse readings (before strain, right after strain, and after a short break)
should ideally not exceed 200 beats per minute.
We propose that children measure their pulse for 15 seconds and find the result in beats per minute by multiplying by 4:
   S = 4 * (P1 + P2 + P3)
The further the result deviates from the ideal 200 beats, the worse it is.
Traditionally, tables are given by values divided by 10.

Ruffier Index:
   IR = (S - 200) / 10

The index is evaluated corresponding to age according to the table:
Age Groups:        7-8         9-10        11-12        13-14        15+ (adolescents only)
---------------------------------------------------------------------------------------------
Perfect:          < 6.5        < 5         < 3.5        < 2          < 0.5
Good:        >= 6.5 < 12   >= 5 < 10.5  >= 3.5 < 9  >= 2 < 7.5   >= 0.5 < 6
Satisfactory: >= 12 < 17   >= 10.5 < 15.5 >= 9 < 14   >= 7.5 < 12.5 >= 6 < 11
Weak:        >= 17 < 21   >= 15.5 < 19.5 >= 14 < 18  >= 12.5 < 16.5 >= 11 < 15
Unsatisfactory: >= 21      >= 19.5      >= 18       >= 16.5       >= 15

Notes:
- “Unsatisfactory” is separated by 4 points from “Weak” for all ages.
- “Weak” is separated from “Satisfactory” by 5 points.
- “Good” is separated from “Satisfactory” by 5.5 points.

Function Overview:
1. `ruffier_result`: Produces the calculated Ruffier index and level “unsatisfactory” for the tested age.
2. Other helper functions to compute intermediate results.

Constants for Texts:
"""

# Constants for text output
txt_index = "Your Ruffier index: "
txt_workheart = "Heart efficiency: "
txt_nodata = "There is no data for that age."

txt_res = [
    "Low.\nGo see your doctor ASAP!",
    "Satisfactory.\nGo see your doctor!",
    "Average.\nIt might be worth additional tests at the doctor.",
    "Higher than average.",
    "High."
]

# Function Definitions

def ruffier_index(P1, P2, P3):
    """
    Calculate the Ruffier index based on three pulse readings.
    
    Parameters:
        P1 (int): Pulse before strain.
        P2 (int): Pulse immediately after strain.
        P3 (int): Pulse after a short rest.
    
    Returns:
        float: Calculated Ruffier index.
    """
    pass

def neud_level(age):
    """
    Determine the "unsatisfactory" threshold based on age.
    
    Parameters:
        age (int): Age of the individual.
    
    Returns:
        float: Unsatisfactory level for the given age.
    
    Notes:
        - For age 7, "unsatisfactory" is an index of 21.
        - Threshold decreases by 1.5 every 2 years until age 15.
    """
    pass

def ruffier_result(r_index, level):
    """
    Interpret the Ruffier index and determine the readiness level.
    
    Parameters:
        r_index (float): Calculated Ruffier index.
        level (float): Unsatisfactory threshold for the age group.
    
    Returns:
        int: Readiness level (0 to 4, higher is better).
    """
    pass

def test(P1, P2, P3, age):
    """
    Conduct the Ruffier test and provide the result as a text summary.
    
    Parameters:
        P1 (int): Pulse before strain.
        P2 (int): Pulse immediately after strain.
        P3 (int): Pulse after a short rest.
        age (int): Age of the individual.
    
    Returns:
        str: Text result summarizing the Ruffier index and heart efficiency level.
    """
    pass
