"""
-------------------------------------------------------
Breakfast Cereal Data Set
Source: American Statistical Association
Section on Statistical Computing
Bi-Annual Data Exposition: 1993 dataset
http://stat-computing.org/dataexpo/
-------------------------------------------------------
Author:  Nora Znotinas
__updated__ = "2018-11-22"
-------------------------------------------------------
"""
# A dictionary of cereal manufacturers:
MFRS = {'A': 'American Home Food Products', 'G': 'General Mills', 'K': 'Kelloggs',
        'N': 'Nabisco', 'P': 'Post', 'Q': 'Quaker Oats', 'R': 'Ralston Purina'}
# A dictionary of cereal types:
TYPE = {'C': 'Cold', 'H': 'Hot'}
# A dictionary of how cereal is shelved in grocery stores:
SHELF = {1: "low", 2: "middle", 3: "high"}

# Vitamins and minerals in cereal:
# 0: "none added",
# up to 25: "enriched, often to 25% FDA recommended",
# 100 or more: "100% of FDA recommended"}

# Names and meanings of the data columns:
COLUMNS = [  # Breakfast cereal variables:
    "name",  # cereal name
    "mfr",  # See MFRS
    "type",  # see TYPE
    "shelf",  # display shelf - see SHELF
    "vitamins",  # vitamins & minerals - see description
    "calories",  # calories (number)
    "protein",  # protein(g)
    "fat",  # fat (g)
    "sodium",  # sodium (mg)
    "fiber",  # dietary fiber (g)
    "carbs",  # complex carbohydrates (g)
    "sugar",  # data (g) - simple carbohydrates
    "potassium",  # potassium (mg)
    "serv size",  # weight (in ounces) of one serving (serving size)
    "cups"]  # cups per serving
