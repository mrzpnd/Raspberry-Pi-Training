# test = "sample {}".format("program")
# print(test)
# test1="sample"+"program"
# print(test1)
# test2="{} program".format(1)
# print (test2)
# test3=str(1)+"program"
# print(test3)
# name= "my name is {} and im an {}".format("miraz","engineer")
# print(name) 
# faculty_batch="I am from {faculty} and {batch}".format(batch="2016",faculty="electronics and communication")
# print(faculty_batch) 

# num=10
# print(num)
# num1=10.5
# print(num1)
# num2=10/3
# print(num2)
# num4=10.0+2
# print(num4)
# print(10/3)
# print(2**3)
# #conditional statements
# x=10 
# if x<10:
#     print("The number is less than 10")
# else:
#     print("The number is greater than 10")




# y=11

# if y%2==0:
#     print("the number is even")
# else:
#     print("the number is odd")





# z=-0
# if z==0:
#     print("the number is equal to zero")
# elif z<0:
#     print("the number is less than zero")
# else :
#     print("the number is greater than zero")

# z=int(input("enter any number"))

# if z==0:
#     print("the number is equal to zero")
# elif z<0:
#     print("the number is negative")
# else :
#     print("the number is positive")


# x=1;
# while x<=10:
#     print(x)
#     x+=1



# for i in range(1,11,1):
#     print(i)



# x=int(input("enter any number"))
# for i in range(1,x,2):
#     print(i)


# print(range(10))
# print(range(0,10))
# print(range(0,10,1))

# list


# numbers=[1,2,3,4,5,"ncit"]
# print(numbers[5])
# print(numbers[-6])



# items=[1,2,3,["hello",[1,2,3,"world"]],"ncit"]
# print(items[3][1][3])


# items=[5,6,[1,2,[1,2],[1,"hello",["world"]],"ncit"]]
# print(items[2][4])
# print(items[2][3][2][0])
# print(items[2][3][1])



# numbers=[1,2,3,4,5,6]
# for i in numbers:
#     print(i)
    


# numbers=[1,2,3,4,5,6,"ncit","next"]


# numbers.append("ashok")
# numbers.append("1")
# numbers.append("sushil")
# numbers.append("rabin")  #append adds content at the last
# numbers.append("arvind")
# numbers.insert(0,"nepal") #insert doesn't replace the content but shifts it right
# numbers.insert(4,"Great")
# numbers[0]="python"  #This is used to replace the  content of the corresponding index
# print(numbers)
# print(len(numbers)) #this gives the length of the list
# last_item=numbers.pop()  #this helps to pop out the last element of the list
# print(last_item)
# print(numbers)
# first_item=numbers.pop(0)     #this pops out the 1st item in the list
# print(first_item)
# print(numbers)
# print (numbers[0:5:1])  #slicing [start:end+1:step]
# print(numbers[1:5:2])
# print(numbers[1:5])
# print(numbers[::-1])    #this displays the list in reverse order


# numbers=[]
# for i in range(1,1001:
#     x=i**2                     #forms the list of squares of numbers from 1 to 1000
#     numbers.append(x)

# print(numbers)




# squares=[num*num for num in range(1,1001)]  #list comprehension
# print(squares)

# items=["ncit","kcc","nce","kec","ioe","kist"]
 
# college=["hawa college {} ".format(name) for name in items     #list comprehension
# #college=["hawa college "+name for name in items]
# print(college) 

#string,tuple

# num1=[1,2,3]
# num2=[4,5,6,7]
# num3=num1 + num2   #concatenate two lists
# print(num3)

# l=(1,2,3)  #tuple

sample_d={        #dictionary similar to structure in C and object in c++
"hello":"world",
"sample":2,
(1,2):[1,2,3,4],
"ashok":"magar",
"rabin":"khadka",
"subash":"wagle",
"sushil":"tiwari",
"sucil":"buju",
"rukum":"rana",
"miraz":"pandey"
}
# print(sample_d)
# print(sample_d["rabin"])
# print(sample_d.pop("miraz"))
# # print(sample_d.get["sam"]) if the argument that is not the key of the dictionary is passed in the square bracket, error will occur
# print(sample_d.get("sam")) #if the argument that is not the key of the dictioary is passed in the small bracket, none is returned as the value

# print(sample_d.keys())
 
# for k in sample_d.keys():
#     print(sample_d[k])

# for k in sample_d:
#     print(k)



# for k,v in sample_d.items():
#     print(k,v)


# print(sample_d.values())


# danger={
#     "NCIT":"Nepal College Of Information Technology",
#     "students_no":"2500",
#     "teachers":[{"name":"shiva hari","designation":"HOD"},{"name":"ujjwal koirala","designation":"principal"}],
#     "alumni":["bhatta sarkar","jigree","mitru","nana bhai"],
#     "est":"2001"



# }
# print(danger["teachers"][1]["designation"])
# print(danger["alumni"][0:4:3])
# print(danger["alumni"][0])
# print(danger["alumni"][3])


# def hello_func():
#     print("hello world")  #function


# hello_func()


# def add_f(a,b):
#     return(a+b)

# c=add_f(100,5)
# print(c)

# def square(a,b):

#     squares= a + b   #function that takes two list and returns the concatenated list
#     return(squares)



# l=[1,2,3]
# c=[4,5,6]
# m=square(l,c)
# print(m)

def func(d):
    m=[d.keys()]
    return(m)

d={
    "name":"miraz",
    "class":"12",
    "address":"kaushaltar",

}
l=func(d)
print(l)