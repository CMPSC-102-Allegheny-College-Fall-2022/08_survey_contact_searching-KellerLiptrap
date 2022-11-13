# Contact Searching

## Keller Liptrap

## Program Output

### What is the output from running the following commands?

```python
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "engineer":

['joe70@yahoo.com', 'Network engineer']
['torresjames@white.info', 'Electrical engineer']
['grahamjoel@castillo-gilbert.net', 'Engineer, technical sales']
['gsutton@miller.com', 'Engineer, maintenance']
['gharris@villarreal-snow.com', 'Water engineer']
['williamsondavid@lopez.com', 'Automotive engineer']
['ronald83@yahoo.com', 'Maintenance engineer']
['zmarshall@yahoo.com', 'Control and instrumentation engineer']
['christopher35@yahoo.com', 'Civil engineer, consulting']
['jacquelinedavid@hotmail.com', 'Engineer, electronics']
['espinozadaryl@hill-maddox.com', 'Engineering geologist']
['edwardsjacob@gmail.com', 'Chemical engineer']

Wow, we found some contacts! Email them to learn about your job!
```

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

```python
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "neer":

['joe70@yahoo.com', 'Network engineer']
['torresjames@white.info', 'Electrical engineer']
['grahamjoel@castillo-gilbert.net', 'Engineer, technical sales']
['gsutton@miller.com', 'Engineer, maintenance']
['gharris@villarreal-snow.com', 'Water engineer']
['williamsondavid@lopez.com', 'Automotive engineer']
['ronald83@yahoo.com', 'Maintenance engineer']
['zmarshall@yahoo.com', 'Control and instrumentation engineer']
['christopher35@yahoo.com', 'Civil engineer, consulting']
['jacquelinedavid@hotmail.com', 'Engineer, electronics']
['espinozadaryl@hill-maddox.com', 'Engineering geologist']
['edwardsjacob@gmail.com', 'Chemical engineer']

Wow, we found some contacts! Email them to learn about your job!
```

- `poetry run contactsearcher --job-description "neer" --contacts-file input/contacts.txt`

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### The source code statement that makes the `search` module available to `main`

```python
from contactsearcher import search
```

This source looks in the file of contactsearcher which contains the .py file fir the program to run. From the contactsearcher file it imports the search.py file. This allows us to use the function search for email given job function with the inputs of job description and contacts text.

#### The source code statement that extracts the current job description for a contact

```python
if job_description in current_contact_job.lower():
            contacts_list.append(contact_line) 
    return contacts_list
```

This if statement takes the inputed job description and looks for the string in the file of jobs. If the inputted string is found within the lines of the text file it will be added to the list that was defined earlier in the function.

#### Invocation of the function called `search_for_email_given_job`

```python
def contactsearcher(
    job_description: str = typer.Option(..., prompt=True),
    contacts_file: Optional[Path] = typer.Option(None),
) -> None:

search.search_for_email_given_job(job_description,contacts_text)
```

The commad line interface takes in an input of the job description and the file in which we want to iterate through as a csv file. When the search for email given job is called it takes the input of the string given by the user as well as the file that is iterated through to find the given string to add to the list and print.

#### Test case for the function called `search_for_email_given_job`

```python
def test_find_multiple_matching_result():
    """Check to ensure that search for contacts works for multiple matches."""
    contacts_database = """kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer"""
    contacts_list = search.search_for_email_given_job("engineer", contacts_database)
    assert len(contacts_list) == 2
```

This test for the function search for email given job is to find multiple matching results from the imputed word. First this test sets up contacts database as a variable with multiple emails and job descriptions. Then the search for email given job function is called with the input of “engineer” and the list of the previous variable of contacts database. This is all set to a new variable of contacts list. Finally, assert is used for the length of contacts list and checks if there’s only two objects within that list. 


#### Execute trace of the `contactsearcher` program

The input given below is designating the contact searcher to run with the job description being entered as a string of engineer and the contacts file of the input contacts.txt file. This is the file that will be integrated through to find a matching string that was inputted. First in the main file it determines whether the contacts file is there or not in this case it will be. And an if statement the Contacts file is iterated through with the read text command and split using the split lines command to determine the number of lines within the file. If the Contacts file does exist it will print out the results from using the search for email given job with the input of job description and the contacts text. For the input of the function it needs to be the contacts taxed because that is the new variable after the file is read through rather than the Contacts file that was inputted. This will display any string that was found in the text that is the same as the user and put it as a string for the job description. 


- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

## Professional Assessment

### So far this semester, what is one area in which you have struggled? How did you overcome this challenge?

One area that I have struggled in this semester was opening and reading files. In this Survey the documentation that was provided was very helpful in learning to read an open as a CSV file. Also other labs that have used opening and reading through files have helped me overcome some of these challenges. 


### Based on your experiences with this project, what is one way in which you want to improve?

One area I would want to improve on is getting a better knowledge of CSV files. This is my first time coding with CSV files. I believe they are important and I need to learn more about them and how to use them properly. 
