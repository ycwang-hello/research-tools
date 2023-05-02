# -*- coding: utf-8 -*-
"""
Created on Mon May  1 21:12:00 2023

@author: Yu-Chen Wang
"""

from argparse import ArgumentParser
import os
import re
import glob
from zipfile import ZipFile, ZIP_DEFLATED
import subprocess

parser = ArgumentParser()

parser.add_argument('file', nargs="?", default=None, help='The main tex file. If not given, automatically use the .tex file (if there is only one) in the current working directory.')
parser.add_argument('-o', '--out', help='The name of the output zip file. The default is the same as that of the main tex file.')
parser.add_argument('-p', '--params', default='', help='The parameters passed to latexpand')
parser.add_argument('-b', '--bibtex', action='store_true', help='Use bibtex (with .bst, .bib) files. By default, bibliography is expanded using the *.bbl file.')

args = parser.parse_args()

if args.file is None:
    files = os.listdir('.')
    texfiles = [f for f in files if f.endswith('.tex')]
    if len(texfiles) != 1:
        raise ValueError('Please input the main tex file.')
    else:
        args.file = texfiles[0]

if args.out is None:
    args.out = args.file[:-4] + '.merged.zip'

if os.path.exists(args.out):
    overwrite = input(f'"{args.out}" already exists. Do you want to overwrite it? y/[n] >>> ')
    if overwrite not in ['y']:
        raise FileExistsError(f'"{args.out}" already exists. Nothing done.')

if '--expand-bbl' not in args.params and not args.bibtex:
    bblfile = args.file[:-4] + '.bbl'
    if not os.path.exists(bblfile):
        raise FileNotFoundError(f"{bblfile} not found. You may consider passing `--bibtex` or `-p \"--expand-bbl BBLFILE\"` or generating a bbl file.")
    args.params += f' --expand-bbl {bblfile}'

output = subprocess.check_output(['latexpand'] + args.params.split() + [args.file])
maintex = output.decode()

includegraphics = r"\\includegraphics(?:\[[^\]]*\])?\{[^\}]*\}"
graphics = re.findall(includegraphics, maintex, flags=re.DOTALL)
imgpaths = [t.split('{')[1].split('}')[0] for t in graphics]

documentclass = r"\\documentclass(?:\[[^\]]*\])?\{[^\}]*\}"
clsfile = re.findall(documentclass, maintex, flags=re.DOTALL)[0].split('{')[1].split('}')[0]

def get_rel_path(mainpath, relpath):
    return os.path.relpath(os.path.join(os.path.dirname(mainpath), relpath))
def move(relpath, f, ext='.*', prefix=''):
    global maintex
    path = get_rel_path(args.file, relpath)
    newpath = prefix + os.path.basename(path)
    maintex = maintex.replace(relpath, newpath)
    if not os.path.exists(path):
        paths = glob.glob(path + ext)
        if len(paths) == 0:
            raise FileNotFoundError(path)
        elif len(paths) >= 2:
            raise ValueError(f'I do not know which to use: {paths}')
        path = paths[0]
        newpath += '.' + path.split('.')[-1]
    f.write(path, arcname=newpath)


with ZipFile(args.out, 'w', compression=ZIP_DEFLATED) as f:
    # cls file
    try:
        move(clsfile, f, ext='.cls')
    except FileNotFoundError:
        pass
    
    # bst, bib file
    if args.bibtex:
        bibliography = r"\\bibliography(?:\[[^\]]*\])?\{[^\}]*\}"
        bibfiles = [t.split('{')[1].split('}')[0] for t in re.findall(bibliography, maintex, flags=re.DOTALL)]
        
        bibliographystyle = r"\\bibliographystyle(?:\[[^\]]*\])?\{[^\}]*\}"
        bstfiles = [t.split('{')[1].split('}')[0] for t in re.findall(bibliographystyle, maintex, flags=re.DOTALL)]
        
        for bibfile in bibfiles:
            move(bibfile, f, ext='.bib')
        for bstfile in bstfiles:
            try:
                move(bstfile, f, ext='.bst')
            except FileNotFoundError:
                pass
    
    # img file
    for i, imgpath in enumerate(imgpaths):
        move(imgpath, f, prefix=f'fig{i+1}_')
    
    with f.open(os.path.basename(args.file), mode='w') as texf:
        texf.write(maintex.encode())
