install.packages("ggplot2")
library(ggplot2)


addFunction <- function(a,b) 
{
  x <- a
  y <- b
  result <- a + b   
  print(result)
}

addFunction(10,10)