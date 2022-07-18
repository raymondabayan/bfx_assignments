library(data.table)
library(ggplot2)
library(dplyr)

list.files()
counts <- fread("count_matrix.csv")
names <- fread("peak_names_out.csv")
data <- cbind(names, counts)

