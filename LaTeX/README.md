# LaTeX
## LaTeX templates
My LaTeX templates.
- `template_A4 homework.tex`: An A4 template suitable for homework. An example explaining the usage is coming soon.

## latexport
### Introduction
When sharing or uploading your LaTeX documents to some websites, you may need to provide a minimum set of files (that can be complied, and no subdirectories). For example, you need to create a folder that contains a single main `.tex` file (without comments, `\input`, etc.), and the images included are also in the folder. `.cls`, `.bst`, `.bib`, `.bbl` should also be included if necessary. 

Sometimes you may write different sections of your document in separate `.tex` files or store image files in different folders for clarity. Additionally, there may be images that are no longer needed in the document. This can make it inconvenient to prepare the minimum working set of files, and updating the set of files can be tiring if changes are made to the document later on.

 `latexport.py` is a simple Python script that:
- Removes comments and inserts content included by `\input`, etc. to generate the main `.tex` file (requires the installation of `latexpand`, which should already be included if you use TeX Live, etc.).
- Exports a zip file (with the file extension `.merged.zip`) that contains the minimum working set of LaTeX files, with no subdirectories.
- Includes images that are referenced by `\includegraphics`, as well as any necessary `.cls`, `.bst`, `.bib`, and `.bbl` files in the zip file. Additionally, the script updates the paths referring to these files in the main `.tex` file so that it can be compiled successfully.

**Important!** Please note that this script is far from sophisticated. Many types of dependent files are not yet considered, and I have not done a thorough test considering any possible situations. Thus, this script may not work perfectly for your case. Please read and understand the terms and conditions of the MIT license. 

If you find errors or have suggestions, you can create an issue. You are also welcome to modify the script and contribute by creating a pull request.

### Example Usage
This is an example of how the script can be used, although there are other ways to use it. To show the help message, run the script by:
```
python latexport.py -h
```

- Copy the `latexport.py` file to the directory where your main `.tex` file is located.
- Open your terminal and go to the directory.
- Run the script by:
```
python latexport.py
```
After running the script, you will find a file in the directory with the extension `.merged.zip`. This zip file includes the main `.tex` file and all image files, with the latter being automatically renamed with prefixes such as "fig1_". However, note that `.bst`, `.bib` and `.bbl` files are not included in the zip file. Instead, the script merges the bibliography into the main `.tex` file within the zip file.
- Alternatively, you can run the script by:
```
python latexport.py -b
```
This time, the bibliography is not merged, and the `.bst` file (if necessary) and the `.bib` files included by `\bibliography` are added into the zip file.

### Configuration File
You can make more settings with a configuration file. The simplest way is to run `latexport.py` once, and you will see a sample configuration file with the extension `.ltxpconfig` in the same directory of the main `.tex` file. The file will include explanations and examples.

To manually add a file into the zip file, add this line to the configuration file:
```
add path/to/file  # filepath is RELATIVE TO THE MAIN TEX FILE.
```
To replace text in the LaTeX code, add this line to the configuration file:
```
replace <pattern> <replacement> # Replace <pattern> to <replacement> in the merged tex file. Regular expressions are supported. Here '.' matches any character INCLUDING A NEW LINE.
```
