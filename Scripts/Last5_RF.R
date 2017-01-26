setwd('D://Github//Open_IIT_DA')
library(randomForest)
library(rpart)

rmse_val <- function(error)
{
  sqrt(mean(error^2))
}

data <- read.csv("dh_features_final.csv")
set.seed(123)
scaled_data <- scale(data[2:28], center = TRUE, scale = TRUE)
y <- data$RUL
scaled_data <- cbind(scaled_data, y)
scaled_data <- as.data.frame(scaled_data)
names(scaled_data)
#scaled_data <- scaled_data[,c(1:4, 6:18,21:28)]
scaled_data <- scaled_data[,c(1:4, 6:8,11:18,21:23,25,27:28)]
#scaled_data <- scaled_data[,c(1:4, 6:18,21:28)]

#smp_size <- floor(0.9 * nrow(scaled_data))
#set.seed(139)
#inTraining <- sample(seq_len(nrow(scaled_data)), size = smp_size)

#inTraining <- createDataPartition(scaled_data$RUL, p = 0.75, list = FALSE)
training <- scaled_data[1:200,]
testing <- scaled_data[201:333,]
testing <- subset(testing,testing$y<20)

#training <- scaled_data[1:333,]
#testing <- subset(scaled_data,scaled_data$y<6)

modelFit <- randomForest( y ~ .,data = training, importance=TRUE, proximity=TRUE )  
pred <- predict(modelFit, testing, type="response")
#pred <- floor(pred)
pred <- round(pred)
#misClasificError <- mean(ifelse(((pred >= testing$y - 3) & (pred <= testing$y + 3)), 0 , 1))
rmse <- rmse_val(pred - testing$y)