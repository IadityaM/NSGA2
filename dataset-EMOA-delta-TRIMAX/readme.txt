./MOGA_TRI <f_name> <nog> <nos> <not> <alfa> <del> <nop> <ngen>

//input parameters:

//f_name: file name and type: string (tp)
//nog: # of genes/ probe-ids and and type: integer (21960)
//nos: # of replicates and and type: integer (4)
//not: # of substances and and type: integer (6)
//alfa: parameter for multiple genes/ probe-ids, replicates, substances removal and type: float (1.2)
//del:  maximum allowable Mean-Squared Residue score and type: float (0.019)
//nop: Population size for Genetic Algorithm and type: integer (100)
//ngen: # of generations for Genetic Algorithm and type: integer (100)


//output files:

//<S_i>.txt: Substances belong to each tricluster
//<G_i>.txt: Genes belong to each tricluster
//<R_i>.txt: Replicates belong to each tricluster
