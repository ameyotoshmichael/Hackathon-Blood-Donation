from datetime import date, timedelta


def calc_expiry_date(bleeding_date):
    expiry_date = bleeding_date + timedelta(days=14)
    return expiry_date


class Donor:
    def __init__(self):
        self.name = None
        self.age = None
        self.gender = None
        self.branch = None
        self.blood_group = None
        self.bleeding_date = None
        self.expiry_date = None
        self.utilisation_date = None
        self.donate_again = None

    def upload_details(self, name, branch, blood_group, age, gender):
        self.name = name
        self.branch = branch
        self.blood_group = blood_group
        self.age = age
        self.gender = gender
        self.bleeding_date = date.today()
        self.expiry_date = calc_expiry_date(self.bleeding_date)
        self.donate_again = False

    def update_utilisation_date(self):
        self.utilisation_date = date.today()

    def new_donation(self):
        self.bleeding_date = date.today()
        self.expiry_date = calc_expiry_date(self.bleeding_date)
        self.donate_again = False

    def check_status(self):
        if date.today() < self.bleeding_date + timedelta(days=56):
            print("No,the current user cannot donate blood")
        else:
            self.donate_again = True
            print("Yes, the user can donate blood")

    def get_blood_group(self):
        return self.blood_group

    def get_branch(self):
        return self.branch

    def get_name(self):
        return self.name

    def get_bleedingdate(self):
        return self.bleeding_date

    def get_expirydate(self):
        return self.expiry_date

    def disp_details(self):
        print(f'Name: {self.name}\nBlood group: {self.blood_group}\nAge: {self.age}\nGender: {self.gender}\n'
              f'Branch: {self.branch}\nDate of donation: {self.bleeding_date}\n'
              f'Date of utilisation: {self.utilisation_date}\nDate of expiry: {self.expiry_date}')

    def request_blood_bag(self):
        if self.utilisation_date is None:
            print('Status: Available')
            self.disp_details()
        else:
            if self.donate_again is True:
                print("Status: Not available but request can be made.")
            else:
                print("Status: Not available and the user cannot donate any blood at this moment.")







