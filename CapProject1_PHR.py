menuList = [
    "1. View Vehicles",
    "2. Add New Vehicle",
    "3. Update Vehicle Information",
    "4. Delete Vehicle",
    "5. Rent a Vehicle",
    "6. Return a Vehicle",
    "7. Exit"
]

dataRental = [
    {
        "Vehicle ID": "001",
        "Type": "Car",
        "Brand": "Toyota Avanza",
        "License Plate": "B 1234 XYZ",
        "Rental Price Per Day": 350000,
        "Availability": True,
        "Last Service Date": "2025-07-15",
        "Odometer": 42500
    },
    {
        "Vehicle ID": "002",
        "Type": "Motorbike",
        "Brand": "Honda Vario",
        "License Plate": "B 5678 ABC",
        "Rental Price Per Day": 90000,
        "Availability": True,
        "Last Service Date": "2025-06-20",
        "Odometer": 12000
    },
    {
        "Vehicle ID": "003",
        "Type": "Car",
        "Brand": "Daihatsu Xenia",
        "License Plate": "B 4321 DEF",
        "Rental Price Per Day": 330000,
        "Availability": True,
        "Last Service Date": "2025-05-18",
        "Odometer": 50500
    },
    {
        "Vehicle ID": "004",
        "Type": "Bicycle",
        "Brand": "Polygon",
        "License Plate": "—",
        "Rental Price Per Day": 25000,
        "Availability": True,
        "Last Service Date": "2025-07-01",
        "Odometer": 800
    },
    {
        "Vehicle ID": "005",
        "Type": "Van",
        "Brand": "Suzuki APV",
        "License Plate": "B 9999 HIJ",
        "Rental Price Per Day": 450000,
        "Availability": True,
        "Last Service Date": "2025-04-30",
        "Odometer": 78000
    }
]

def find_index_by_id(vehicleid):
    for i in range(len(dataRental)):
        if dataRental[i]["Vehicle ID"] == vehicleid:
            return i
    return -1

# READ
def viewVehicles():
    print("\n========== VIEW VEHICLES ==========\n")
    print("1. Show All")
    print("2. Search by Vehicle ID")
    print("3. Show Only Available")
    print("4. Filter by Type")
    print("5. Back to Main Menu")

    choice = input("Choose (1-5): ")
    if choice == "1":
        if len(dataRental) == 0:
            print("No data.")
        else:
            print("\nList of Vehicles:")
            for i, v in enumerate(dataRental):
                print(f"{i+1}. {v['Vehicle ID']} | {v['Type']} | {v['Brand']} | {v['License Plate']} | Rp{v['Rental Price Per Day']}/day | {'Available' if v['Availability'] else 'Rented'} | LastSvc: {v['Last Service Date']} | Odo: {v['Odometer']}")
    elif choice == "2":
        vid = input("Enter Vehicle ID: ")
        idx = find_index_by_id(vid)
        if idx == -1:
            print("Vehicle not found.")
        else:
            v = dataRental[idx]
            print(f"Found: {v['Vehicle ID']} | {v['Type']} | {v['Brand']} | {v['License Plate']} | Rp{v['Rental Price Per Day']}/day | {'Available' if v['Availability'] else 'Rented'} | LastSvc: {v['Last Service Date']} | Odo: {v['Odometer']}")
    elif choice == "3":
        found = False
        for v in dataRental:
            if v["Availability"] == True:
                if found == False:
                    print("\nAvailable Vehicles:")
                found = True
                print(f"- {v['Vehicle ID']} | {v['Type']} | {v['Brand']} | Rp{v['Rental Price Per Day']}/day")
        if found == False:
            print("No available vehicles.")
    elif choice == "4":
        t = input("Type to filter (Car/Motorbike/Bicycle/Van/Bus): ")
        found = False
        for v in dataRental:
            if v["Type"].lower() == t.lower():
                if found == False:
                    print("\nFiltered Vehicles:")
                found = True
                print(f"- {v['Vehicle ID']} | {v['Type']} | {v['Brand']} | Rp{v['Rental Price Per Day']}/day | {'Available' if v['Availability'] else 'Rented'}")
        if found == False:
            print("No vehicles for that type.")
    elif choice == "5":
        return
    else:
        print("Invalid choice.")

# CREATE
def addVehicle():
    print("\n========== ADD NEW VEHICLE ==========\n")

    vid = input("Vehicle ID (unique): ").strip()
    if vid == "":
        print("Vehicle ID cannot be empty.")
        return
    
    # UNIQUE CHECK FOR ID
    if find_index_by_id(vid) != -1:
        print("Vehicle ID already exists.")
        return

    vtype = input("Type (Car/Motorbike/Bicycle/Van/Bus): ").strip()
    if vtype == "":
        print("Type cannot be empty.")
        return

    brand = input("Brand: ").strip()
    if brand == "":
        print("Brand cannot be empty.")
        return

    plate = input("License Plate (use '-' if none): ").strip()
    if plate == "":
        print("License Plate cannot be empty (use '-' if none).")
        return
    
    # CHECK FOR LICENSE PLATE
    if plate != "-":
        taken = False
        for v in dataRental:
            if v["License Plate"].lower() == plate.lower():
                taken = True
                break
        if taken:
            print("License Plate already exists.")
            return

    # PRICE > 0
    price_str = input("Rental Price Per Day (IDR, numbers only): ").strip()
    if price_str.isdigit() == False:
        print("Price must be a positive number.")
        return
    price = int(price_str)
    if price <= 0:
        print("Price must be greater than 0.")
        return

    avail_input = input("Available now? (Y/N): ").strip().upper()
    if avail_input == "Y":
        avail = True
    elif avail_input == "N":
        avail = False
    else:
        print("Please answer Y or N.")
        return

    lastsvc = input("Last Service Date (YYYY-MM-DD): ").strip()
    if lastsvc == "":
        print("Last Service Date cannot be empty.")
        return

    odo_str = input("Odometer (numbers only): ").strip()
    if odo_str.isdigit() == False:
        print("Odometer must be a non-negative number.")
        return
    odo = int(odo_str)

    print("\nPlease confirm the new vehicle:")
    print(f"- Vehicle ID        : {vid}")
    print(f"- Type             : {vtype}")
    print(f"- Brand            : {brand}")
    print(f"- License Plate    : {plate}")
    print(f"- Price Per Day (IDR)  : {price}")
    print(f"- Availability     : {'Available' if avail else 'Rented'}")
    print(f"- Last Service     : {lastsvc}")
    print(f"- Odometer         : {odo}")

    confirm = input("Save? (Y/N): ").strip().upper()
    if confirm != "Y":
        print("Canceled. Nothing saved.")
        return

    new_item = {
        "Vehicle ID": vid,
        "Type": vtype,
        "Brand": brand,
        "License Plate": plate,
        "Rental Price Per Day": price,
        "Availability": avail,
        "Last Service Date": lastsvc,
        "Odometer": odo
    }
    dataRental.append(new_item)
    print("New vehicle saved successfully.")

# UPDATE
def updateVehicle():
    print("\n========== UPDATE VEHICLE ==========\n")
    vid = input("Enter Vehicle ID to update: ").strip()
    idx = find_index_by_id(vid)
    if idx == -1:
        print("Vehicle not found.")
        return

    v = dataRental[idx]

    print("\nCurrent data:")
    print(f"- Vehicle ID        : {v['Vehicle ID']}")
    print(f"- Type             : {v['Type']}")
    print(f"- Brand            : {v['Brand']}")
    print(f"- License Plate    : {v['License Plate']}")
    print(f"- Price Per Day (IDR)  : {v['Rental Price Per Day']}")
    print(f"- Availability     : {'Available' if v['Availability'] else 'Rented'}")
    print(f"- Last Service     : {v['Last Service Date']}")
    print(f"- Odometer         : {v['Odometer']}")

    choice = ""
    while choice != "8":
        print("\nWhat do you want to edit?")
        print("1. Type")
        print("2. Brand")
        print("3. License Plate")
        print("4. Rental Price Per Day")
        print("5. Availability")
        print("6. Last Service Date")
        print("7. Odometer")
        print("8. Done (Back to Main Menu)")
        choice = input("Choose (1-8): ").strip()

        if choice == "1":
            new_val = input("New Type (Car/Motorbike/Bicycle/Van/Bus): ").strip()
            if new_val == "":
                print("Type cannot be empty.")
            else:
                v["Type"] = new_val
                print("Type updated.")
        elif choice == "2":
            new_val = input("New Brand: ").strip()
            if new_val == "":
                print("Brand cannot be empty.")
            else:
                v["Brand"] = new_val
                print("Brand updated.")
        elif choice == "3":
            new_plate = input("New License Plate (use '-' if none): ").strip()
            if new_plate == "":
                print("License Plate cannot be empty.")
            else:
                # only check uniqueness if not '-'
                if new_plate != v["License Plate"]:
                    if new_plate != "-":
                        taken = False
                        for item in dataRental:
                            if item["License Plate"].lower() == new_plate.lower():
                                taken = True
                                break
                        if taken:
                            print("License Plate already exists.")
                            continue
                v["License Plate"] = new_plate
                print("License Plate updated.")
        elif choice == "4":
            price_str = input("New Price Per Day (numbers only): ").strip()
            if price_str.isdigit() == False:
                print("Price must be a positive number.")
            else:
                price = int(price_str)
                if price <= 0:
                    print("Price must be greater than 0.")
                else:
                    v["Rental Price Per Day"] = price
                    print("Price updated.")
        elif choice == "5":
            ans = input("Availability (Y=Available / N=Rented): ").strip().upper()
            if ans == "Y":
                v["Availability"] = True
                print("Availability set to Available.")
            elif ans == "N":
                v["Availability"] = False
                print("Availability set to Rented.")
            else:
                print("Please answer Y or N.")
        elif choice == "6":
            new_date = input("New Last Service Date (YYYY-MM-DD): ").strip()
            if new_date == "":
                print("Date cannot be empty.")
            else:
                v["Last Service Date"] = new_date
                print("Last Service Date updated.")
        elif choice == "7":
            odo_str = input("New Odometer (numbers only): ").strip()
            if odo_str.isdigit() == False:
                print("Odometer must be a non-negative number.")
            else:
                odo = int(odo_str)
                if odo < 0:
                    print("Odometer cannot be negative.")
                else:
                    v["Odometer"] = odo
                    print("Odometer updated.")
        elif choice == "8":
            print("Finished updating.")
        else:
            print("Invalid choice.")

# DELETE
def deleteVehicle():
    print("\n========== DELETE VEHICLE ==========\n")
    vid = input("Enter Vehicle ID to delete: ").strip()
    idx = find_index_by_id(vid)
    if idx == -1:
        print("Vehicle not found.")
        return

    v = dataRental[idx]

    # CANNOT DELETE WHILE RENTED
    if v["Availability"] == False:
        print("Cannot delete. Vehicle is currently rented.")
        return

    print(f"- Vehicle ID        : {v['Vehicle ID']}")
    print(f"- Type             : {v['Type']}")
    print(f"- Brand            : {v['Brand']}")
    print(f"- License Plate    : {v['License Plate']}")
    print(f"- Price Per Day (IDR)  : {v['Rental Price Per Day']}")
    print(f"- Availability     : {'Available' if v['Availability'] else 'Rented'}")
    print(f"- Last Service     : {v['Last Service Date']}")
    print(f"- Odometer         : {v['Odometer']}")

    confirm = input("Are you sure you want to delete this vehicle? (Y/N): ").strip().upper()
    if confirm == "Y":
        del dataRental[idx]
        print("Vehicle deleted successfully.")
    else:
        print("Deletion canceled.")

# RENT
rentalHistory = []  # CREATE DICTONARY FOR RENT/RETURN

def rentVehicle():
    print("\n========== RENT A VEHICLE ==========\n")

    # SHOW VEHICEL AVAIL
    has_any = False
    for v in dataRental:
        if v["Availability"] == True:
            if has_any == False:
                print("Available Vehicles:")
            has_any = True
            print(f"- {v['Vehicle ID']} | {v['Type']} | {v['Brand']} | Rp{v['Rental Price Per Day']}/day")
    if has_any == False:
        print("No vehicles available right now.")
        return

    vid = input("\nEnter Vehicle ID to rent: ").strip()
    idx = find_index_by_id(vid)
    if idx == -1:
        print("Vehicle not found.")
        return

    v = dataRental[idx]
    if v["Availability"] == False:
        print("Sorry, that vehicle is already rented.")
        return

    customer = input("Customer Name: ").strip()
    if customer == "":
        print("Customer name cannot be empty.")
        return

    start_date = input("Start Date (YYYY-MM-DD): ").strip()
    if start_date == "":
        print("Start date cannot be empty.")
        return

    days_str = input("Number of rental days (numbers only): ").strip()
    if days_str.isdigit() == False:
        print("Days must be a positive number.")
        return
    days = int(days_str)
    if days <= 0:
        print("Days must be greater than 0.")
        return

    total = days * v["Rental Price Per Day"]

    print("\nRental Summary:")
    print(f"- Vehicle ID     : {v['Vehicle ID']} ({v['Type']} - {v['Brand']})")
    print(f"- Customer      : {customer}")
    print(f"- Start Date    : {start_date}")
    print(f"- Days          : {days}")
    print(f"- Price Per Day     : Rp{v['Rental Price Per Day']}")
    print(f"- TOTAL         : Rp{total}")

    confirm = input("Confirm rent? (Y/N): ").strip().upper()
    if confirm != "Y":
        print("Canceled. Nothing changed.")
        return

    # RENTED MARKING
    v["Availability"] = False

    # STORE RENTING HISTORY
    rent_record = {
        "Vehicle ID": v["Vehicle ID"],
        "Customer": customer,
        "Start Date": start_date,
        "Days": days,
        "Price Per Day": v["Rental Price Per Day"],
        "Total": total,
        "Returned": False,         
        "Return Date": ""           
    }
    rentalHistory.append(rent_record)

    print("Rental recorded. Vehicle status set to Rented.")

# RETURN
def returnVehicle():
    print("\n========== RETURN A VEHICLE ==========\n")

    # VEHICLE LIST
    any_rented = False
    for v in dataRental:
        if v["Availability"] == False:
            if any_rented == False:
                print("Currently Rented Vehicles:")
            any_rented = True
            print(f"- {v['Vehicle ID']} | {v['Type']} | {v['Brand']} | Rp{v['Rental Price Per Day']}/day")
    if any_rented == False:
        print("No vehicles are currently rented.")
        return

    vid = input("\nEnter Vehicle ID to return: ").strip()
    idx = find_index_by_id(vid)
    if idx == -1:
        print("Vehicle not found.")
        return

    v = dataRental[idx]
    if v["Availability"] == True:
        print("This vehicle is already available (not rented).")
        return

    # FIND ACTIVE RENTAL
    active_idx = -1
    for i in range(len(rentalHistory)):
        rec = rentalHistory[i]
        if rec["Vehicle ID"] == vid and rec["Returned"] == False:
            active_idx = i
            break
    if active_idx == -1:
        print("Active rental record not found.")
        return

    rec = rentalHistory[active_idx]

    print("\nActive Rental Record:")
    print(f"- Vehicle ID     : {rec['Vehicle ID']}")
    print(f"- Customer      : {rec['Customer']}")
    print(f"- Start Date    : {rec['Start Date']}")
    print(f"- Planned Days  : {rec['Days']}")
    print(f"- Price Per Day     : Rp{rec['Price Per Day']}")
    print(f"- Planned Total : Rp{rec['Total']}")

    return_date = input("\nReturn Date (YYYY-MM-DD): ").strip()
    if return_date == "":
        print("Return date cannot be empty.")
        return

    used_str = input("Actual Days Used (numbers only): ").strip()
    if used_str.isdigit() == False:
        print("Days must be a positive number.")
        return
    used_days = int(used_str)
    if used_days <= 0:
        print("Days must be greater than 0.")
        return

    final_total = used_days * v["Rental Price Per Day"]

    print("\nReturn Summary:")
    print(f"- Vehicle ID     : {v['Vehicle ID']} ({v['Type']} - {v['Brand']})")
    print(f"- Customer      : {rec['Customer']}")
    print(f"- Start Date    : {rec['Start Date']}")
    print(f"- Return Date   : {return_date}")
    print(f"- Days Used     : {used_days}")
    print(f"- Price Per Day     : Rp{v['Rental Price Per Day']}")
    print(f"- FINAL TOTAL   : Rp{final_total}")

    confirm = input("Confirm return? (Y/N): ").strip().upper()
    if confirm != "Y":
        print("Canceled. Nothing changed.")
        return

    # LET THE VEHICLE AVAIL AGAIN
    v["Availability"] = True

    # UPDATE HISTOR
    rec["Returned"] = True
    rec["Return Date"] = return_date
    rec["Actual Days"] = used_days
    rec["Final Total"] = final_total

    odo_ans = input("Update Odometer? (Y/N): ").strip().upper()
    if odo_ans == "Y":
        odo_str = input("New Odometer (numbers only): ").strip()
        if odo_str.isdigit():
            v["Odometer"] = int(odo_str)
            print("Odometer updated.")
        else:
            print("Skipped: Odometer must be a number.")

    svc_ans = input("Update Last Service Date? (Y/N): ").strip().upper()
    if svc_ans == "Y":
        new_date = input("Last Service Date (YYYY-MM-DD): ").strip()
        if new_date != "":
            v["Last Service Date"] = new_date
            print("Last Service Date updated.")
        else:
            print("Skipped: date cannot be empty.")

    print("Return processed. Vehicle is now Available.")

# LOOP
def mainMenu():
    userInput = ""
    while userInput != "7":
        print("\n========== TRANSPORTATION RENTAL MANAGEMENT SYSTEM ==========\n")
        for m in menuList:
            print(m)
        userInput = input("Choose (1-7): ")
        if userInput == "1":
            viewVehicles()
        elif userInput == "2":
            addVehicle()
        elif userInput == "3":
            updateVehicle()
        elif userInput == "4":
            deleteVehicle()
        elif userInput == "5":
            rentVehicle()
        elif userInput == "6":
            returnVehicle()
        elif userInput == "7":
            print("Goodbye!")
        else:
            print("Invalid menu.")

mainMenu()