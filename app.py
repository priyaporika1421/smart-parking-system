from flask import Flask, render_template, request, redirect, url_for, flash
from parking_data import parking_slots
from parking_manager import get_statistics, park_vehicle, release_vehicle

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

@app.route("/", methods=["GET"])
def home():
    stats = get_statistics()
    return render_template("index.html", slots=parking_slots, stats=stats)

@app.route("/park", methods=["POST"])
def park():
    vehicle_number = request.form.get("vehicle_number", "").strip().upper()
    vehicle_type = request.form.get("vehicle_type", "Car")
    is_ev = request.form.get("is_ev") == "on"

    if not vehicle_number:
        flash("Please enter a vehicle number.", "error")
    elif vehicle_type not in ("Bike", "Car", "SUV"):
        flash("Please select a valid vehicle type.", "error")
    else:
        result = park_vehicle(vehicle_number, vehicle_type, is_ev)
        if result.get("success"):
            flash(f"Vehicle {vehicle_number} allotted slot {result['slot']}.", "success")
        else:
            messages = {
                "already_parked": f"Vehicle {vehicle_number} is already parked.",
                "parking_full": "Parking is full.",
                "no_suitable_slot": "No available slot matches this vehicle's requirements."
            }
            flash(messages.get(result.get("reason"), "Could not park vehicle."), "error")
    return redirect(url_for("home"))

@app.route("/release", methods=["POST"])
def release():
    vehicle_number = request.form.get("vehicle_number", "").strip().upper()
    if not vehicle_number:
        flash("Enter the vehicle number to release.", "error")
    else:
        result = release_vehicle(vehicle_number)
        if result.get("success"):
            flash(f"Vehicle {vehicle_number} released from slot {result['slot']}.", "success")
        else:
            flash(f"No parked vehicle found with number {vehicle_number}.", "error")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
