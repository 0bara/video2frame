# convert video to frames 
# ref: https://note.nkmk.me/python-opencv-video-to-still-image/

import os
import cv2
import click

@click.command()
@click.option('--output-dir', '-d', 'odir', help='output directory', default='.')
@click.option('--output-fmt', '-e', 'ofmt', help='output file-format', default='.png')
@click.argument('source')

def cli(odir, ofmt, source):
    if not source:
        click.echo("convert video to frame (image files).")
        return
    
    os.makedirs(odir, exist_ok=True)
    base_path = os.path.join(odir, "img")
    v = cv2.VideoCapture(source)
    digit = len(str(int(v.get(cv2.CAP_PROP_FRAME_COUNT))))
    n = 0
    while v.isOpened():
        ret, frame = v.read()
        if not ret:
            break
        cv2.imwrite(f"{base_path}_{str(n).zfill(digit)}{ofmt}", frame)
        n += 1
    v.release()

if __name__ == '__main__':
    cli()