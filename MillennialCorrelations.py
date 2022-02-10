import numpy as np
#import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt

DATA_SHEET = "MillennialResponses-02-10.csv"

print('==========READ IN DATA==========')
# read in the data
data_train = np.loadtxt (DATA_SHEET, delimiter=',')
print('done.\n')


print('==========SECTION 1: DEMOGRAPHICS==========')
exposedToHikeYoung = [0,0,0]    # represents [min, mean, max]
exposedToParkYoung = [0,0,0]
interestNature = [0,0,0]
interestConservation = [0,0,0]
goToPark = [0,0,0]
goToNonPark = [0,0,0]
pplShouldGo = [0,0,0]
tooCrowded = [0,0,0]

# I was exposed to hiking at a young age:
exposedToHikeYoung[1] = np.mean (data_train[:,1])
exposedToHikeYoung[0] = np.min (data_train[:,1])
exposedToHikeYoung[2] = np.max (data_train[:,1])

# I was exposed to national parks at a young age
exposedToParkYoung[1] = np.mean (data_train[:,2])
exposedToParkYoung[0] = np.min (data_train[:,2])
exposedToParkYoung[2] = np.max (data_train[:,2])

# I have always had an interest in nature
interestNature[1] = np.mean (data_train[:,3])
interestNature[0] = np.min (data_train[:,3])
interestNature[2] = np.max (data_train[:,3])

# I have always had an interest in conservation
interestConservation[1] = np.mean (data_train[:,4])
interestConservation[0] = np.min (data_train[:,4])
interestConservation[2] = np.max (data_train[:,4])

# In my free time, I go to national parks
goToPark[1] = np.mean (data_train[:,5])
goToPark[0] = np.min (data_train[:,5])
goToPark[2] = np.max (data_train[:,5])

# In my free time, I go to state parks/forest
goToNonPark[1] = np.mean (data_train[:,6])
goToNonPark[0] = np.min (data_train[:,6])
goToNonPark[2] = np.max (data_train[:,6])

# I think more people should visit national parks
pplShouldGo[1] = np.mean (data_train[:,7])
pplShouldGo[0] = np.min (data_train[:,7])
pplShouldGo[2] = np.max (data_train[:,7])

# I think national parks are too crowded
tooCrowded[1] = np.mean (data_train[:,8])
tooCrowded[0] = np.min (data_train[:,8])
tooCrowded[2] = np.max (data_train[:,8])

print ('I was exposed to hiking at a young age: ', exposedToHikeYoung)
print ('I was exposed to national parks at a young age: ', exposedToHikeYoung)
print ('I have always had an interest in nature: ', interestNature)
print ('I have always had an interest in conservation: ', interestConservation)
print ('In my free time, I go to national parks: ', goToPark)
print ('In my free time, I go to state parks/forest: ', goToNonPark)
print ('I think more people should visit national parks: ', pplShouldGo)
print ('I think national parks are too crowded: ', tooCrowded)

print('\n==========SECTION 2: REASONING==========')
forWildlife = [0,0,0]    # represents [min, mean, max]
forViews = [0,0,0]
forActivity = [0,0,0]
forWellness = [0,0,0]
forSocial = [0,0,0]
forSolo = [0,0,0]

# I would go to a national park for the wildlife (e.g. animals, plants)
forWildlife[1] = np.mean (data_train[:,9])
forWildlife[0] = np.min (data_train[:,9])
forWildlife[2] = np.max (data_train[:,9])

# I would go to a national park for the views (e.g. mountains)
forViews[1] = np.mean (data_train[:,10])
forViews[0] = np.min (data_train[:,10])
forViews[2] = np.max (data_train[:,10])

# I would go to a national park for the physical activity
forActivity[1] = np.mean (data_train[:,11])
forActivity[0] = np.min (data_train[:,11])
forActivity[2] = np.max (data_train[:,11])

# I would go to national park for wellness (e.g. mental health)
forWellness[1] = np.mean (data_train[:,12])
forWellness[0] = np.min (data_train[:,12])
forWellness[2] = np.max (data_train[:,12])

# I would go to a national park to socialize (i.e. be with friends or family)
forSocial[1] = np.mean (data_train[:,13])
forSocial[0] = np.min (data_train[:,13])
forSocial[2] = np.max (data_train[:,13])

# I would go to a national park for alone time
forSolo[1] = np.mean (data_train[:,14])
forSolo[0] = np.min (data_train[:,14])
forSolo[2] = np.max (data_train[:,14])

sec2Data = [forWildlife, forViews, forActivity, forWellness, forSocial, forSolo]
fig2 = plt.boxplot (sec2Data)
plt.xticks([1, 2, 3, 4, 5, 6], ['Wildlife', 'Views', 'Activity', 'Wellness', 'Social', 'Solo'])
plt.yticks([-2, -1, 0, 1, 2], ['Strongly Disagree', 'Somewhat Disagree', 'Neither Agree nor Disagree', 'Somewhat Agree', 'Strongly Agree'])
#plt.show();

print ('\n==========SECTION 3A: ENCOURAGE/DISCOURAGE==========')
costDis = [0,0,0]
timeDis = [0,0,0]
freeDis = [0,0,0]
equipDis = [0,0,0]
safetyDis = [0,0,0]
pubSafeDis = [0,0,0]
fitDis = [0,0,0]
disabDis = [0,0,0]

# The cost of visiting a national park DISCOURAGES
costDis[1] = np.mean (data_train[:,25])
costDis[0] = np.min (data_train[:,25])
costDis[2] = np.max (data_train[:,25])

# The travel time to go to a national park DISCOURAGES
timeDis[1] = np.mean (data_train[:,26])
timeDis[0] = np.min (data_train[:,26])
timeDis[2] = np.max (data_train[:,26])

# A lack of free time DISCOURAGES
freeDis[1] = np.mean (data_train[:,27])
freeDis[0] = np.min (data_train[:,27])
freeDis[2] = np.max (data_train[:,27])

# A lack of equipment poses a challenge
equipDis[1] = np.mean (data_train[:,28])
equipDis[0] = np.min (data_train[:,28])
equipDis[2] = np.max (data_train[:,28])

# Concerns over safety DISCOURAGES
safetyDis[1] = np.mean (data_train[:,29])
safetyDis[0] = np.min (data_train[:,29])
safetyDis[2] = np.max (data_train[:,29])

# Concern over public safety (e.g. harassment) DISCOURAGES 
pubSafeDis[1] = np.mean (data_train[:,30])
pubSafeDis[0] = np.min (data_train[:,30])
pubSafeDis[2] = np.max (data_train[:,30])

# My level of physical fitness or health DISCOURAGES
fitDis[1] = np.mean (data_train[:,31])
fitDis[0] = np.min (data_train[:,31])
fitDis[2] = np.max (data_train[:,31])

# A physical disability DISCOURAGES
disabDis[1] = np.mean (data_train[:,32])
disabDis[0] = np.min (data_train[:,32])
disabDis[2] = np.max (data_train[:,32])

print ('A lack of free time DISCOURAGES: ', freeDis)
print ('The travel time to go to a park DISCOURAGES: ', timeDis)
print ('A lack of equipment poses a challenge: ', equipDis)
print ('The cost of visiting a natl park DISCOURAGES: ', costDis)
print ('Concerns over safety DISCOURAGES: ', safetyDis)
print ('My level of physical fitness or health DISCOURAGES: ', fitDis)
print ('Concern over public safety DISCOURAGES : ', pubSafeDis)
print ('A physical disability DISCOURAGES: ', disabDis)

sec3Data = [freeDis, costDis, safetyDis, fitDis, pubSafeDis, disabDis]

# fig3 = plt.boxplot (sec3Data)
# plt.xticks([1, 2, 3, 4, 5, 6], 
#     ['Lack of free time disc.', 'Cost disc.', 'Safety disc.', 'Fitness disc.',
#       'Pub. Safe disc.', 'Disability disc.'])
# plt.yticks([-2, -1, 0, 1, 2], ['Strongly Disagree', 'Somewhat Disagree', 'Neither Agree nor Disagree', 'Somewhat Agree', 'Strongly Agree'])
# plt.show();

print ('\n==========SECTION 3B: ENCOURAGE/DISCOURAGE==========')
hiRanger = [0,0,0]
hiPeople = [0,0,0]
canHike = [0,0,0]
canCamp = [0,0,0]
canGet = [0,0,0]
wantToGo = [0,0,0]
withPeople = [0,0,0]
wasEnc = [0,0,0]

# I feel comfortable interacting with park rangers or officers
hiRanger[1] = np.mean (data_train[:,33])
hiRanger[0] = np.min (data_train[:,33])
hiRanger[2] = np.max (data_train[:,33])

# I feel comfortable interacting with strangers
hiPeople[1] = np.mean (data_train[:,34])
hiPeople[0] = np.min (data_train[:,34])
hiPeople[2] = np.max (data_train[:,34])

# I am confident in my ability to hike
canHike[1] = np.mean (data_train[:,35])
canHike[0] = np.min (data_train[:,35])
canHike[2] = np.max (data_train[:,35])

# I am confident in my ability to camp
canCamp[1] = np.mean (data_train[:,36])
canCamp[0] = np.min (data_train[:,36])
canCamp[2] = np.max (data_train[:,36])

# I am confident in my ability to get to a national park
canGet[1] = np.mean (data_train[:,37])
canGet[0] = np.min (data_train[:,37])
canGet[2] = np.max (data_train[:,37])

# I have a desire to go to a national park
wantToGo[1] = np.mean (data_train[:,38])
wantToGo[0] = np.min (data_train[:,38])
wantToGo[2] = np.max (data_train[:,38])

# I would feel more comfortable if I went with a group to a national park
withPeople[1] = np.mean (data_train[:,39])
withPeople[0] = np.min (data_train[:,39])
withPeople[2] = np.max (data_train[:,39])

# I have been ENCOURAGED by friends or family to visit 
wasEnc[1] = np.mean (data_train[:,42])
wasEnc[0] = np.min (data_train[:,42])
wasEnc[2] = np.max (data_train[:,42])

print ('I have a desire to go to a national park: ', wantToGo)
print ('Want to go with group: ', withPeople)
print ('I have been ENCOURAGED to visit: ', wasEnc)
print ('I am confident in my ability to get to park: ', canGet)
print ('I feel comfortable interacting with park rangers: ', hiRanger)
print ('I am confident in my ability to hike: ', canHike)
print ('I feel comfortable interacting with other: ', hiPeople)
print ('I am confident in my ability to camp: ', canCamp)


print ('\n==========SECTION 4: APP==========')
reviewsLike = [0,0,0]    # represents [min, mean, max]
campStay = [0,0,0]
reviewsNotLike = [0,0,0]
howToHike = [0,0,0]
howClose = [0,0,0]
whichPark = [0,0,0]
whatEquipment = [0,0,0]
howPopular = [0,0,0]
howChallenging = [0,0,0]
offlineMap = [0,0,0]
whatCost = [0,0,0]

# Reviews from people like you (e.g. experience level, gender, age) would encourage you go to a national park
reviewsLike[1] = np.mean (data_train[:,43])
reviewsLike[0] = np.min (data_train[:,43])
reviewsLike[2] = np.max (data_train[:,43])

# Information on where to camp/stay/sleep
campStay[1] = np.mean (data_train[:,44])
campStay[0] = np.min (data_train[:,44])
campStay[2] = np.max (data_train[:,44])

# Reviews from people NOT like you 
reviewsNotLike[1] = np.mean (data_train[:,45])
reviewsNotLike[0] = np.min (data_train[:,45])
reviewsNotLike[2] = np.max (data_train[:,45])

# Advice on how to hike
howToHike[1] = np.mean (data_train[:,46])
howToHike[0] = np.min (data_train[:,46])
howToHike[2] = np.max (data_train[:,46])

# Information on how close a park is
howClose[1] = np.mean (data_train[:,47])
howClose[0] = np.min (data_train[:,47])
howClose[2] = np.max (data_train[:,47]) 

# Advice on which parks to go to
whichPark[1] = np.mean (data_train[:,48])
whichPark[0] = np.min (data_train[:,48])
whichPark[2] = np.max (data_train[:,48]) 

# Advice on what equipment is needed per trail/park
whatEquipment[1] = np.mean (data_train[:,49])
whatEquipment[0] = np.min (data_train[:,49])
whatEquipment[2] = np.max (data_train[:,49]) 

# How popular or full the park is would be helpful
howPopular[1] = np.mean (data_train[:,50])
howPopular[0] = np.min (data_train[:,50])
howPopular[2] = np.max (data_train[:,50]) 

# Information on how challenging a trail/park would be helpful
howChallenging[1] = np.mean (data_train[:,51])
howChallenging[0] = np.min (data_train[:,51])
howChallenging[2] = np.max (data_train[:,51]) 

# An offline map of the park would be helpful
offlineMap[1] = np.mean (data_train[:,52])
offlineMap[0] = np.min (data_train[:,52])
offlineMap[2] = np.max (data_train[:,52]) 

# Information on how much the trip would cost would be helpful 
whatCost[1] = np.mean (data_train[:,53])
whatCost[0] = np.min (data_train[:,53])
whatCost[2] = np.max (data_train[:,53]) 

print ('Information on where to camp/stay/sleep: ', campStay)
print ('An offline map of the park would be helpful: ', offlineMap)
print ('Advice on which parks to go to: ', whichPark)
print ('Information on how much the trip would cost would be helpful: ', whatCost)
print ('Advice on what equipment is needed per trail/park: ', whatEquipment)
print ('Information on how challenging a trail/park would be helpful: ', howChallenging)
print ('How popular or full the park is would be helpful: ', howPopular)
print ('Information on how close a park is: ', howClose)
print ('Reviews from people like you: ', reviewsLike)
print ('Advice on how to hike: ', howToHike)
print ('Reviews from people NOT like you : ', reviewsNotLike)

sec4Data = [campStay, offlineMap, whichPark, whatCost,
            whatEquipment, howChallenging, howPopular, howClose, reviewsLike, howToHike, reviewsNotLike]

fig4 = plt.boxplot (sec4Data)
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 
    ['Where to Camp', 'Offline Map', 'Park Selection', 'Cost',
      'Equipment Selection', 'Difficulty', 'Popularity', 
      'Proximity', 'Reviews Like You','How To Hike', 'Reviews Not Like You'])
plt.yticks([-2, -1, 0, 1, 2], ['Strongly Disagree', 'Somewhat Disagree', 'Neither Agree nor Disagree', 'Somewhat Agree', 'Strongly Agree'])
#plt.show();

print('\n==========SECTION 5: RESULTS==========')


