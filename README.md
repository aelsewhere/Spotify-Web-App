## Getting Started
_**Before exploring**_: look at secret.py. This file is necessary for using the rest of these spotify wrapped features. You will need to get your *own* CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, and SCOPE. You can get your info on [Spotify's Site for Developers](https://developer.spotify.com/). For more info on getting an access token, look [here](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token).

# Spotify Web App AI Playlist Generator

### Monthly Top 50

During the peak of the COVID-19 pandemic in 2020, I decided it was the perfect time to really expand my music taste. I’ve always loved discovering new music, so I figured why not put some real effort into it? That’s when I got super into making Spotify playlists. Now, I’ve got hundreds—some are basic, like indie pop or classic rock, and others are way more specific, like ones inspired by a single scene from a TV show. For example, I’m a big Attack on Titan fan, so I made a "Rumbling" playlist just for that vibe.  

At some point, I realized a good way to keep discovering music was to make a monthly Top 50 playlist. Every month, I’d put together 50 songs that I’d been listening to, kind of like a personal snapshot of my music for that time. I had a few rules for myself: the songs had to be fresh (nothing I’d added in the last six months), and I had to actually listen to them during that month. Sometimes I’d check the calendar and realize I was running out of time, so I’d throw on some random Spotify recommendations to make sure I had enough new stuff. I’d also get song suggestions from friends, and different seasons, holidays, and life events would naturally influence the playlists too. 

Over time, these playlists became really special to me. Now that I have years’ worth of them, I love being able to go back and listen to, say, March 2021 and instantly remember what that time in my life felt like. It’s like a little time capsule in music form. And as a data scientist, it hit me—if I love this so much, maybe other people would too.  

That’s where this app comes in. The whole idea is to make a Monthly Top 50 generator using AI. You log into your Spotify, and it pulls your listening data to create a personalized top 50 playlist for any month you choose. The AI doesn’t just pick random songs—it actually arranges them in a way that makes sense, so the playlist flows naturally. One of the coolest features is that you can retroactively create playlists for past months, even if you weren’t doing it manually at the time. Just log in, pick a month and year, and boom—your playlist is ready to go.


### Mood-Generated Playlists

Another cool feature of the site is the mood-based playlist builder. Instead of just picking a genre or artist, you can create a playlist based on how you're feeling. There are hundreds of moods to choose from, and you can select up to three at a time to really fine-tune the vibe you're going for.  

To make it even more intuitive, moods are organized by color—18 different colors representing different emotional categories. Within each color, the intensity of the mood is shown through opacity, so you can easily find the right match for how you’re feeling in the moment.  

Once you’ve chosen your moods and set the playlist length, the algorithm gets to work. Using your Spotify listening history, it pulls together a playlist that not only matches your mood but also fits your personal taste. Whether you need something chill for a rainy day, energetic for a workout, or nostalgic for a late-night drive, the mood-based builder makes sure you always have the perfect soundtrack.


Pick 1-3 moods to generate a personalized Spotify playlist. Mood emotions gathered from [The Hoffman Institute](https://www.hoffmaninstitute.org/wp-content/uploads/Practices-FeelingsSensations.pdf).

Example of emotions storage:

| Emotion               | Family 1                  | Family 2               | Intensity              |
|-----------------------|---------------------------|------------------------|------------------------|
| Calm                  | Accepting                 | Tender                 | 2                      |
| Centered              | Accepting                 |                        | 2                      |

Emotion column is straightforward. Family 1 is the general umbrella the emotion falls under. Family 2 is an optional category if the emotion falls under two umbrellas. Intensity is scored 1-5 how strong the emotion generally tends to be. 

There are 18 umbrella categories:

Accepting, Joy, Angry, Courageous, Loving, Curious, Sad, Numb, Shame, Fear, Fragile, Grateful, Guilt, Hopeful, Powerless, Tender, Stressed, Doubt

### Media-Generated Playlist *coming soon!*


Coming soon: a playlist generator inspired by your favorite movies, TV shows, books, and more! Instead of just making a playlist based on a mood or genre, this feature lets you create one that captures the essence of your favorite stories.  

The playlist pulls songs from your own listening history, blending them with tracks featured in the media itself. If a movie or show has an iconic soundtrack, those songs can be added too—along with music from similar films, shows, or books that share the same vibe. Whether you want the moody atmosphere of your favorite sci-fi series or the upbeat energy of a classic coming-of-age film, this generator helps bring your favorite stories to life through music.
