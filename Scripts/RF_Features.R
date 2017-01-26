library(randomForest)
library(rpart)
library(caret)
data <- read.csv("dh_features_final.csv")
col.names <-names(data[2:28])
scaled_data <- scale(data[2:27], center = TRUE, scale = TRUE)
y <- data$RUL
scaled_data <- cbind(scaled_data, y)
#gbmimp <- varImp(scaled_data, scale = FALSE)
modelFit <- randomForest( y ~ .,data = scaled_data, importance=TRUE, proximity=TRUE )  

importance(modelFit)
varImp(modelFit)