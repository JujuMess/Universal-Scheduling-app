# Universal-Scheduling-app

Universal Scheduling app to create a schedule for a team based on their skills and on each shift requirement

The app has three phases:

Pull data from the source file

Assign shifts

Design a new excel file to be filled

Export the data to another excel file


Future enhancements:

    GUI that will allow to fill all needs directly, no need for a source excel file
    Allow more than 5 shifts and skills

    Interactive live schedule that adapts to changes 


Product development plan:

Data pulling
Shift assignment first phase
Data exporting
Shift assignment second phase
Cleanup
GUI building (Flask)

changelog:

18-09-25: 
Folder structure created :


    py file for the scheduler
    py file for the GUI (will be the Flask part of the program)
    template folder with html template file
    static folder that includes-style folder with .css file for the html style
    
    Docker:
    dockerfile
    dockerignore file
    requirements file. gitignrore file to avoid the venv to be copied into github
    
18-09-2025:

/app and /test folders created

first test created to see if a DataFrame is created

19-09-2025:

    created .yml file so pytest can be used.
    created the first test for the load team function.

20-09-22025:
cleaned the source file and made it compatible with universal logic:
    each days can have it's shift requirements
    each shift has it's own requirements
    agents can be trained in 5 different skills
    agents can be not doing some shifts
    added supervisor for each agent for sorting in final output
    removed useless tabs
    made columns reference each other fir shifts and skills  so renaming them will change all tabs  ⚠️ check if this is compatible with data manipulation on pandas Warning : will it pull the formulas or the values? potential function to save as values

renamed folders and created a conftest file to ensure pytest runs in the correct app/ folder