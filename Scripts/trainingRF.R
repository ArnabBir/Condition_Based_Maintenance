library(randomForest)
library(rpart)

data <- read.csv("dh_features_final.csv")
scaled_data <- scale(data[2:28], center = TRUE, scale = TRUE)
y <- data$RUL
scaled_data <- cbind(scaled_data, y)
scaled_data <- as.data.frame(scaled_data)
smp_size <- floor(0.9 * nrow(scaled_data))
set.seed(139)
inTraining <- sample(seq_len(nrow(scaled_data)), size = smp_size)

#inTraining <- createDataPartition(scaled_data$RUL, p = 0.75, list = FALSE)
training <- scaled_data[inTraining, ]
testing <- scaled_data[-inTraining, ]
modelFit <- randomForest( y ~ .,data = training, importance=TRUE, proximity=TRUE )  
pred <- predict(modelFit, testing, type="response")
pred <- round(pred)
#misClasificError <- mean(ifelse(((pred >= testing$y - 3) & (pred <= testing$y + 3)), 0 , 1))
rmse = sqrt(mean(pred - testing$y)^2)
