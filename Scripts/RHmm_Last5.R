library(quantmod)
library(HMM)
library(R.matlab)
library(depmixS4)
setwd("D://Github//Open_IIT_DA")

mat_data = readMat("dbhole.mat")
name <- names(mat_data)
dh_features = data.frame()
training <- mat_data[[1]]
for(i in 2:200){
  training <- rbind(training, mat_data[[i]])
}
testing <- mat_data[[219]]
for(i in 220:223){
  testing <- rbind(testing, mat_data[[i]])
}
for(i in 240:244){
  testing <- rbind(testing, mat_data[[i]])
}
for(i in 285:289){
  testing <- rbind(testing, mat_data[[i]])
}
for(i in 329:333){
  testing <- rbind(testing, mat_data[[i]])
}
