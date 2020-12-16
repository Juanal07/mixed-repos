const express = require('express')
const { getBooks, createBook } = require('./model')

const app = express()

app.use(express.json())

app.get('/api', (req, res) =>{
    res.send('Hello you!')
})

app.get('/api/books', (req,res) => {
       getBooks((books) => res.send(books))
})

app.post('/api/books', (req,res) =>{
    createBook(req.body, () => res.send())
})

app.listen(3000, () => {
    console.log('Escuchando en el puerto 3000')
})

// postman - cliente http para hacer peticiones
//
// curl --location --request POST 'localhost:3000/api/books' \
//
// --header 'Content-Type: application/json' \
//
// --data-raw ' {
//
// "title": "El Principito",
//
//     "author": "Antoine de Saint-Exupéry"
//
// }