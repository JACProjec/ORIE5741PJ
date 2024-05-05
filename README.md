# ORIE5741PJ
Repository for ORIE5741 group project work

**Names of team:**
James Clark
Alex Hertadi
Katherine O'Connor

**Net ID:**
JAC692
AFH78
KSO25

# Overview
Our project consists of an analysis of gaming subreddit data to determine whether there is a relationship between the activity on a games subreddit and the sentiment of this activity, and the impact this has on the number of active players. We are also investigating whether this differs between type of video game.

We define type of game as:
 - Single release: Game is released completed
 - Single release with DLC: Game is release completed and updated periodically with additional content
 - Single release and updated: Game is released in an alpha state and updated over a several months/years

For our selection of games, we wanted games that matched these profiles and also were released over a similiar time frame. Thus we settled on Dark Souls 3, No Man's Sky and Stardew Valley, all games released in 2016 and all with (at the time) active subreddits.

# Input Data
Our data is sourced from an [academic torrents](https://academictorrents.com/details/9c263fc85366c1ef8f5bb9da0203f4c8c8db75f4/tech&filelist=1) website and because of its size, is stored in .zst format. Our first step in EDA will be to download, decompress and extract all data relating to the above 3 subreddits.

The data in question is very detailed and contains information about:
- Subreddit of the post
- Engagement with the post (upvotes and downvotes)
- Text of post/comment
- Date posted

There are a large number of fields available, but for our analysis we will focus on the above. A full list of features available can be found in the info.md files [here](https://drive.filen.io/f/fb67389b-2eb2-42e8-9d2f-474ca153e105#cgZ5eW2NWXuS9n9rVhdnTkPDmZAeuOhk)

Our input data is very large and requires a drive link to download (found [here](https://drive.google.com/drive/folders/1zf7hDntAEjSkgaZHAL7tawRT5hVLaxZ9?usp=sharing).

To clean it we simply downloaded comment and post data for 2016-01-01 - 2017-01-05 from the academic torrent. This took significant space up on our computers (~800gb) since it composed comments and posts from all subreddits. We filtered for our relevant games and compressed into zst files. 

Should you wish to do the same, you may unpack the files using [ztsd_unpack](data_processing/ztsd_unpack.py) and filter for subreddits using [subreddit_filter](data_processing/subreddit_filter.py)

# How to run

To begin, download the data from the google drive link above. The data has already been filtered and is in json form. 
**Please note:** This data is very large, particularly comments, so running the notebook without a good memory and processing speed will take some time! If you do not wish to run the sentiments analysis, we have preprocessed the sentiments for posts and comments [here](https://drive.google.com/drive/folders/1R2RbRyzjkVBQ8fBwrfUX97MMRnrfCk9c). Simply move these csvs into the same folder as the notebook and comment out the sentiment functions and **only use the pd.read_csv** line!





