library(pheatmap)

data<-read.delim("Orthogroups.GeneCount_I4.4.tsv",header=T,row.names = 1)
pangenomeClass<-read.delim("pangenoma.classification.txt",header = F, sep = "\t")
colnames(pangenomeClass)<-c('Category', 'OG')
head(pangenomeClass)
pangenomeClass<-pangenomeClass[order(pangenomeClass$Category),]
rownames(pangenomeClass)<-pangenomeClass$OG
pangenomeClass$OG<-NULL
pangenomeClass$Category<-as.factor(pangenomeClass$Category)
head(pangenomeClass)
strainClass<-read.delim("isolates.txt", header=T, row.names = 1)
strainClass$Genome.size<-NULL
strainClass$Year.of.isolation<-as.factor(strainClass$Year.of.isolation)
strainClass$Country<-as.factor(strainClass$Country)
head(strainClass)
data$Total<-NULL

data2<-data
dim(data2)
data2[data2>1]<-1

ann_colors=list(Category = c(Accessory="#E69F00",Exclusive="#56B4E9",'Hard-core'="#009E73",'Soft-core'="#CC79A7"),
                Country  = c(Bolivia="#E69F00", Colombia="#56B4E9", 'Costa Rica'="#009E73", Ecuador="#CC79A7", Peru="#F0E442"))

data3 <- data2[match(rownames(pangenomeClass), rownames(data2)),]
colnames(data3) <- c("A4295", "B3", "C26", "Co12", "Co25", "Co29", "Co43", "Co44", "Co45", "Co52", "Co58", "Co65", "Co67", "Co74", "Co82", "Co84", "Co8", "E7", "Mr017", "Mr020", "Mr030", "P5")

pheatmap(data3, 
         cluster_rows=T, 
         show_rownames = F, 
         annotation_row = pangenomeClass, 
         annotation_col = strainClass,
         annotation_colors = ann_colors,
         legend_breaks=c(0,1),
         main='M. roreri pangenome'
)
