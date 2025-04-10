# Profiles
## Project about finding optimal angle and position between 2 tubes before weld them
## File purpose
### Files-functions
#### cs_change.py
Functions for transform coordinates from Cartesian to polar, from polar to Cartesian and for interpolate polar coordinates with same angle step
#### center_finder.py
2 functions for find center of tube: by find center of mass of tube volume and by find center of mass of tube shell 
#### profile_generator.py
Function generates tube profile for test program
#### center_correction.py
By center_finder corrects tube center and places it in reference point
#### stat_tube_pos.py
Function measures tube coordinates relatively static rollers, after rotation at target angle
#### angles_of_arms.py
Function measures angle of elevation of dynamic rollers, to maintain alignment
### Work files
#### final_compare.py
Via all previous functions, outputs rotation angle and angles of elevation of 2 dynamic rollers
#### profile_reader.py и profile_saver.py
Programs for work with profile files
