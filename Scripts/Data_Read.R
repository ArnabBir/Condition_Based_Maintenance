for(i in 1:21){
  i=2
  file <- paste(1:3, c("D://Github//Open IIT DA//Data/Filename_d1h", i, ".csv"))
  file <-strwrap(file)
  data <- read.csv(file)
  summary(data)
  capture.output(s, file = "D://Github//Open IIT DA//summary.txt")
}