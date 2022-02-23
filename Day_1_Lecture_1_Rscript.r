#===============================================================
#                 Basic R programming
#===============================================================
# TITLE  : LECTURE 1 AM, R as calculator
# BY     : PALANG CHOTSIRI
# DATE   : 11 Jan 2021
#===============================================================


##========##
## Part 1 ##
##========##

## Basic calculations are easy:
1+1
2-1
6*8
1/2
3^2
## (To run any of these, you can do one of the following:
##  [a] Select the text, ctrl-c, then put the cursor in the console and hit ctrl-v
##  [b] Select the text and hit ctrl-enter or ctrl-r, but note on some computers only one of these works
##  [c] Put the cursor on the line and hit ctrl-enter or ctrl-r. This runs the whole line
##  [d] Select text or put the cursor on the line and click the Run button above
##  [e] If you want to run EVERY command in the file, hit the Source button above.)

# <---- this symbol is a comment character
# anything after this does not get run by R


##========##
## Part 2 ##
##========##

## You can store values in objects using <- or =
## If you use =, the thing on the left becomes the same as the thing on the right.
x = 2
y <- 2
3 -> z
x
y
z
x + y
x = y+z
x
## Note that x changed values from 1 to 5 because we reassigned its value


#===================================================================#
# Question 1: If you type the following sequence, what will happen? #
#===================================================================#
a = 3
b <- 6
b -> a


a # what is this equal to?
b # what is this equal to?

# Note the difference between these:
6+7
a=6+9
# The first one prints the answer to screen
# The second one stores the answer in 'a' but does not print

class(a)

a <- as.character(a)
a

print(a)

class(a)

a <- as.numeric(a)
a

##========##
## Part 3 ##
##========##

## There are many of the basic mathematical functions built into R:
sqrt(9)
sin(0)
cos(0)
x = 1.5*pi
y = sin(x)
x = log(10)
# log[10] this doesn't work!
# log{10} this also doesn't work!
x = log(10, base = 2)
x = log10(10)
y = exp(x)
x = abs(-2.5)

#round = ปัดทศนิยมออก
x = round(2.1254578)

#digits = 2 เอาทศนิยม 2 ตำแหน่ง 
x = round(2.1254578, digits = 2)
## For all these functions, there are one (or more) arguments in brackets, and the results are either displayed to screen or stored in a value, depending on whether you used an = or <- or not.

#==================================================================#
# Question: why when you type abs(-2.5) something is printed       #
# to the screen but when you type x=log(10) nothing is displayed?  #
#==================================================================#



##========##
## Part 4 ##
##========##

## You can make your own functions like this:
square=function(x)
{
  y=x^2
  return(y)
}


adder=function(x,y)
{
  return(x+y)
}


adder(5,7)
square(8)


##========##
## Part 5 ##
##========##

## You can also store multiple values in the same object, either as a vector (like one column with many rows in excel), matrix (like several columns and many rows in excel) or array (like several columns, several rows and several sheets in excel). For now, we just look at vectors:

#seq คือ sequence 
x = seq(0,1,by = 0.1)  # เริ่ม 0 จบที่1 โดยเพิ่มที่ละ 0.1

#หรืออีกแบบ
y = 0:10


z = c(3,1,4,1,5,9,3) #c คือเชื่อมแต่ละตัว โดยภายใน=vector[คล้าย ๆ list]

# You can then do stuff to the vectors as if they were just normal numbers
x+y # This works because x and y are the same length
x+1 # This works because R works out to repeat 1 for each entry in x


x+z # This gives a warning message: why? 

#================================================#
# Question: Why does x+z give a warning message? #  [เพราะความยาวไม่เท่ากัน]
#================================================#

square(y)
y
sqrt(x) 
#จะเห็นว่าไม่ต้องใช้loopเหมือนpy


## If you want to extract out one or more entries from a vector, you use [] brackets:
#ภาษาR เริ่มจาก1 นาจา
x[3]
x[c(3,4)]
x[3:5]


# You can stick vectors together using the c() function:
# c stands for 'concatenate'
a=c(1,2,3)
b=c(4,5)

c(a,b)
#เอาa มาต่อ b


##========##
## Part 6 ##
##========##


## Logic
# We can ask R if a number is more than another
3>2
# R treats TRUE as 1 and FALSE as 0

(3>2)+0
(3>2)+1

# This works for vectors too
a=c(0,1,2,3,4)
a>2
a<=3
# To check for equality we need to use a double ==
a==4
# This is different! Why?
a=4

#===================================================================#
# Question: what is the difference between the following two lines? # [เพราะ = คือการกำหนด ==คือการเช็ค]
#===================================================================#
a=c(0,1,2,3,4)

which(a>2) #aตัวไหนที่มากกว่า2บาง มันจะแสดงตำแหน่งของตัวนั้น ๆ มา

i= which(a>2) 
a[i]



# You can get R to do something only if a 
# condition is true:
x=3
y=1

if(x<0)y=x  #False
y


if(x>0)y=x else y=-x #True
y

#============================================#
# Question: what does the following code do? #
#============================================#
alldata <- c(-1.4, 5.3, 7.8, -0.3, -4.5, 9.9, 6.6, -2.5)
i=which(alldata>0)
somedata <- alldata[i]

somedata #จะแสดงผลออกมา เป็นตัวที่มากกว่า 0



## You can use logic statements inside a function like this:
squareroot=function(x)
{
  if(x<0) return(sqrt(-x))
  return(sqrt(x))
}


# This can stop errors happening!
sqrt(-1) # basic function
squareroot(-1) # my function


##========##
## Part 8 ##
##========##

## Loops: if you are doing something for each entry in a vector it can sometimes be useful to use a loop to go through each one.  For example:
a=c(2,4,6,8)
b=c() # creates an empty vector

for(i in 1:4)
{
  b[i]=square(a[i])
}
b

#===============================================#
# Question: can you think of any other way to   #
# create b with exactly the same numbers in it? #
#===============================================#

## These can be more complicated. Eg
x=c(-1,4,-9,16,-25,36)
y=c()

for(i in 1:6)
{
  if(x[i]>=0)y[i]=sqrt(x[i])
  if(x[i]<0)y[i]=sqrt(-x[i])
}
y

# If you don't know how long the vector is, use length():
for(i in 1:length(x))
{
  if(x[i]>=0)y[i]=sqrt(x[i])
  if(x[i]<0)y[i]=sqrt(-x[i])
}

y

##========##
## Part 9 ## Data types
##========##

##
## 9.1 Vectors
##

vec1 <- c(10, 20, 15, 40)  # numeric vector
vec2 <- c("a", "b", "c", NA)  # character vector
vec3 <- c(TRUE, FALSE, TRUE, TRUE)  # logical vector
vec4 <- gl(4, 1, 4, label = c("l1", "l2", "l3", "l4"))  # factor with 4 levels

length(vec1)  
print(vec1[1])  
print(vec1[1:3])  

# initialised vector without assign value
numericVector <- numeric(100) 

## Manipulating vector
## Subsetting

logic1 <- vec1 < 15  # create a logical vector, TRUE if value < 15
vec1[logic1]  # elements in TRUE positions will be included in subset
vec1[1:2]  # returns elements in 1 & 2 positions.
vec1[c(1,3)]  # returns elements in 1 & 3 positions
vec1[-1]  # returns all elements except in position 1. ไม่เอาตัวที่1 **-แปลว่าเอาออก

## Sorting vector
sort(vec1)  # ascending sort
sort(vec1, decreasing = TRUE)  # Descending sort 

## Sorting another way
vec1[order(vec1)]  # ascending sort
vec1[rev(order(vec1))]  # descending sort

## Creating vector sequences and repetitions
seq(1, 10, by = 2)  # diff between adj elements is 2
seq(1, 10, length=25)  # length of the vector is 25
rep(1, 5)  # repeat 1, five times.
rep(1:3, 5)  # repeat 1:3, 5 times
rep(1:3, each=5)  # repeat 1 to 3, each 5 times.

## Remove missing value
vec2 <- c("a", "b", "c", NA)  # character vector
is.na(vec2)  # missing TRUE  #แปลว่าตัวไหนที่เป็นNAบ้าง
!is.na(vec2)  # missing FALSE #! = not
vec2[!is.na(vec2)]  # return non missing values from vec2

## Sampling สุ่ม
set.seed(100)  # optional. set it to get same random samples.
sample(vec1)  # sample all elements randomly
sample(vec1, 3)  # sample 3 elem without replacement   #เอามา 3 ตัว
sample(vec1, 10, replace=T)  # sample with replacement #เอามา 10 ตัว โดยซ้ำได้

sample(vec1, 4, replace=F ,prob = NULL)

sample(1:100, 1)
sample(1:100, 1)

## Assign vector name
temps <- c(72,71,68,73,69,75,71)
temps

names(temps) <- c('Mon','Tue','Wed','Thu','Fri','Sat','Sun')
temps

temps['Mon']

## Working with vectors
vec1 <- c(1, 3, 6, 8, -4)
vec2 <- c(5, 3, -9, 4, 8)

vec1 + vec2
vec1 - vec2
vec1*vec2
vec1/vec2

## Function on vectors
sqrt(vec1)
sqrt(abs(vec1))

log(vec1)
log(abs(vec1))

sum(vec1)
sd(vec1)
var(vec1)
max(vec1)
min(vec1)
prod(vec1)

## See short_refcard

##
## 9.2 Matrix
##

1:10
v <- 1:10

matrix(v)
matrix(v, nrow = 2)
matrix(1:12, byrow = TRUE, nrow = 4)
matrix(1:12, byrow = FALSE, nrow = 4)

## creating a matrix of stock price, not the real price
ptt  <- c(450,451 ,452,445,468)
dtac <- c(230,231 ,232,236,228)
stocks <- c(ptt, dtac)
stock.matrix <- matrix(stocks ,byrow=TRUE ,nrow=2)
stock.matrix

## Naming matrix
days <- c('Mon','Tue','Wed','Thu','Fri')
st.names <- c('PTT','DTAC')

colnames(stock.matrix) <- days
rownames(stock.matrix) <- st.names

stock.matrix

## Matrix arithmatics
mat <- matrix(1:6,byrow=TRUE ,nrow=2)
mat

2*mat
mat/2
1/mat
mat^2
mat**2

mat >= 3
mat + mat
mat * mat
mat / mat
mat ** mat

## Matrix multiplication 
mat2 <- matrix(1:9, nrow = 3)
mat2

mat2 %*% mat2

## Recall stock matrix
stock.matrix
rowSums(stock.matrix)
colSums(stock.matrix)

BAY <- c(111,112 ,113 ,120,145)
set.stocks <- rbind(stock.matrix ,BAY)
set.stocks

avg <- rowMeans(set.stocks)
avg

set.stocks <- cbind(set.stocks, avg)
set.stocks

## matrix selection and indexing 
mat <- matrix(1:16,  byrow = TRUE, nrow = 4)
mat

## Matrix[row, col]
mat[1,]
mat[,1]
mat[2:3,]
mat[1:3,4]

