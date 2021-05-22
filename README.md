# Easy Lofi Youtube Playlist Search CLI

## Issue

YouTube can be a pretty distracting place. Although I use other streaming services for the majority of my music listening, occasionally I'll play a lofi playlist while trying to focus on a task. Besides a bombardment of enticing recommended videos it can be hard to pick a specific playlist from the options.

This CLI was built to solve these issues taking a simple input (does not handle special characters at the moment), makes an API request to Youtube with the "{input} + lofi" and then opens up the first result back. In essence an "I'm feeling lucky lofi video search from terminal.

## Supported Functionalities

Currently only allow for input with no special character

## TODO

* Allow for a second mode to just randomly pick a genre. No specific search needed
* Error Handling for special characters or handle special characters
* See if only playing the first result is the best result. Potential Solution randomize the video that is opened between the first result -- will create variability while still maintaining relevancy
