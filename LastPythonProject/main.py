import tkinter as tk
from tkinter import simpledialog, messagebox


class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details


class SalesManager(Employee):
    def __init__(self, name, employee_id, basic_salary, age, date_of_birth, passport_details, managed_salespersons):
        super().__init__(name, employee_id, "Sales", "Manager", basic_salary, age, date_of_birth, passport_details)
        self.managed_salespersons = managed_salespersons


class SalesPerson(Employee):
    def __init__(self, name, employee_id, basic_salary, age, date_of_birth, passport_details, manager_id):
        super().__init__(name, employee_id, "Sales", "Salesperson", basic_salary, age, date_of_birth, passport_details)
        self.manager_id = manager_id


class MarketingManager(Employee):
    def __init__(self, name, employee_id, basic_salary, age, date_of_birth, passport_details, managed_marketers):
        super().__init__(name, employee_id, "Marketing", "Manager", basic_salary, age, date_of_birth, passport_details)
        self.managed_marketers = managed_marketers


class Marketer(Employee):
    def __init__(self, name, employee_id, basic_salary, age, date_of_birth, passport_details, manager_id):
        super().__init__(name, employee_id, "Marketing", "Marketer", basic_salary, age, date_of_birth, passport_details)
        self.manager_id = manager_id


class Event:
    def __init__(self, event_id, event_type, theme, date, time, duration, venue, client_id, guest_list, suppliers,
                 invoice):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue = venue
        self.client_id = client_id
        self.guest_list = guest_list
        self.suppliers = suppliers
        self.invoice = invoice


class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget


class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details


class Supplier:
    def __init__(self, supplier_id, name, address, contact_details, services, min_guests, max_guests):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.services = services
        self.min_guests = min_guests
        self.max_guests = max_guests


class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests


def add_employee():
    name = simpledialog.askstring("Add Employee", "Enter employee name:")
    employee_id = simpledialog.askinteger("Add Employee", "Enter employee ID:")
    department = simpledialog.askstring("Add Employee", "Enter department:")
    job_title = simpledialog.askstring("Add Employee", "Enter job title:")
    basic_salary = simpledialog.askfloat("Add Employee", "Enter basic salary:")
    age = simpledialog.askinteger("Add Employee", "Enter age:")
    date_of_birth = simpledialog.askstring("Add Employee", "Enter date of birth (YYYY-MM-DD):")
    passport_details = simpledialog.askstring("Add Employee", "Enter passport details:")

    # Creating Employee object
    employee = Employee(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)

    # Store the employee details
    messagebox.showinfo("Employee Added", "Employee details added successfully.")


def delete_employee():
    employee_id = simpledialog.askinteger("Delete Employee", "Enter employee ID to delete:")

    # Code to delete employee
    messagebox.showinfo("Employee Deleted", f"Employee with ID {employee_id} deleted successfully.")


def modify_employee():
    employee_id = simpledialog.askinteger("Modify Employee", "Enter employee ID to modify:")

    # Code to get employee details and display them for modification
    messagebox.showinfo("Employee Details", "Employee details displayed for modification.")


def display_employee():
    employee_id = simpledialog.askinteger("Display Employee", "Enter employee ID:")

    # Code to get and display employee details
    messagebox.showinfo("Employee Details", "Employee details displayed.")


def display_event():
    event_id = simpledialog.askinteger("Display Event", "Enter event ID:")

    # Code to get and display event details
    messagebox.showinfo("Event Details", "Event details displayed.")


def display_client():
    client_id = simpledialog.askinteger("Display Client", "Enter client ID:")

    # Code to get and display client details
    messagebox.showinfo("Client Details", "Client details displayed.")


def display_supplier():
    supplier_id = simpledialog.askinteger("Display Supplier", "Enter supplier ID:")

    # Code to get and display supplier details
    messagebox.showinfo("Supplier Details", "Supplier details displayed.")


def display_guest():
    guest_id = simpledialog.askinteger("Display Guest", "Enter guest ID:")

    # Code to get and display guest details
    messagebox.showinfo("Guest Details", "Guest details displayed.")


def display_venue():
    venue_id = simpledialog.askinteger("Display Venue", "Enter venue ID:")

    # Code to get and display venue details
    messagebox.showinfo("Venue Details", "Venue details displayed.")


def main():
    root = tk.Tk()
    root.title("Event Management System")

    # Create buttons for each functionality
    add_employee_button = tk.Button(root, text="Add Employee", command=add_employee)
    add_employee_button.pack()

    delete_employee_button = tk.Button(root, text="Delete Employee", command=delete_employee)
    delete_employee_button.pack()

    modify_employee_button = tk.Button(root, text="Modify Employee", command=modify_employee)
    modify_employee_button.pack()

    display_employee_button = tk.Button(root, text="Display Employee", command=display_employee)
    display_employee_button.pack()

    display_event_button = tk.Button(root, text="Display Event", command=display_event)
    display_event_button.pack()

    display_client_button = tk.Button(root, text="Display Client", command=display_client)
    display_client_button.pack()

    display_supplier_button = tk.Button(root, text="Display Supplier", command=display_supplier)
    display_supplier_button.pack()

    display_guest_button = tk.Button(root, text="Display Guest", command=display_guest)
    display_guest_button.pack()

    display_venue_button = tk.Button(root, text="Display Venue", command=display_venue)
    display_venue_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
