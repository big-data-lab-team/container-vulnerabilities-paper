# Vulnerability analysis of container images

This repository is a paper reporting on a vulnerability analysis of container images.

The paper is written in Latex and can be compiled as follows:
```
pdflatex -shell-escape paper ; bibtex paper ; pdflatex -shell-escape paper ; pdflatex -shell-escape paper
```

Data stored in `Data` was generated using the Anchore, Clair and Vuls 
container image scanners. 

The notebook in `analysis.ipynb` describes our data analysis and 
generates the figures of the paper.

The scripts in `Scripts` were used to update and minify container images.

TODOs
- add a README in `Data`, showing the command line used for each scanner
