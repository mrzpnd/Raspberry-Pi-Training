
// console.log(name)
// var name="jepi"
// console.log(name)
// name="arvind" 
// var x
// console.log(x)


// console.log(1+"node js")
// let x="name"
// console.log(x)
// for(var i=0;i<10;i++){
//     console.log("hello")
// }



// console.log(name)
// name="jepi"


// for(var i=100;i<=1000;i+=2){
// console.log(i)
// // }
// if(1=='1')console.log("success in first")
// // if(1==='1')console.log("success in second")

// var sample={
//     name:"arvind",
//     faculty:"electronics",  //object---property:value
//     batch:"2016"
// }
// console.log(sample)
// console.log(sample.faculty)
// //console.log(sample[faculty]) not this way
// console.log(sample["fac"+"ulty"])
// var sample={
//     name:"random",
//     faculty:"elx",
//     batch:"2016"
// }
// for(var x in sample){
//     console.log(sample[x])
// }



// var x=[1,2,3,"hello","world"] //array
// console.log(x)
// for(var i=0;i<x.length;i++){
// console.log(x[i])
// }

// for(var i of x){
//                     //of gives the value
//     console.log(i)  //another way       
// }
// for(var i in x){
//                     //in gives the index
//     console.log(i)  //another way       
// }
// for(var i in x){

//     console.log(x[i])  //another way       
// }



// function hello(){
//     console.log("hello")
// }
// hello()
// console.log(hello())
// console.log(hello)



var stu={
    name:"jepi yadav",
    faculty:"electronics",
    batch:"2016",
    getfaculty: function fac(){
        return stu.faculty
    },
    getbatch: function(){
        return stu.batch
    }

}
console.log(stu)
console.log(stu.getfaculty())
console.log(stu.getbatch())
console.log(stu.batch)
console.log(stu.faculty)
var g=stu.getbatch
var f=stu.getbatch()

console.log(f)
console.log(g)