library(randomForest)
library(rpart)
library(Matrix)
library(xgboost)
library(stringr)
library(caret)

mat_data = read.csv("D://Github//Open_IIT_DA//moving_average.csv")
pca = prcomp(mat_data[,2:54],center = T,scale. = T)
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
testing <- subset(testing,testing$y<10)

#training <- scaled_data[1:333,]
#testing <- subset(scaled_data,scaled_data$y<6)

#modelFit <- randomForest( y ~ .,data = training, importance=TRUE, proximity=TRUE )  
xgb <- xgboost(data = data.matrix(training), 
               label = training$y, 
               #eta = 0.3,
               eta = 0.55,
               max_depth = 15, 
               nround=25, 
               subsample = 0.5,
               colsample_bytree = 0.5
               #eval_metric = "merror",
               #objective = "multi:softprob",
               #num_class = 45,
               #nthread = 3
)
#pred <- predict(modelFit, testing, type="response")
pred <- predict(xgb, data.matrix(testing))

pred <- round(pred)
pred <-ifelse((pred < 0), 0 , pred)
#misClasificError <- mean(ifelse(((pred >= testing$y - 3) & (pred <= testing$y + 3)), 0 , 1))
rmse <- sqrt(mean((pred - testing$y)^2))

#testing$Predicted_RUL = pred
#i = as.character(i)
#finalcsv = cbind(i,testing$y,j)
#write.csv(finalcsv,"result2.csv")
