# Covid-19-analysis
### Com a chegada do novo Covid19 se fez necessário que todos os cientístas do pais, que podem ajudar, cedam um pouco do seu tempo e conhecimento para pesquisar e encontrar novos dados que possam ajudar no combate dessa pândemia. 
#### O intuito dessa pesquisa é ultilizar RINs( Residue Iteration Network ) para identificar quais regiões do genoma do vírus são mais propensos a mudanças.

![fluxo 2(Under revision)](https://github.com/bombermal/Covid-19-analysis/blob/master/Uml/Covid%20-%20Total.png)
## Pt 1
 - [X] Read aligned Fasta files
    - [X] Load Fasta on DataFrame
 - [X] Counting SNPs
    - [X] Save counted DF as csv
 - [X] Plot SNPs positions
 
## Pt 2
 
 - [X] Read PDBs
    - [X] Load PDBs as DataFrames
    - [ ] Convert PDBs list to nodes
    - [ ] Convert samples list to nodes
 - [ ] Align PDBs with samples
 - [ ] Determine values of degree and betwenness
 - [ ] Plot degree and betwenness dristribution

## Versão para docker
![fluxo 1(Terminal)](https://github.com/bombermal/Covid-19-analysis/blob/master/Uml/Covid%20-%20Terminal.png)

- [X] Terminal version of the SNPS plot code
- [X] Dockerfile
- [X] Local test
- [ ] Remote test
