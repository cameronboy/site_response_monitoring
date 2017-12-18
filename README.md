# Site Monitoring:


## I thought I would look into the trends of content load times as net neutrality is looking more and more like yesterday's news.

### The why.

- With net neutrality appearing to be repealed, I wanted to take a look at how my ISP Comcast is handling traffic to a number of sites.

- I'm only intending to monitor the initial transfer of data necessary to load the site; however, I'm sure any potential throttling occurring in the future would be more sophisticated than slowing down anything with the youtube.com domain.



### The How.

- Using the `requests` and `gspread` packages I'm inefficiently looping through my site list and using the `request.elapsed.total_seconds()` to provide the time it took to load the page.


- I'm not backing into effective bandwidth, only time necessary to download the landing page content.

- Now it's intended to be run on a raspberry pi so local storage isn't an option I'm capable of exploring.


#### Future to do:

1. Error handling & recording of said Error
2. New data storage option as I'm sure there will be a time where I outgrow the google sheets 400K cell max.



## Here are the sites currently recorded

1. **Site**: A Combination of Provider and category

2. **Type**: Indcates the "*type*" of site. This list originated with only video streaming sites so this field indicated whether it was from a Provider (ISP) or a Dedicated streaming site like Youtube. Since adding controls and Social Media it lost some congruency.
3. **Category**: Groups the sites into some helpful categories for analysis like Control, social media, speed test etc.
4. **Provider**: The company providing the site/service.
5. **URL**: Web address the site/service is located at.


| site                      | type          | category     | provider          | url                                                                  |
|---------------------------|---------------|--------------|-------------------|----------------------------------------------------------------------|
| CO Gov - Control          | Gov Site      | Control      | CO Gov            | https://www.colorado.gov/                                            |
| EPA - Control             | Gov Site      | Control      | EPA               | https://www.epa.gov/                                                 |
| Government - Control      | Gov Site      | Control      | Government        | https://www.usa.gov/                                                 |
| CNN - Control             | News          | Control      | CNN               | https://www.cnn.com/                                                 |
| FOX - Control             | News          | Control      | FOX               | http://www.foxnews.com/                                              |
| Motogp (Spain) - Control  | Racing        | Control      | Motogp (Spain)    | http://www.motogp.com/                                               |
| Google - Control          | Search Engine | Control      | Google            | https://google.com                                                   |
| Facebook - Social Media   | Social Media  | Social Media | Facebook          | https://www.facebook.com/                                            |
| Instagram - Social Media  | Social Media  | Social Media | Instagram         | https://www.instagram.com/                                           |
| Microsoft - Social Media  | Social Media  | Social Media | Microsoft         | https://www.linkedin.com                                             |
| Pinterest - Social Media  | Social Media  | Social Media | Pinterest         | https://www.pinterest.com/                                           |
| Twitter - Social Media    | Social Media  | Social Media | Twitter           | https://twitter.com/                                                 |
| Armstrong - Speed Test    | Provider      | Speed Test   | Armstrong         | http://speedtest.zoominternet.net/                                   |
| AT&T - Speed Test         | Provider      | Speed Test   | AT&T              | http://speedtest.att.com/speedtest/                                  |
| CenturyLink - Speed Test  | Provider      | Speed Test   | CenturyLink       | http://internethelp.centurylink.com/internethelp/zam-speed-test.html |
| Comcast - Speed Test      | Provider      | Speed Test   | Comcast           | http://speedtest.xfinity.com/                                        |
| Cox - Speed Test          | Provider      | Speed Test   | Cox               | https://www.cox.com/residential/support/internet/speedtest.html      |
| Frontier - Speed Test     | Provider      | Speed Test   | Frontier          | http://speedtest.frontier.com/                                       |
| GCI - Speed Test          | Provider      | Speed Test   | GCI               | http://speedtest.gci.com/                                            |
| MidContinent - Speed Test | Provider      | Speed Test   | MidContinent      | http://speedtest.midco.net/                                          |
| Spectrum - Speed Test     | Provider      | Speed Test   | Spectrum          | https://www.spectrum.com/internet/speed-test                         |
| Verizon - Speed Test      | Provider      | Speed Test   | Verizon           | https://www.verizon.com/speedtest/                                   |
| ookla - Speed Test        | Speed Test    | Speed Test   | ookla             | http://www.speedtest.net/                                            |
| Amazon - Video            | Dedicated     | Video        | Amazon            | https://www.amazon.com                                               |
| FuboTV - Video            | Dedicated     | Video        | FuboTV            | https://www.fubo.tv                                                  |
| Google - Video            | Dedicated     | Video        | Google            | https://www.youtube.com                                              |
| Google - Video            | Dedicated     | Video        | Google            | https://tv.youtube.com/                                              |
| Hulu - Video              | Dedicated     | Video        | Hulu              | https://www.hulu.com                                                 |
| Netflix - Video           | Dedicated     | Video        | Netflix           | https://www.netflix.com                                              |
| RLJ Entertainment - Video | Dedicated     | Video        | RLJ Entertainment | https://www.acorn.tv                                                 |
| RLJ Entertainment - Video | Dedicated     | Video        | RLJ Entertainment | https://umc.tv                                                       |
| Sony - Video              | Dedicated     | Video        | Sony              | https://vue.playstation.com/watch/                                   |
| AT&T - Video              | Provider      | Video        | AT&T              | https://www.directvnow.com                                           |
| Comcast - Video           | Provider      | Video        | Comcast           | https://tv.xfinity.com/                                              |
| Dish Network - Video      | Provider      | Video        | Dish Network      | https://www.sling.com/                                               |
| T-Mobile - Video          | Provider      | Video        | T-Mobile          | https://layer3tv.com                                                 |
| Verizon - Video           | Provider      | Video        | Verizon           | https://www.go90.com                                                 |
| CBS - Video               | Station       | Video        | CBS               | https://www.cbs.com                                                  |
| HBO - Video               | Station       | Video        | HBO               | https://play.hbonow.com/                                             |
| Showtime - Video          | Station       | Video        | Showtime          | https://www.showtime.com                                             |
