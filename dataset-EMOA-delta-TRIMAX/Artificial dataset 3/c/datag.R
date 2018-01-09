#for(i in 1:30)
#{
#	f0<-paste("./tp_",(i-1),".txt",sep="")
#	tp_data<-read.delim(f0,sep="\t",header=FALSE)

#	fw<-paste("./tp",i,sep="")
#	write.table(tp_data,fw,sep="\t",append=FALSE,quote=FALSE,row.names=FALSE,col.names=FALSE)

#}


for(i in 1:3)
{
	f0<-paste("./tp_ind_tricl_",i,sep="")
	f1<-paste("./gene_ind_tricl_",i,sep="")
	f2<-paste("./samp_ind_tricl_",i,sep="")

	tp_ind<-read.table(f0,header=FALSE)
	gene_ind<-read.table(f1,header=FALSE)
	samp_ind<-read.table(f2,header=FALSE)

	tp_ind<-as.vector(tp_ind[,1])+1
	gene_ind<-as.vector(gene_ind[,1])+1
	samp_ind<-as.vector(samp_ind[,1])+1

	write.table(tp_ind,f0,append=FALSE,quote=FALSE,row.names=FALSE,col.names=FALSE)
	write.table(gene_ind,f1,append=FALSE,quote=FALSE,row.names=FALSE,col.names=FALSE)
	write.table(samp_ind,f2,append=FALSE,quote=FALSE,row.names=FALSE,col.names=FALSE)

}
	
