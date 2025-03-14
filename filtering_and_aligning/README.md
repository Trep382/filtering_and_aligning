
## Copy your pickle into pickle_folder
## Elaborate data from bags saved in a pickle file
```bash
cd filtering_and_aligning
python3 filtering_and_aligning/pickle_filtering.py 
```
## Enjoy your revised pickle!

## Features
Ever wondered why your metrics come out looking a little suspect? Most often the culptrit is a missing data at a certain time-stamp or a perceived sudden movement of the agent which causes some metrics to get all messy. Not good.
Luckily for you my python file is here to help you!
Featuring:
    - haysel filter for extreme outlier removal
    - exponential moving average for a little smoothing (more aggressive smoothing can be achieved by changing the parameter that goes in create_filtered-data)
    - timestamps alignment between robot and agent, with the missing data being filled
## Notes
This assumes that your ros2 data bag has been extracted into a pickle, and features the 'transforms' and 'agents' fields.