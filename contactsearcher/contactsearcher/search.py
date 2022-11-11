"""Search for an email address given a fragment of a job description."""

from typing import List

import csv # allows the program to use csv file

# note: see https://docs.python.org/3/library/csv.html 

def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    contacts_list = [] # empty container for jobs
    for contact_line in csv.reader(contacts.splitlines(),quotechar='"',delimiter=",",
    quoting=csv.QUOTE_ALL,
    skipinitialspace=True,
    ): # looks through csv file
    # splitlines() to divide data set
        current_contact_job = contact_line[1] # searchs for word inputted
        if job_description in current_contact_job.lower():
            contacts_list.append(contact_line) # add to list is world is in string
    return contacts_list