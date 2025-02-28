This application generates a Spotify playlist featuring the top 100 songs from a user-specified date. It was created using Pyton v3.13.

Before runing the app, you need to set up your Spotify account by going to https://developer.spotify.com/dashboard and creating a new project. Client ID and Client Secret are used by Spotify to allow third-party applications to access a Spotify user's account (see https://developer.spotify.com/documentation/web-api/concepts/authorization).
The songs are sourced by web scraping Bilboard Hot 100 website. Then, using Spotipy library (see https://spotipy.readthedocs.io/en/2.25.1/),  the app creates a new Spotify playlist and adds the songs to it.
