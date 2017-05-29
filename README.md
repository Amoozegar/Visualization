Data Visualization for analyzing the relationship between the performance of the baseball players and their weight

This visualization is provided to show the relationship between Average home runs and the weight of 1157 baseball players for one year. The points are colored according to the handedness of each player.

Design decisions:

The reason for using scatter plots is to describe the relatioship between two variables(average home runs and weight) while being able to access the individual data points, actually in this case we have paired numerical data (weight for each player and the corresponding average home runs for that player), so we can investigate the relatioship between these variables using scatter plots. In order to be able to compare the performance of baseball players with different handedness, the points are colored according to handedness of players. Also an interactive legend is added to the plot to be able to filter the points according to handedness of players and compare them. The visual encodings that were used in this visualization are position x for weight, position y for batting average and color hue for handedness.

It should be noted that the players with home runs equal to zero had batting average equal to zero which shows that these players probably didn't play in that given year. So they were removed from the data set when doing the visualization.

Conclusions based on this visualization:
_ From this graph, it is clear that handedness isn't a good indicator of the average home runs of the players.

_There is correlation between average home runs and the weight of players. Players with larger weights seem to have more number of home runs than others.

Here are the feedbacks that I got for this data visualization:

Feedback 1:

1.	I noticed that most players seem to average under 80 home runs. Handedness seems to be evenly scattered.
2.	Is there a relationship between handedness and home runs?
3.	There may be a relationship between weight and home runs.
4.	To me, the graph shows that handedness is not a good indicator of home runs, but weight of the player may be.
5.	Is it average home runs per year? Lifetime? I'm not into sports so I really have no idea. 

feedback 2:

The graph looks good and is showing several fields such as weight, average home runs, batting average and handedness by color.
I can see that by increasing the weight, average home runs would increase and as a result the performance of the players would increase.
I think there is a problem with the legend and it doesn't work correctly when clicking on the legend the first time.

Feedback 3:

I don't know much about baseball but I can give you my feedback:
- I observed a weak relationship between home runs and weight in general but it seemed a little more stronger for right handedness.
- You didn't labelled the x-axis or may be I didn't see it on my browser.
- the legend should be more clear I think, put Right, Left...eccc
  
 Feedback 4:

the bubble size causes a deal of overlap and it makes it very difficult to compare home run and batting average. 
For legends, "Left", "Right", "Both" would be much clearer than L,R,B. 
It's better to explain the story to the reader in the title. 

Feedback 5:
This feedback is from Udacity reviewer:
there is the one important point that should be improved still: You have grouped bubbles according to each possible weight value. As some values do not exist (for example 141-147) increments between each bubble are different. This can confuse the viewer a bit as usually grouped values should follow in increment of the same, so if the viewer sees bubble without fixed increment he or she incline to think that every bubble shows particular value, not summarizing.

In order to fix this, please group the data for every weight period, so there will be three bubbles for every category (left, both, right). Categories can be as following: 140-150, 150-160, 160-170 and so on.

Note: for feedback 5 I used python to group the data according to handedness and group categories for weight that I created in python. I exported the results in a new CSV file called "New_baseball_data" and used that for visualization. The python code is also included in the project folder. 

After getting the fifth feedback, I decided to change the y-axis to batting average . Because I wanted to show clear findings about the data set. As it was mentioned previously the x axis contains the ranges of weights like 130-140, 140-150,.. . and the average of batting average for each category of handedness for each range is calculated and is shown by colored circles. 