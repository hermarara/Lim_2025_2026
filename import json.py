import json
from pathlib import Path

# ---------- Setup ----------
ROOT = Path(__file__).parent
DB_FILE = ROOT / "database.json"


# ---------- Core Utilities ----------
def fetch_data():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def commit_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------- Insert ----------
def create_info(key, value):
    db = fetch_data()
    db[key] = value
    commit_data(db)


def create_snack(name, category, price):
    db = fetch_data()

    snacks = db.get("snacks")
    if snacks is None:
        print("Snacks list not initialized.")
        return

    new_entry = {
        "snack_id": len(snacks) + 1,
        "name": name,
        "category": category,
        "price": price
    }

    snacks.append(new_entry)
    commit_data(db)


def create_student(name, grade_level):
    db = fetch_data()

    students = db.get("students")
    if students is None:
        print("Students list not initialized.")
        return

    new_entry = {
        "student_id": len(students) + 1,
        "name": name,
        "grade_level": grade_level
    }

    students.append(new_entry)
    commit_data(db)


def create_sale(student_id, snack_id, quantity, total_price, date, day):
    db = fetch_data()

    sales = db.get("sales")
    if sales is None:
        print("Sales list not initialized.")
        return

    new_entry = {
        "sale_id": len(sales) + 1,
        "student_id": student_id,
        "snack_id": snack_id,
        "quantity": quantity,
        "total_price": total_price,
        "date": date,
        "day": day
    }

    sales.append(new_entry)
    commit_data(db)


# ---------- Display ----------
def show_all():
    print(fetch_data())


def filter_chips():
    db = fetch_data()
    print("\n--- Chips ---")

    for snack in db.get("snacks", []):
        if snack.get("category") == "chips":
            print(snack)


def sales_from_grade10():
    db = fetch_data()
    print("\n--- Grade 10 Sales ---")

    grade10 = {s["student_id"] for s in db.get("students", []) if s["grade_level"] == 10}

    for sale in db.get("sales", []):
        if sale["student_id"] in grade10:
            print(sale)


def quantity_on_date():
    db = fetch_data()
    target = "2026-03-16"

    total = sum(
        sale["quantity"]
        for sale in db.get("sales", [])
        if sale["date"] == target
    )

    print(f"Total quantity sold today: {total}")


# ---------- Modify ----------
def set_snack_price(sid, new_price):
    db = fetch_data()

    for snack in db.get("snacks", []):
        if snack["snack_id"] == sid:
            snack["price"] = new_price

    commit_data(db)


def set_student_grade(sid, new_grade):
    db = fetch_data()

    for student in db.get("students", []):
        if student["student_id"] == sid:
            student["grade_level"] = new_grade

    commit_data(db)


def set_sale_quantity(sale_id, qty):
    db = fetch_data()

    for sale in db.get("sales", []):
        if sale["sale_id"] == sale_id:
            sale["quantity"] = qty

    commit_data(db)


# ---------- Remove ----------
def erase_snack(sid):
    db = fetch_data()
    db["snacks"] = [x for x in db.get("snacks", []) if x["snack_id"] != sid]
    commit_data(db)


def erase_student(sid):
    db = fetch_data()
    db["students"] = [x for x in db.get("students", []) if x["student_id"] != sid]
    commit_data(db)


def erase_sale(sale_id):
    db = fetch_data()
    db["sales"] = [x for x in db.get("sales", []) if x["sale_id"] != sale_id]
    commit_data(db)


# ---------- Insights ----------
def most_sold_snack():
    db = fetch_data()

    count_map = {}
    for sale in db.get("sales", []):
        sid = sale["snack_id"]
        count_map[sid] = count_map.get(sid, 0) + 1

    if not count_map:
        print("No sales data.")
        return

    top_id = max(count_map, key=count_map.get)

    name = next(
        (s["name"] for s in db.get("snacks", []) if s["snack_id"] == top_id),
        "Unknown"
    )

    print(f"Most Popular Snack: {name} ({count_map[top_id]} sales)")


def biggest_spender_grade():
    db = fetch_data()

    grade_map = {s["student_id"]: s["grade_level"] for s in db.get("students", [])}
    totals = {}

    for sale in db.get("sales", []):
        grade = grade_map.get(sale["student_id"])
        totals[grade] = totals.get(grade, 0) + sale["total_price"]

    if totals:
        best = max(totals, key=totals.get)
        print(f"Grade That Spends The Most: Grade {best} ({totals[best]} total)")


def peak_sales_day():
    db = fetch_data()

    counter = {}
    for sale in db.get("sales", []):
        d = sale["day"]
        counter[d] = counter.get(d, 0) + 1

    if counter:
        best = max(counter, key=counter.get)
        print(f"Day With Most Sales: {best} ({counter[best]} sales)")


def top_buyer():
    db = fetch_data()

    name_map = {s["student_id"]: s["name"] for s in db.get("students", [])}
    freq = {}

    for sale in db.get("sales", []):
        sid = sale["student_id"]
        freq[sid] = freq.get(sid, 0) + 1

    if freq:
        best = max(freq, key=freq.get)
        print(f"Top Buyer: {name_map.get(best, 'Unknown')} ({freq[best]} purchases)")


def average_sale_value():
    db = fetch_data()

    sales = db.get("sales", [])
    if sales:
        avg = sum(s["total_price"] for s in sales) / len(sales)
        print(f"Average Spending Per Sale: {avg:.2f}")


def sales_trend_report():
    db = fetch_data()
    sales = db.get("sales", [])

    if not sales:
        print("No sales data.")
        return

    totals, counts = {}, {}

    for s in sales:
        d = s["day"]
        totals[d] = totals.get(d, 0) + s["total_price"]
        counts[d] = counts.get(d, 0) + 1

    print("\n--- Sales Trends ---")

    for d in totals:
        avg = totals[d] / counts[d]
        print(f"{d}: Total Revenue = {totals[d]}, Average per Sale = {avg:.2f}")

    best_day = max(totals, key=lambda x: totals[x] / counts[x])
    print(f"\nDay with Highest Average Sale Value: {best_day}")

    days = list(totals.keys())
    if len(days) > 1:
        trend = "increasing" if totals[days[-1]] > totals[days[0]] else "decreasing"
        print(f"Overall Trend: Revenue is {trend} from {days[0]} to {days[-1]}.")


def run_all_reports():
    most_sold_snack()
    biggest_spender_grade()
    peak_sales_day()
    top_buyer()
    average_sale_value()
    sales_trend_report()


# ---------- Main ----------
def main():
    create_info("snacks", [])
    create_info("students", [])
    create_info("sales", [])

    create_snack("Piattos", "chips", 20)
    create_snack("Nova", "chips", 18)
    create_snack("Oreo", "cookies", 15)
    create_snack("KitKat", "chocolate", 25)
    create_snack("Skyflakes", "crackers", 12)

    create_student("Alice Cruz", 10)
    create_student("Brian Santos", 9)
    create_student("Carla Reyes", 10)
    create_student("David Lim", 11)
    create_student("Ella Tan", 10)

    create_sale(1, 1, 2, 40, "2026-03-14", "Saturday")
    create_sale(3, 3, 1, 15, "2026-03-14", "Saturday")
    create_sale(2, 2, 3, 54, "2025-03-15", "Sunday")
    create_sale(5, 4, 1, 25, "2026-03-15", "Sunday")
    create_sale(1, 1, 1, 20, "2026-03-16", "Monday")
    create_sale(4, 5, 2, 24, "2026-03-16", "Monday")

    filter_chips()
    sales_from_grade10()
    quantity_on_date()

    run_all_reports()

    set_snack_price(3, 17)
    set_student_grade(4, 10)
    set_sale_quantity(2, 2)

    erase_snack(2)
    erase_student(1)
    erase_sale(6)

    show_all()


main()