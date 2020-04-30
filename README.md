#   **spider**

### *python crawler and data analysis and visualization*

***

##  **Technology stack**

-   python3 

-   requests

-   pyquery

-   pandas

-   matplotlib.pyplot

***

##  **Note**

    With caching, the crawler was a little slow the first time, and it was a flash later

***

##  doubanTop250

### crawling movie data

    title, quoto, cover_image, ranking, score, comments, time, region, category...

    Write to file in JSON format

    save to mongodb

### data analysis and visualization

1. score the top ten
!['score the top ten'](https://github.com/realRichard/crawler/blob/master/visualization/doubanScore.png 'score the top ten')

2. movie category
!['movie category'](https://github.com/realRichard/crawler/blob/master/visualization/doubanCategory.png 'movie category')

3. movie region
!['movie region'](https://github.com/realRichard/crawler/blob/master/visualization/doubanRegion.png 'movie region')

4. movie release time proportion
!['movie region'](https://github.com/realRichard/crawler/blob/master/visualization/doubanTime.png 'movie region')

***

##  zhihuAnser

### crawling anser data

    question, question link, agreement numbers, author, anser content, comments...

    Write to file in JSON format

    save to mongodb