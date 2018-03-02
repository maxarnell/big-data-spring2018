



for i in range(0, 168, 24):
    #print(i)
    #i-5 as index
    #ranges are exclusive on the right side, not inclusive
    j = range(0,168,1)[i-5]
    if (j > i):
        df['hour'].replace(range(i, i + 19, 1), range(5, 24, 1), inplace = True)
        df['hour'].replace(range(i,i+5,1),range(163,167,1), inplace=True)
    else:
        df['hour'].replace(range((j, i+19, 1), range(0, 24, 1), inplace = True))

        # a range from x to y will be a list of values running from x to y-1

df.head()


print(i,j)
    #if (j > i):
    #    df.drop(df[

    #    ])

#replace allows you to replace a value or set of values with a corresponding replacement.
#.replace(val1, val2, inplace)

'''
#Catherine  Ignazio - Feminist Data Visualization
    Missing body Problem - bodies extracted
    profound inequity and asymmetry in datasets
    science surveillance selling
    states corporations universities
    "data shepherds"

Missing body problem #2 : Bodies absent
    inclusion issues in data science & visualizations

Missing Body Problem #3 : Bodies uncounted
    when quanitification is representation
    systematically ignoring hate crimes to focus on prostate functions
    "cell phone ownership in africa" aggregation can erase critical nuance -

Missing Body Probelm #4 : Bodies invisible
    rhetorical power of data visualization
    "the god trick" Donna Haraway

Knowledge is partial
knowledge is situated
knowledge is historical

Feminist data visualization is the visual presentation of systematically collected information that intentionally and explicitly addresses questions of power, inequality, representation, and ethics.

2. examine power and aspire to empowerment
    Male Presidents/Female Presidents pie Chart
Data Basic.io
Data Mural

4. Consider Context
    How was this collected, who collected it, why?
    Sexual assault on college campuses


5. Legitmize affect and embodiment
    Edward Tufte - Data modernist, all ink should be used to convey goal
    "data visceralization" - kelly dobson
