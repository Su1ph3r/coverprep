#!/usr/local/bin/python3

'''
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
'''

import argparse
import subprocess

parser = argparse.ArgumentParser(
    description='Downloads YouTube video as MP3 and splits it into multi tracks')
parser.add_argument('-u', '--url', dest='url',
                    help='URL of the YouTube video', required=True)
parser.add_argument('-o', '--output', dest='outfile',
                    help='Output Filename', required=True)

args = parser.parse_args()

# Use Youtube-dl to download the video


def download(url, outfile):
    subprocess.call(['youtube-dl', '-x', '--audio-format',
                    'mp3', '-o', outfile + '.%(ext)s', url])

# Use Spleeter to split the audio into multi tracks


def split(outfile):
    subprocess.call(['spleeter', 'separate', '-p',
                    'spleeter:4stems', '-o', outfile, '%s.mp3' % outfile])
    # Remove the downloaded MP3 file
    subprocess.call(['rm', '%s.mp3' % outfile])


# Run the downloader
print('\nDownloading...\n')
download(args.url, args.outfile)

# Run the splitter
print('\nSplitting...\n')
split(args.outfile)
