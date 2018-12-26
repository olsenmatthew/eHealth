from app.modules.level_0.class_employment import *
from app.modules.level_0.class_system import *
from app.modules.level_1.class_user import *
from app.modules.level_1.class_centre import *
from app.modules.level_0.class_customers import *
system = System

# ---------------------------------------------------------
# Initialising Users from CSV Files
# ---------------------------------------------------------
# Initialising patients from csv file info
user1 = Patient(system.generate_user_id(), "Jack", "Smith", "jack@gmail.com", "0", "cs1531", "0")
user2 = Patient(system.generate_user_id(), "Tom", "Smith", "tom@gmail.com", "0", "cs1531", "0")
user3 = Patient(system.generate_user_id(), "Isaac", "Smith", "isaac@gmail.com", "0", "cs1531", "0")
user4 = Patient(system.generate_user_id(), "Hao", "Smith", "hao@gmail.com", "0", "cs1531", "0")

# Initialising providers from csv file info
user5 = Provider(system.generate_user_id(), "Toby", "Smith", "toby@gmail.com", "0", "cs1531", "0", "Pathologist")
user6 = Provider(system.generate_user_id(), "Gary", "Smith", "gary@gmail.com", "0", "cs1531", "0", "GP")
user7 = Provider(system.generate_user_id(), "Samuel", "Smith", "samuel@gmail.com", "0", "cs1531", "0", "GP")
user8 = Provider(system.generate_user_id(), "Sid", "Smith", "sid@gmail.com", "0", "cs1531", "0", "Pathologist")
user9 = Provider(system.generate_user_id(), "Micheal", "Smith", "micheal@gmail.com", "0", "cs1531", "0", "Physiotherapist")
user10 = Provider(system.generate_user_id(), "Anna", "Smith", "anna@gmail.com", "0", "cs1531", "0", "GP")
user11 = Provider(system.generate_user_id(), "Thomas", "Smith", "thomas@gmail.com", "0", "cs1531", "0", "Pharmacist")
user12 = Provider(system.generate_user_id(), "Ian", "Smith", "ian@gmail.com", "0", "cs1531", "0", "Physiotherapist")

# Placing users in dict
dict_users = {user1.userID:user1,user2.userID:user2,user3.userID:user3,user4.userID:user4,user5.userID:user5,user6.userID:user6,user7.userID:user7,\
user8.userID:user8,user9.userID:user9,user10.userID:user10,user11.userID:user11,user12.userID:user12}

# Saving user info to database file "users"
system.set_users(dict_users)

# ---------------------------------------------------------
# Initialising Centres from CSV Files
# ---------------------------------------------------------
# Initialising centres from csv file info
centre1 = Centre(system.generate_centre_id(), "1111", "Sydney Children Hospital", "Hospital", "93821111", "Randwick")
centre2 = Centre(system.generate_centre_id(), "1112", "UNSW Health Service", "Medical Centre", "93855425", "Kensington")
centre3 = Centre(system.generate_centre_id(), "1113", "Prince of Wales Hospital", "Hospital", "93821118", "Randwick")
centre4 = Centre(system.generate_centre_id(), "1114", "Royal Prince Alfred Hospital", "Hospital", "95156111", "Sydney")
centre5 = Centre(system.generate_centre_id(), "1115", "USYD Health Service", "Medical Centre", "93513484", "Darlington")
centre6 = Centre(system.generate_centre_id(), "1116", "UTS Health Service", "Medical Centre", "95141177", "Ultimo")

# Placing centres in dict
dict_centres = {centre1.centreID:centre1, centre2.centreID:centre2, centre3.centreID:centre3, centre4.centreID:centre4, \
centre5.centreID:centre5, centre6.centreID:centre6}

# Saving centre info into database file "centres"
system.set_centres(dict_centres)

# ---------------------------------------------------------
# Initialising Provider-Centre Relationships from CSV Files
# ---------------------------------------------------------
# Initialising relationships from csv file info
p_c1 = Employment(centre1, user5)
p_c2 = Employment(centre1, user6)
p_c3 = Employment(centre1, user10)
p_c4 = Employment(centre1, user12)
p_c5 = Employment(centre3, user7)
p_c6 = Employment(centre3, user10)
p_c7 = Employment(centre3, user11)
p_c8 = Employment(centre4, user8)
p_c9 = Employment(centre5, user9)
p_c10 = Employment(centre5, user6)
p_c11 = Employment(centre6, user5)
p_c12 = Employment(centre6, user10)

# Placing relationships into a list
list_employment = [p_c1, p_c2, p_c3, p_c4, p_c5, p_c6, p_c7, p_c8, p_c9, p_c10, p_c12]

# Saving the info to databse file "employment"
system.set_employment(list_employment)

# ---------------------------------------------------------
# Initialising Some Relationships
# ---------------------------------------------------------

rel1 = Customer("usr-999127", "usr-413230")
rel2 = Customer("usr-690352", "usr-413230")

list_cust = [rel1, rel2]
system.set_customers(list_cust)