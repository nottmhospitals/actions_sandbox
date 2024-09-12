stringFunction <- function() 
{
  print("Hello World!")
}





result <- stringFunction()

#try(assert("string should return 'Hello World'",
stopifnot(result == "Hello World!")
print("Test has passes")
