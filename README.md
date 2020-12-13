# Digital Tools for Finance - Assignment

This is the assignment project of
- Patrick Storz  16-108-011
- Kevin Steijn   19-770-429
- Hubert Mrugala 19-764-265

for the course Digital Tools for Finance at UZH.

## What is the project about?

Flash Eurozone PMIs for September and their signal with respect to the business cycle.

* * *
### Contribution
- Patrick Storz: LaTeX report
- Kevin Steijn: LateX beamer
- Hubert Mrugala: Visualizations

* * *
### Collaboration Comments
- [Brainstorming miro](https://miro.com/app/board/o9J_khn4A3g=/)
- More about managing the project in Projects --> Assignment

### Some info about PMI
- Purchasing Managers Index (PMI) is a survey that measures firms' business activity.
- The surveys ask respondents (managers) to report the change in each variable (like output or employment) compared to the prior month, noting whether each has risen/improved, fallen/deteriorated or remained unchanged.
- Flash reading is an advanced estimate of the final PMI number based on ~85% of total responses. It's publised about a week earlier
- PMIs are calculated by using diffusion index: INDEX = %’higher’ * 1.0 + %’the same’ * 0.5 + %’lower’ * 0.0.
- If PMI is 50 then nothing changed with respect to the last month. More than 50 - increased business activity. Less than 50 - decreased activity.
- PMIs can be used to forecast GDP


# Structure of Project

    .
    ├── data                # Data used for our analysis
    ├── src                 # Code that performs analysis
	│   └── output              # Charts outputted from code
	├── temp                # Files of previous project
    │   └── reports             # Research from previous project   
    ├── text                # Documentation files
	│   ├── presentation        # Presentation of project
    │   └── report              # Report of project
    └── README.md
	
## Download and Usage

Simply Fork, Clone, or Download on GitHub

To run the code ensure that your environment has the needed libraries by using pip:

pip install -r requirements.txt

[requirements.txt](https://github.com/patrickrstorz/DTfF_group_project/blob/main/src/requirements.txt) is found in /src/

To modify the presentation or report you require a tex editor, we used [MikTex](https://miktex.org/)

## Dependencies

See [requirements](https://github.com/patrickrstorz/DTfF_group_project/blob/main/src/requirements.txt)

Noteworthy of the libraries required for the project are two libraries for data retrieval:

[World Bank Data](https://github.com/mwouts/world_bank_data) for retrieval of GDP indicators

[Pandas Datareader](https://github.com/pydata/pandas-datareader) for retrieval of Stock prices


## Bugs

Find a bug in the project? [Open a new issue on GitHub](https://github.com/patrickrstorz/DTfF_group_project/issues)