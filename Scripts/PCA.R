library(R.matlab)
mat_data = read.csv("D://Github//Open_IIT_DA//dh_features_Final.csv")
pca = prcomp(mat_data[,2:27],center = T,scale. = T)
sd = pca$sdev
var = sd^2
perc_var = var/sum(var)
scaled_data = pca$x[,1:8]
