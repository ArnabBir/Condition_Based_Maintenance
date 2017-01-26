library(randomForest)
library(rpart)
library(Matrix)
library(xgboost)
library(stringr)
library(caret)

mat_data = read.csv("D://Github//Open_IIT_DA//dh_features_Final.csv")
pca = prcomp(mat_data[,2:28],center = T,scale. = T)
sd = pca$sdev
var = sd^2
perc_var = var/sum(var)
scaled_data = pca$x[,1:6]
y <- mat_data$RUL
scaled_data <- cbind(scaled_data, y)
scaled_data <- as.data.frame(scaled_data)
#smp_size <- floor(0.9 * nrow(scaled_data))
set.seed(123)
#inTraining <- sample(seq_len(nrow(scaled_data)), size = smp_size)

#inTraining <- createDataPartition(scaled_data$RUL, p = 0.75, list = FALSE)
training <- scaled_data[1:200,]
testing <- scaled_data[201:333,]
testing <- subset(testing,testing$y<20)

#training <- scaled_data[1:333,]
#testing <- subset(scaled_data,scaled_data$y<6)

#modelFit <- randomForest( y ~ .,data = training, importance=TRUE, proximity=TRUE )  
xgb <- lm(y~ ., data = training)
#pred <- predict(modelFit, testing, type="response")
pred <- predict(xgb, testing)

pred <- round(pred)
pred <-ifelse((pred < 0), 0 , pred)
#misClasificError <- mean(ifelse(((pred >= testing$y - 3) & (pred <= testing$y + 3)), 0 , 1))
rmse <- sqrt(mean((pred - testing$y)^2))

testing$Predicted_RUL = pred
i = as.character(i)
finalcsv = cbind(i,testing$y,j)
write.csv(finalcsv,"result2.csv")
