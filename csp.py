# ============================================================
# CONSTRAINT SATISFACTION PROBLEM
# ============================================================

from parking_data import (
    parking_slots,
    vehicle_requirements,
    size_rank
)


# ============================================================
# FIND VALID SLOTS
# ============================================================

def get_valid_slots(vehicle_type, is_ev):

    required_size = vehicle_requirements[vehicle_type]

    valid_slots = []

    for slot, details in parking_slots.items():

        # ----------------------------------------------------
        # CONSTRAINT 1:
        # Slot must be empty
        # ----------------------------------------------------

        if details["occupied"]:
            continue

        # ----------------------------------------------------
        # CONSTRAINT 2:
        # Slot must be large enough
        # ----------------------------------------------------

        if (
            size_rank[details["size"]]
            < size_rank[required_size]
        ):
            continue

        # ----------------------------------------------------
        # CONSTRAINT 3:
        # EV vehicle requires EV slot
        # ----------------------------------------------------

        if is_ev and not details["ev"]:
            continue

        valid_slots.append(slot)

    return valid_slots


# ============================================================
# CHOOSE BEST SLOT
# ============================================================

def choose_best_slot(
    valid_slots,
    vehicle_type,
    is_ev
):

    required_size = vehicle_requirements[vehicle_type]

    scores = {}

    for slot in valid_slots:

        details = parking_slots[slot]

        score = 0

        # ----------------------------------------------------
        # Prefer exact vehicle size
        # ----------------------------------------------------

        if details["size"] == required_size:
            score += 10

        # ----------------------------------------------------
        # Prefer EV slot for EV vehicle
        # ----------------------------------------------------

        if is_ev and details["ev"]:
            score += 5

        scores[slot] = score

    return max(
        scores,
        key=scores.get
    )


# ============================================================
# AUTOMATIC SLOT SELECTION
# ============================================================

def find_best_slot(
    vehicle_type,
    is_ev
):

    valid_slots = get_valid_slots(
        vehicle_type,
        is_ev
    )

    if not valid_slots:
        return None

    return choose_best_slot(
        valid_slots,
        vehicle_type,
        is_ev
    )