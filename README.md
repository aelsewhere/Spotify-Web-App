## Getting Started
_**Before exploring**_: look at secret.py. This file is necessary for using the rest of these spotify wrapped features. You will need to get your *own* CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, and SCOPE. You can get your info on [Spotify's Site for Developers](https://developer.spotify.com/). For more info on getting an access token, look [here](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token).

# Spotify Web App AI Playlist Generator

### Monthly Top 50


### Mood-Generated Playlists
Pick 1-3 moods to generate a personalized Spotify playlist. Mood emotions gathered from [The Hoffman Institute](https://www.hoffmaninstitute.org/wp-content/uploads/Practices-FeelingsSensations.pdf).

Example of emotions storage:

| Emotion               | Family 1                  | Family 2               | Intensity              |
|-----------------------|---------------------------|------------------------|------------------------|
| Calm                  | Accepting                 | Tender                 | 2                      |
| Centered              | Accepting                 |                        | 2                      |

Emotion column is straightforward. Family 1 is the general umbrella the emotion falls under. Family 2 is an optional category if the emotion falls under two umbrellas. Intensity is scored 1-5 how strong the emotion generally tends to be. 

There are 18 umbrella categories:

* Accepting
* Joy
* Angry
* Courageous
* Loving
* Curious
* Sad
* Numb
* Shame
* Fear
* Fragile
* Grateful
* Guilt
* Hopeful
* Powerless
* Tender
* Stressed
* Doubt

### Song-Generated Playlist