// students array
var students = [
    {first_name:  'Michael', last_name : 'Jordan'},
    {first_name : 'John', last_name : 'Rosales'},
    {first_name : 'Mark', last_name : 'Guillen'},
    {first_name : 'KB', last_name : 'Tonel'}
]

// users object
var users = {
    students: [
        {first_name:  'Michael', last_name : 'Jordan'},
        {first_name : 'John', last_name : 'Rosales'},
        {first_name : 'Mark', last_name : 'Guillen'},
        {first_name : 'KB', last_name : 'Tonel'}
    ]
}

function printNames(arr) {
    for(var i = 0; i < arr.length; i++) {
        console.log(arr[i].first_name.toUpperCase() + " " + arr[i].last_name.toUpperCase());
    }
}

// using students array
printNames(students);
// create an empty line between outputs
console.log('');
// using users object
printNames(users.students);