class Phonebook(object):
    def __init__(self, entries):
        self.entries = entries

    def add_entry(self, entry):
        ######################
        ### YOUR CODE HERE ###
        ######################
        self.entries[entry.get_full_name()] = entry.phone_number



    def check_if_entry_exists(self, entry):
        ######################
        ### YOUR CODE HERE ###
        ######################
        if entry.get_full_name() in self.entries:
            return True
        else:
            return False





    def __str__(self):
       # self.entries[]


        return str(self.entries)


class Entry(object):

    def __init__(self, first_name, last_name, address, phone_number="555-555-5555"):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number

    def get_full_name(self):
        return self.first_name + " " + self.last_name


#################
### Main Code ###
#################
def main():

    # Create some entries
    hermione = Entry(first_name="Hermione", last_name="Granger", address="London")
    finn = Entry(first_name="Finn", last_name="Mertens", address="Treehouse")
    entries = {hermione.get_full_name():hermione, finn.get_full_name():finn}

    # Create the phonebook
    the_phonebook = Phonebook(entries)

    print "Before", the_phonebook

    new_entry = Entry(first_name="Wall", last_name="-E", address="Earth?", phone_number="1")
    print "Should say False:", the_phonebook.check_if_entry_exists(new_entry)
    the_phonebook.add_entry(new_entry)

    print "After", the_phonebook

if __name__ == "__main__":
    main()