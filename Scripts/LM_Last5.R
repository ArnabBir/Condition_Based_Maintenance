setwd('D:/Github/Open_IIT_DA')
library(xgboost)
library(readr)
library(Matrix)
library(stringr)
library(caret)
library(car)

rmse_val <- function(error)
{
  sqrt(mean(error^2))
}


data <- read.csv("dh_features_Final.csv")
set.seed(123)

scaled_data <- scale(data[2:28], center = TRUE, scale = TRUE)
y <- data$RUL
scaled_data <- cbind(scaled_data, y)
scaled_data <- as.data.frame(scaled_data)
names(scaled_data)
scaled_data <- scaled_data[,c(1:28)]
#sparse_matrix <- sparse.model.matrix(y ~ ., data = scaled_data)
training <- scaled_data[1:200,]
testing <- scaled_data[201:333,]
testing <- subset(testing,testing$y<20)
xgb <- lm(y~ ., data = training)

pred <- predict(xgb, testing)
pred <- round(pred)
rmse <- rmse_val(pred - testing$y)