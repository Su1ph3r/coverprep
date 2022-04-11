# coverprep

Downloads audio from a YouTube video and uses Spleeter to split it into multi tracks.
Multi tracks can then be loaded in a DAW and used to create a cover.

Example Usage:
python3 coverprep.py -u https://youtu.be/dQw4w9WgXcQ -o Example

Example Output:
Downloading...

[youtube] dQw4w9WgXcQ: Downloading webpage
[download] Destination: Example.webm
[download] 100% of 3.28MiB in 01:05
[ffmpeg] Destination: Example.mp3
Deleting original file Example.webm (pass -k to keep)

Splitting...

INFO:spleeter:File Example/Example/vocals.wav written succesfully
INFO:spleeter:File Example/Example/drums.wav written succesfully
INFO:spleeter:File Example/Example/bass.wav written succesfully
INFO:spleeter:File Example/Example/other.wav written succesfully
