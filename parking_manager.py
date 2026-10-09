# parking_manager.py

from parking_data import parking_slots
from csp import find_best_slot


def get_statistics():
    """
    Return total, available and occupied slot counts.
    """

    total = len(parking_slots)

    occupied = sum(
        1 for details in parking_slots.values()
        if details["occupied"]
    )

    available = total - occupied

    return {
        "total": total,
        "available": available,
        "occupied": occupied
    }


def find_vehicle(vehicle_number):
    """
    Find a vehicle currently parked.
    """

    vehicle_number = vehicle_number.strip().upper()

    for slot, details in parking_slots.items():

        if (
            details["occupied"]
            and details["vehicle"].upper() == vehicle_number
        ):
            return slot

    return None


def park_vehicle(vehicle_number, vehicle_type, is_ev):
    """
    Automatically allocate the best parking slot.
    """

    vehicle_number = vehicle_number.strip().upper()

    # Check if vehicle is already parked
    if find_vehicle(vehicle_number) is not None:
        return {
            "success": False,
            "reason": "already_parked"
        }

    # Find the best slot using CSP
    selected_slot = find_best_slot(
        vehicle_type,
        is_ev
    )

    # If no suitable slot is found
    if selected_slot is None:

        stats = get_statistics()

        # All physical slots are occupied
        if stats["occupied"] == stats["total"]:
            return {
                "success": False,
                "reason": "parking_full"
            }

        # Slots exist, but none satisfy the constraints
        return {
            "success": False,
            "reason": "no_suitable_slot"
        }

    # Allocate the selected slot
    parking_slots[selected_slot]["occupied"] = True
    parking_slots[selected_slot]["vehicle"] = vehicle_number

    return {
        "success": True,
        "reason": "success",
        "slot": selected_slot
    }


def release_vehicle(vehicle_number):
    """
    Release a vehicle from its parking slot.
    """

    vehicle_number = vehicle_number.strip().upper()

    slot = find_vehicle(vehicle_number)

    # Vehicle not found
    if slot is None:
        return {
            "success": False,
            "reason": "vehicle_not_found"
        }

    # Clear the parking slot
    parking_slots[slot]["occupied"] = False
    parking_slots[slot]["vehicle"] = ""

    return {
        "success": True,
        "reason": "released",
        "slot": slot
    }