library(Boruta)
traindata <- read.csv("dh_features_final.csv")
traindata <- traindata[,2:29]
set.seed(123)
boruta.train <- Boruta(RUL~ ., data = traindata, doTrace = 2)
print(boruta.train)