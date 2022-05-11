# litmus-test-paper 
Analysis pipeline and code to reproduce part of the results presented in the manuscript:
 `A litmus test for classification of recognition mechanisms of transiently binding proteins`
 by Chakrabarti, Olsson et al. Nat Comms 2022.

## Dependencies
We provide a environment YAML file reflecting the conda environment used to generate the results.

Some analysis scripts rely on the separate downloads:
 - Pre-processed molecular dynamics trajectories (see below)
 - Serialized Bayesian MSM model (PyEMMA) http://ftp.imp.fu-berlin.de/pub/solsson/model.pyemma.zip

## Disclaimer
We provide these materials _as is_ and as such cannot guarantee any support in getting the code running on your system. Please post questions/bugs/problems in the GitHub Issues. 

## Citing these resources
Molecular Dynamics data:
```
@misc{md-data,
	author = {Simon Olsson and Thomas R.\ Weikl},
	howpublished = {https://doi.org/10.17617/3.8o, Edmond, V1},
	title = {{1.68 milliseconds of MD simulation trajectories for the binding of ubiquitin to the SH3c domain from CIN85}}}
```
Code and scientific findings:
```
@article{chakrabartiolsson2022,
	author = {Kalyan S. Chakrabarti and Simon Olsson and Supriya Pratihar and Karin Giller and Kerstin Overkamp and  Ko On Lee and  Vytautas Gapsys and Kyoung-Seok Ryu and Bert L. de Groot and Frank No\'e and Stefan Becker and Donghan Lee and Thomas R.\ Weikl and Christian Griesinger },
journal = {Nat. Commun.},
	journal-full = {Nature communications},
	title = {A litmus test for classification of recognition mechanisms of transiently binding proteins},
	year = {2022}}
```
