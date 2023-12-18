# The Importance of Pitch Sequencing in the MLB

## Introduction:
In the MLB, teams tend to seek out pitchers with better pitch characteristics when acquiring pitchers. Wholistically, a pitcher's pitch characteristics has become functionally known as "stuff". Simply put, pitchers with better "stuff" are generally targetted by teams more. Team's value these players because there is a larger margin of error in their pitchers. For example, let's say we look at two different pitchers' fastballs. One pitcher throws a 98 MPH fastball with a high spin rate, the other a 91 MPH fastball with an average spin rate. The pitcher that throws a 98 MPH fastball has a larger margin for error when it comes to the location of their pitches because it's harder for batters to square up and make significant contact. This compares to the pitcher with the 91 MPH fastball who has a smaller location area to yield success.

With all the above said, there are plenty of pitchers in the MLB who have success with average or below average "stuff". The code for this project will be used to try and determine how these pitchers have success at the major league level. Specifically, I will look at the art of pitch sequencing. Pitch sequencing is the order a pitcher throws his specific pitches in an attempt to further deceive the hitter. The goal is to identify pitchers who are effectively sequence their pitchers to yield more success than may be expected.

## The Data:
The data for this project consists of 3 main datasets:
1. Every pitch from the 2023 MLB season, sourced from Baseball Savant via the PyBaseball Python package
2. FanGraphs Stuff+ Metric from FanGraphs.com **ADD LINK**
3. A crosswalk between players Baseball Savant ID and FanGraphs IDs, sourced from [SmartFantasyBaseball.com]([url](https://www.smartfantasybaseball.com/tag/player-id/)https://www.smartfantasybaseball.com/tag/player-id/)
