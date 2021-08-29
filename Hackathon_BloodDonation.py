import Donor_class as Dc

# defining all the lists to be used in the program

# for simplification purposes branch names will be in the format branch_number
branch = [[], [], [], []]
branch_blood_type = [[], [], [], []]

# currently set to all blood groups within 10%
rare_blood_types_list = ['ab_positive', 'ab_negative', 'b_positive', 'b_negative', 'a_negative']

blood_types_dict = {'ab_positive': [],
                    'ab_negative': [],
                    'b_positive': [],
                    'b_negative': [],
                    'a_negative': [],
                    'a_positive': [],
                    'o_positive': [],
                    'o_negative': [],
                    }


def get_details():
    donor = Dc.Donor()
    name = input('Enter the name: ')
    Branch = input('Enter the branch name: ')
    age = int(input('Enter the age of the donor: '))
    gender = input('Enter the gender of the donor: ')
    blood_group = input('Enter the blood_group of the donor(type(a,b,ab,o)_sign(positive,negative)): ')
    donor.upload_details(name=name, branch=Branch, blood_group=blood_group, age=age, gender=gender)

    temp = Branch.split('_')
    i = int(temp[1])
    branch[i-1].append(donor)
    if blood_group not in branch_blood_type[i-1]:
        branch_blood_type[i-1].append(blood_group)

    if blood_group in blood_types_dict.keys():
        blood_types_dict[blood_group].append(donor)


def update_details():
    name = input('Enter the name: ')
    Branch = input('Enter the branch name: ')
    blood_group = input('Enter the blood_group of the donor(type(a,b,ab,o)_sign(positive,negative)): ')
    temp = Branch.split('_')
    i = int(temp[1])
    for person in branch[i-1]:
        donor_update = Dc.Donor
        donor_update = person
        if donor_update.get_name() == name and donor_update.get_blood_group() == blood_group:
            donor_update.update_utilisation_date()
            print("Donor details updated successfully..")
            return

    print("Error encountered....\nPlease ensure that correct details were entered")


def get_branch_details():
    branch_input = input('Enter the branch name: ')
    temp = branch_input.split('_')
    branch_index = int(temp[1]) - 1
    print(f'Branch Name: {branch_input}\nNumber of donors: {len(branch[branch_index])}\n'
          f'Types of blood available: {" ".join(branch_blood_type[branch_index])}\n')

    donor_branch = Dc.Donor()
    for person in branch[branch_index]:
        donor_branch = person
        donor_branch.disp_details()
        print("\n")


def get_rare_blood_details():
    rare_blood_donor = Dc.Donor()
    for blood in rare_blood_types_list:
        for person in blood_types_dict[blood]:
            rare_blood_donor = person
            rare_blood_donor.disp_details()


def request_blood():
    blood_donor = Dc.Donor()
    blood = input('Enter the type of blood to be requested: ')
    for person in blood_types_dict[blood]:
        blood_donor = person
        blood_donor.request_blood_bag()


# to get list of donors who donated blood on a particular date
def get_bleeding_date():
    date = input('Please enter the date in yyyy-mm-dd format: ')
    blood_donor = Dc.Donor()
    for br in branch:
        for person in br:
            blood_donor = person
            if str(blood_donor.get_bleedingdate()) == date:
                blood_donor.disp_details()
                print('\n')


# to get a list of donated blood which is set to expire on a particular date provide it is not utilised
def get_expiry_date():
    date = input('Please enter the date in yyyy-mm-dd format: ')
    blood_donor = Dc.Donor()
    for br in branch:
        for person in br:
            blood_donor = person
            if str(blood_donor.get_expirydate()) == date and blood_donor.utilisation_date is None:
                blood_donor.disp_details()
                print('\n')


get_details()
update_details()
get_branch_details()
# request_blood()
# get_bleeding_date()





