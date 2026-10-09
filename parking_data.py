# ============================================================
# PARKING DATA
# ============================================================

parking_slots = {

    "A1": {
        "size": "Small",
        "ev": False,
        "occupied": False,
        "vehicle": ""
    },

    "A2": {
        "size": "Small",
        "ev": True,
        "occupied": False,
        "vehicle": ""
    },

    "A3": {
        "size": "Medium",
        "ev": False,
        "occupied": True,
        "vehicle": "TS09AA1111"
    },

    "A4": {
        "size": "Medium",
        "ev": True,
        "occupied": False,
        "vehicle": ""
    },

    "B1": {
        "size": "Small",
        "ev": False,
        "occupied": False,
        "vehicle": ""
    },

    "B2": {
        "size": "Medium",
        "ev": False,
        "occupied": False,
        "vehicle": ""
    },

    "B3": {
        "size": "Large",
        "ev": True,
        "occupied": False,
        "vehicle": ""
    },

    "B4": {
        "size": "Large",
        "ev": False,
        "occupied": True,
        "vehicle": "TS09BB2222"
    },

    "C1": {
        "size": "Small",
        "ev": True,
        "occupied": False,
        "vehicle": ""
    },

    "C2": {
        "size": "Medium",
        "ev": False,
        "occupied": False,
        "vehicle": ""
    },

    "C3": {
        "size": "Medium",
        "ev": True,
        "occupied": False,
        "vehicle": ""
    },

    "C4": {
        "size": "Large",
        "ev": False,
        "occupied": False,
        "vehicle": ""
    },

    "D1": {
        "size": "Small",
        "ev": False,
        "occupied": False,
        "vehicle": ""
    },

    "D2": {
        "size": "Medium",
        "ev": True,
        "occupied": False,
        "vehicle": ""
    },

    "D3": {
        "size": "Large",
        "ev": True,
        "occupied": False,
        "vehicle": ""
    },

    "D4": {
        "size": "Large",
        "ev": False,
        "occupied": False,
        "vehicle": ""
    }
}


# ============================================================
# VEHICLE REQUIREMENTS
# ============================================================

vehicle_requirements = {
    "Bike": "Small",
    "Car": "Medium",
    "SUV": "Large"
}


# ============================================================
# SIZE RANKING
# ============================================================

size_rank = {
    "Small": 1,
    "Medium": 2,
    "Large": 3
}