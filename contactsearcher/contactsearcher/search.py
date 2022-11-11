"""Search for an email address given a fragment of a job description."""

from typing import List

import csv

# note: see https://docs.python.org/3/library/csv.html 


def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    contacts_list = []
    for contact_line in csv.reader(contacts.splitlines(),quotechar='"',delimiter=",",
    quoting=csv.QUOTE_ALL,
    skipinitialspace=True,
    ):
        current_contact_job = contact_line[1]
        if job_description in current_contact_job.lower():
            contacts_list.append(contact_line)
    return contacts_list